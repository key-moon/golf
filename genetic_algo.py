# 時間がかかるかわりに強いoptimizer
# optimizer_results/genetic_algo/ に途中状態や最終状態のdeflate fileを保存している
# プログラム改変後に再度走らせたい場合は current_states / input_deflate / input_variable を削除してから再実行で良い

import argparse
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Dict, Optional, Sequence
import subprocess
import traceback

import zlib
import zopfli

from deflate_optimizer.dump_deflate_stream import dump_deflate_stream
from deflate_optimizer.load_deflate_text import load_deflate_stream
from deflate_optimizer.enumerate_variable_occurrences import list_var_occurrences
from deflate_optimizer.variable_conflict import build_conflict_report
from compress import get_embed_str, optimize_deflate_stream, determine_wbits, signed_str
from strip import strippers
from utils import get_code_paths, viz_deflate_url


@dataclass
class GAExecutionResult:
    optimized_bytes: Optional[bytes]
    bit_length: Optional[int]
    stdout: str
    stderr: str
    timed_out: bool
    returncode: Optional[int]
    output_text: str
    workdir: Optional[str] = None
    error: Optional[str] = None


def _truncate(text: str, limit: int = 2000) -> str:
    # if bytes, decode as utf-8 with replacement
    if isinstance(text, bytes):
        text = text.decode("utf-8", errors="replace")
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."

def _resolve_source(task_dir: str, task_id: int) -> Path:
    paths = sorted(get_code_paths(task_dir, task_id))
    if not paths:
        raise FileNotFoundError(f"No source found for {task_dir=}, {task_id=}")
    if 1 < len(paths):
        print(
            f"[genetic_algo] multiple sources found, selecting {paths[0]}",
            file=sys.stderr,
        )
    return Path(paths[0])


def _build_variable_dump(code: str) -> str:
    occ_text = list_var_occurrences(
        code,
        as_text=True,
        nostrip=True,
        include_exec=True,
    )
    conflict_text = build_conflict_report(
        code,
        occ_text,
        assume_preprocessed=True,
        as_text=True,
    )
    if occ_text and not occ_text.endswith("\n"):
        occ_text += "\n"
    if conflict_text and not conflict_text.endswith("\n"):
        conflict_text += "\n"
    return occ_text + conflict_text


def _compress_code(
    code: str,
    *,
    use_zopfli: bool,
) -> tuple[bytes, str, int]:
    code = code.encode("utf-8")
    zopfli_param = 2000
    if use_zopfli:
        compressed = zopfli.zlib.compress(code, numiterations=zopfli_param, blocksplitting=False)[2:-4]
        # compressed_splitting = zopfli.zlib.compress(val, numiterations=zopfli_param)[2:-4]
        # if len(compressed_splitting) < len(compressed):
        # compressed = compressed_splitting
    else:
        compressed_9 = zlib.compress(code, level=9, wbits=-9)
        compressed_15 = zlib.compress(code, level=9, wbits=-15)
        compressed = compressed_9 if len(compressed_9) < len(compressed_15) else compressed_15

    deflate_text = dump_deflate_stream(compressed)
    return compressed, deflate_text


def _run_genetic_algorithm(
    deflate_text: str,
    variable_text: str,
    *,
    binary_path: Path,
    timeout_sec: Optional[int],
    work_dir: Path,
    output_path: Path,
    py_output_path: Path,
    snapshot_interval_sec: int = 10,
) -> GAExecutionResult:
    work_dir.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    deflate_path = work_dir / "input_deflate.txt"
    variable_path = work_dir / "input_variable.txt"
    out_deflate_path = work_dir / "output_deflate.txt"
    out_variable_path = work_dir / "output_variable.txt"
    states_path = work_dir / "current_states.txt"

    deflate_path.write_text(deflate_text, encoding="utf-8")
    variable_path.write_text(variable_text, encoding="utf-8")

    for path in (out_deflate_path, out_variable_path):
        if path.exists():
            path.unlink()

    cmd = [
        str(binary_path),
        str(deflate_path),
        str(variable_path),
        str(out_deflate_path),
        str(out_variable_path),
        str(states_path),
    ]

    @dataclass(frozen=True)
    class SnapshotCacheEntry:
        raw_compressed: bytes
        embed: bytes
        extra_overhead: int
        res: bytes

    # 一度最適化した圧縮結果を覚えて再利用する
    seen_cache: Dict[bytes, SnapshotCacheEntry] = {}
    snapshot_warning_emitted = False

    py_output_best_len: Optional[int] = None
    try:
        py_output_best_len = py_output_path.stat().st_size
    except FileNotFoundError:
        py_output_best_len = None
    except OSError:
        py_output_best_len = None

    lib_name = "zlib"

    def snapshot_once() -> Optional[tuple[int, bytes]]:
        nonlocal snapshot_warning_emitted, py_output_best_len
        if not out_deflate_path.exists():
            return None
        try:
            text = out_deflate_path.read_text(encoding="utf-8").strip()
        except OSError:
            return None
        if not text:
            return None
        try:
            bit_length, compressed = load_deflate_stream(StringIO(text))
        except Exception:  # pylint: disable=broad-except
            if not snapshot_warning_emitted:
                print(
                    (
                        "[genetic_algo] warning: failed to parse in-progress GA output; "
                        "will retry on next snapshot"
                    ),
                    file=sys.stderr,
                )
                snapshot_warning_emitted = True
            return None
        entry = seen_cache.get(compressed)
        if entry is None:
            print('[genetic_algo] caching new snapshot result...', file=sys.stderr)
            raw_compressed = optimize_deflate_stream(
                compressed,
                lambda x: len(get_embed_str(x)),
                num_iteration=5000,
                num_perturbation=3,
                tolerance_bit=16,
                # terminate_threshold=2 + len(val) + 1,
                seed=1234,
            )
            embed = get_embed_str(raw_compressed)
            extra_overhead = len(embed) - (len(raw_compressed) + 2)
            extra_args = determine_wbits(raw_compressed)
            prefix = (
                f"#coding:L1\nimport {lib_name}\nexec({lib_name}.decompress(bytes("
            ).encode()
            suffix = b",'L1')" + extra_args.encode() + b"))"
            res = prefix + embed + suffix
            entry = SnapshotCacheEntry(
                raw_compressed=raw_compressed,
                embed=embed,
                extra_overhead=extra_overhead,
                res=res,
            )
            print('[genetic_algo] done caching new snapshot result.', file=sys.stderr)
            seen_cache[compressed] = entry
        else:
            raw_compressed = entry.raw_compressed
            extra_overhead = entry.extra_overhead
            res = entry.res

        output_path.write_bytes(raw_compressed)

        current_best = py_output_best_len
        if current_best is None:
            try:
                current_best = py_output_path.stat().st_size
            except FileNotFoundError:
                current_best = None
            except OSError:
                current_best = None
        if current_best is None or len(res) < current_best:
            py_output_path.write_bytes(res)
            py_output_best_len = len(res)
        else:
            py_output_best_len = current_best

        message = "" if extra_overhead == 0 else f"encode:{signed_str(extra_overhead)}"
        print(
            f"[genetic_algo]   snapshot: {output_path} => {len(raw_compressed)} bytes, final: {len(res)} bytes ({message})",
            file=sys.stderr,
        )

        snapshot_warning_emitted = False
        return bit_length, entry.raw_compressed

    stop_event = threading.Event()

    def snapshot_loop() -> None:
        while not stop_event.wait(snapshot_interval_sec):
            snapshot_once()

    process = subprocess.Popen(  # pylint: disable=consider-using-with
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(binary_path.parent),
    )

    watcher = threading.Thread(target=snapshot_loop, daemon=True)
    watcher.start()

    try:
        stdout, stderr = process.communicate(timeout=timeout_sec)
        timed_out = False
        returncode = process.returncode
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        timed_out = True
        returncode = process.returncode
    finally:
        stop_event.set()
        watcher.join()

    final_snapshot = snapshot_once()

    if timed_out and not out_deflate_path.exists():
        return GAExecutionResult(
            optimized_bytes=None,
            bit_length=None,
            stdout=stdout,
            stderr=stderr,
            timed_out=True,
            returncode=returncode,
            workdir=str(work_dir),
            output_text="",
            error="geneticalgo timed out",
        )

    optimized_text = stdout
    if not optimized_text.strip() and out_deflate_path.exists():
        optimized_text = out_deflate_path.read_text(encoding="utf-8")

    optimized_text = optimized_text.strip()
    if not optimized_text:
        if final_snapshot:
            bit_length, optimized_bytes = final_snapshot
            return GAExecutionResult(
                optimized_bytes=optimized_bytes,
                bit_length=bit_length,
                stdout=stdout,
                stderr=stderr,
                timed_out=timed_out,
                returncode=returncode,
                workdir=str(work_dir),
                output_text="",
            )
        return GAExecutionResult(
            optimized_bytes=None,
            bit_length=None,
            stdout=stdout,
            stderr=stderr,
            timed_out=timed_out,
            returncode=returncode,
            workdir=str(work_dir),
            output_text="",
            error="geneticalgo produced no output",
        )

    try:
        bit_length, optimized_bytes = load_deflate_stream(StringIO(optimized_text))
    except Exception as exc:  # pylint: disable=broad-except
        if final_snapshot:
            bit_length, optimized_bytes = final_snapshot
            return GAExecutionResult(
                optimized_bytes=optimized_bytes,
                bit_length=bit_length,
                stdout=stdout,
                stderr=stderr,
                timed_out=timed_out,
                returncode=returncode,
                workdir=str(work_dir),
                output_text=optimized_text,
                error=f"failed to parse GA output: {exc}",
            )
        return GAExecutionResult(
            optimized_bytes=None,
            bit_length=None,
            stdout=stdout,
            stderr=stderr,
            timed_out=timed_out,
            returncode=returncode,
            workdir=str(work_dir),
            output_text=optimized_text,
            error=f"failed to parse GA output: {exc}",
        )

    return GAExecutionResult(
        optimized_bytes=optimized_bytes,
        bit_length=bit_length,
        stdout=stdout,
        stderr=stderr,
        timed_out=timed_out,
        returncode=returncode,
        workdir=str(work_dir),
        output_text=optimized_text,
    )


def solve(
    task_dir: str,
    task_id: int,
    *,
    stripper_name: str,
    use_zopfli: bool = True,
    timeout_sec: Optional[int] = None,
) -> Dict[str, object]:
    repo_root = Path(__file__).resolve().parent
    source_path = _resolve_source(task_dir, task_id)
    source_code = source_path.read_text(encoding="utf-8")

    if stripper_name not in strippers:
        raise ValueError(f"Unknown stripper: {stripper_name}")

    stripper = strippers[stripper_name]

    try:
        stripped_code = stripper(source_code)
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "error": f"failed to apply stripper: {exc}",
            "stripper": stripper_name,
            "source_path": str(source_path),
        }

    try:
        deflate_bytes, deflate_text = _compress_code(
            stripped_code,
            use_zopfli=use_zopfli,
        )
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "error": f"compression failed: {exc}",
            "stripper": stripper_name,
            "source_path": str(source_path),
        }

    ga_binary = repo_root / "deflate_optimizer_cpp" / "geneticalgo"
    if not ga_binary.exists():
        raise FileNotFoundError(f"geneticalgo binary not found at {ga_binary}")

    cache_dir = repo_root / "optimizer_results" / "genetic_algo"
    cache_dir.mkdir(parents=True, exist_ok=True)
    work_dir = cache_dir / f"{task_dir}-{task_id}-{stripper_name}-{'zopfli' if use_zopfli else 'zlib'}"
    output_path = work_dir / "result.deflate"
    py_output_path = work_dir / f"task{task_id:03d}.py"

    variable_text = _build_variable_dump(stripped_code)

    print(f"[genetic_algo] running GA for {stripper_name} {'(zopfli)' if use_zopfli else '(zlib)' }...", file=sys.stderr)

    try:
        ga_exec = _run_genetic_algorithm(
            deflate_text,
            variable_text,
            binary_path=ga_binary,
            timeout_sec=timeout_sec,
            work_dir=work_dir,
            output_path=output_path,
            py_output_path=py_output_path,
        )
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "stripper": stripper_name,
            "source_path": str(source_path),
            "used_zopfli": use_zopfli,
            "initial_size": len(deflate_bytes),
            "error": str(exc),
            "traceback": traceback.format_exc(),
        }

    final_bytes = ga_exec.optimized_bytes or deflate_bytes
    final_bit_length = ga_exec.bit_length
    output_path.write_bytes(final_bytes)

    result = {
        "stripper": stripper_name,
        "source_path": str(source_path),
        "used_zopfli": use_zopfli,
        "initial_size": len(deflate_bytes),
        "final_bit_length": final_bit_length,
        "final_size": len(final_bytes),
        "timed_out": ga_exec.timed_out,
        "returncode": ga_exec.returncode,
        "ga_stdout_excerpt": _truncate(ga_exec.stdout),
        "ga_stderr": _truncate(ga_exec.stderr),
        "ga_error": ga_exec.error,
        "workdir": ga_exec.workdir,
        "output_path": str(output_path),
        "py_output_path": str(py_output_path),
        "viz_url": viz_deflate_url(final_bytes),
    }

    print(f"[genetic_algo] done for {stripper_name}", file=sys.stderr)
    print(f"[genetic_algo]   initial: {len(deflate_bytes)} bytes", file=sys.stderr)
    print(f"[genetic_algo]   final:   {len(final_bytes)} bytes", file=sys.stderr)
    print(f"[genetic_algo]   output:  {output_path}", file=sys.stderr)
    print(f"[genetic_algo]   viz:     {result['viz_url']}", file=sys.stderr)

    return result

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run genetic deflate optimizer over stripped sources.")
    parser.add_argument("task_dir", help="Task directory (e.g., base_yu)")
    parser.add_argument("task_id", type=int, help="Task ID (e.g., 151)")
    parser.add_argument(
        "--stripper",
        choices=sorted(strippers.keys()),
        help="Run only the specified stripper",
    )
    parser.add_argument(
        "--timeout",
        dest="timeout_sec",
        type=int,
        default=None,
        help="Timeout in seconds for the GA binary (omit for no timeout)",
    )
    parser.add_argument(
        "--use-zlib",
        dest="use_zopfli",
        action="store_false",
        help="Use zlib instead of zopfli for initial compression",
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Skip slow optimizations in cached_zopfli_ours2",
    )
    parser.add_argument(
        "--list-strippers",
        action="store_true",
        help="List available stripper names and exit",
    )

    args = parser.parse_args(argv)

    if args.list_strippers:
        for name in sorted(strippers.keys()):
            print(name)
        return 0

    timeout_sec: Optional[int] = args.timeout_sec
    if timeout_sec is not None and timeout_sec <= 0:
        timeout_sec = None

    common_kwargs = {
        "task_dir": args.task_dir,
        "task_id": args.task_id,
        "timeout_sec": timeout_sec,
    }

    results: Dict[str, Dict[str, object]] = {}

    if args.stripper:
        results[args.stripper] = solve(
            stripper_name=args.stripper,
            use_zopfli=args.use_zopfli,
            **common_kwargs,
        )
    else:
        names = sorted(strippers.keys())
        max_workers = len(names) * 2
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(
                    solve,
                    stripper_name=name,
                    use_zopfli=use_zopfli,
                    **common_kwargs,
                ): name
                for name in names
                for use_zopfli in [True, False]
            }
            for future in as_completed(futures):
                name = futures[future]
                try:
                    results[name] = future.result()
                except Exception as exc:  # pylint: disable=broad-except
                    results[name] = {
                        "stripper": name,
                        "error": str(exc),
                        "traceback": traceback.format_exc(),
                    }

    best_result = min(
        (info for info in results.values() if "error" not in info),
        key=lambda x: x["final_size"],
        default=None,
    )

    best_length = best_result["final_size"] if best_result else None
    best_url = best_result["viz_url"] if best_result else None
    print("=== best result ===", file=sys.stderr)
    print(f"stripper: {best_result['stripper']}", file=sys.stderr)
    print(f"source:   {best_result['source_path']}", file=sys.stderr)
    print(f"workdir:   {best_result.get('workdir', 'N/A')}", file=sys.stderr)
    print(f"size:     {best_length} bytes", file=sys.stderr)
    print(f"viz:      {best_url}", file=sys.stderr)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

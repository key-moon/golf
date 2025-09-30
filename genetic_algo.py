import argparse
import sys
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
    timeout_sec: int,
    work_dir: Path,
) -> GAExecutionResult:
    work_dir.mkdir(parents=True, exist_ok=True)

    deflate_path = work_dir / "input_deflate.txt"
    variable_path = work_dir / "input_variable.txt"
    out_deflate_path = work_dir / "output_deflate.txt"
    out_variable_path = work_dir / "output_variable.txt"

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
    ]

    try:
        completed = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
            cwd=str(binary_path.parent),
        )
        timed_out = False
        stdout = completed.stdout
        stderr = completed.stderr
        returncode = completed.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        returncode = None

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
    timeout_sec: int = 300,
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

    cache_dir = repo_root / ".cache" / "genetic_algo"
    cache_dir.mkdir(parents=True, exist_ok=True)
    work_dir = cache_dir / f"{task_dir}-{task_id}-{stripper_name}-{'zopfli' if use_zopfli else 'zlib'}"

    variable_text = _build_variable_dump(stripped_code)

    print(f"[genetic_algo] running GA for {stripper_name} {'(zopfli)' if use_zopfli else '(zlib)' }...", file=sys.stderr)

    try:
        ga_exec = _run_genetic_algorithm(
            deflate_text,
            variable_text,
            binary_path=ga_binary,
            timeout_sec=timeout_sec,
            work_dir=work_dir,
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

    output_path = work_dir / "result.deflate"
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
        default=300,
        help="Timeout in seconds for the GA binary",
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

    common_kwargs = {
        "task_dir": args.task_dir,
        "task_id": args.task_id,
        "timeout_sec": args.timeout_sec,
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

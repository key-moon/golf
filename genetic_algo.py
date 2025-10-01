# 時間がかかるかわりに強いoptimizer
# optimizer_results/genetic_algo/ に途中状態や最終状態のdeflate fileを保存している
# プログラム改変後に再度走らせたい場合は current_states / input_deflate / input_variable を削除してから再実行で良い

import argparse
import os
import random
import sys
import threading
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, as_completed, wait
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Iterator, Optional, Sequence
import subprocess
import traceback

import zlib
import zopfli

from deflate_optimizer.dump_deflate_stream import dump_deflate_stream
from deflate_optimizer.load_deflate_text import load_deflate_stream
from deflate_optimizer.enumerate_variable_occurrences import list_var_occurrences
from deflate_optimizer.variable_conflict import build_conflict_report
from compress import get_embed_str, optimize_deflate_stream, determine_wbits, signed_str
from get_compression_candidates import CompressionCandidate, collect_compress_candidates
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


@dataclass(frozen=True)
class GAJob:
    task_id: int
    task_dir: str
    base_path: Path
    stripper: str

    def label(self) -> str:
        return f"{self.task_dir}/task{self.task_id:03d}:{self.stripper}"


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

    # 一度最適化した圧縮結果を覚えて再利用する
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

        extra_args = determine_wbits(compressed)
        prefix = (
            f"#coding:L1\nimport {lib_name}\nexec({lib_name}.decompress(bytes("
        ).encode()
        suffix = b",'L1')" + extra_args.encode() + b"))"
        embed = get_embed_str(compressed)
        extra_overhead = len(embed) - (len(compressed) + 2)
        res = prefix + embed + suffix

        output_path.write_bytes(compressed)

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
            f"[genetic_algo]   snapshot: {output_path} => {len(compressed)} bytes, final: {len(res)} bytes ({message})",
            file=sys.stderr,
        )

        snapshot_warning_emitted = False
        return bit_length, compressed

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
    source_override: Path | None = None,
) -> None:
    repo_root = Path(__file__).resolve().parent
    if source_override is not None:
        source_path = Path(source_override)
        if not source_path.is_absolute():
            source_path = (repo_root / source_path).resolve()
    else:
        source_path = _resolve_source(task_dir, task_id)
    source_code = source_path.read_text(encoding="utf-8")

    if stripper_name not in strippers:
        raise ValueError(f"Unknown stripper: {stripper_name}")

    stripper = strippers[stripper_name]

    try:
        stripped_code = stripper(source_code)
    except Exception as exc:  # pylint: disable=broad-except
        print(
            (
                f"[genetic_algo] error: failed to apply stripper {stripper_name} "
                f"for {source_path}: {exc}"
            ),
            file=sys.stderr,
        )
        return

    try:
        deflate_bytes, deflate_text = _compress_code(
            stripped_code,
            use_zopfli=use_zopfli,
        )
    except Exception as exc:  # pylint: disable=broad-except
        print(
            (
                f"[genetic_algo] error: compression failed for {stripper_name} "
                f"at {source_path}: {exc}"
            ),
            file=sys.stderr,
        )
        return

    ga_binary = repo_root / "deflate_optimizer_cpp" / "geneticalgo"
    if not ga_binary.exists():
        raise FileNotFoundError(f"geneticalgo binary not found at {ga_binary}")

    cache_dir = repo_root / "optimizer_results" / "genetic_algo"
    cache_dir.mkdir(parents=True, exist_ok=True)
    work_dir = cache_dir / f"{task_dir}-{task_id}-{stripper_name}-{'zopfli' if use_zopfli else 'zlib'}"
    output_path = work_dir / "result.deflate"
    py_output_path = work_dir / f"task{task_id:03d}.py"

    variable_text = _build_variable_dump(stripped_code)

    print(
        (
            f"[genetic_algo] running GA for task {task_id:03d} "
            f"{source_path} stripper={stripper_name} "
            f"{'(zopfli)' if use_zopfli else '(zlib)'}..."
        ),
        file=sys.stderr,
    )

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
        print(
            (
                f"[genetic_algo] error: GA execution failed for {stripper_name} "
                f"({'zopfli' if use_zopfli else 'zlib'}): {exc}"
            ),
            file=sys.stderr,
        )
        traceback.print_exc()
        return

    final_bytes = ga_exec.optimized_bytes or deflate_bytes
    final_bit_length = ga_exec.bit_length
    output_path.write_bytes(final_bytes)

    viz_url = viz_deflate_url(final_bytes)
    stdout_excerpt = _truncate(ga_exec.stdout)
    stderr_excerpt = _truncate(ga_exec.stderr)

    print(f"[genetic_algo] done for {stripper_name}", file=sys.stderr)
    print(f"[genetic_algo]   initial: {len(deflate_bytes)} bytes", file=sys.stderr)
    print(f"[genetic_algo]   final:   {len(final_bytes)} bytes", file=sys.stderr)
    if final_bit_length is not None:
        print(f"[genetic_algo]   bits:    {final_bit_length}", file=sys.stderr)
    print(f"[genetic_algo]   output:  {output_path}", file=sys.stderr)
    print(f"[genetic_algo]   py:      {py_output_path}", file=sys.stderr)
    print(f"[genetic_algo]   viz:     {viz_url}", file=sys.stderr)
    if ga_exec.timed_out:
        print("[genetic_algo]   note: GA timed out", file=sys.stderr)
    if ga_exec.returncode is not None:
        print(f"[genetic_algo]   returncode: {ga_exec.returncode}", file=sys.stderr)
    if ga_exec.error:
        print(f"[genetic_algo]   GA error: {ga_exec.error}", file=sys.stderr)
    # if stdout_excerpt:
    #     print(f"[genetic_algo]   stdout: {stdout_excerpt}", file=sys.stderr)
    # if stderr_excerpt:
    #     print(f"[genetic_algo]   stderr: {stderr_excerpt}", file=sys.stderr)



def _jobs_from_candidates(candidates: Sequence[CompressionCandidate]) -> list[GAJob]:
    jobs: list[GAJob] = []
    for cand in candidates:
        base_path = cand.base_path
        task_dir = base_path.parent.name
        for stripper in cand.strippers:
            jobs.append(
                GAJob(
                    task_id=cand.task_id,
                    task_dir=task_dir,
                    base_path=base_path,
                    stripper=stripper,
                )
            )
    return jobs


def _iter_shuffled_jobs(jobs: Sequence[GAJob]) -> Iterator[GAJob]:
    job_list = list(jobs)
    if not job_list:
        return
    while True:
        random.shuffle(job_list)
        for job in job_list:
            yield job


def _submit_job(
    executor: ThreadPoolExecutor,
    job_iter: Iterator[GAJob],
    timeout_sec: int,
):
    job = next(job_iter)
    future = executor.submit(
        solve,
        job.task_dir,
        job.task_id,
        stripper_name=job.stripper,
        timeout_sec=timeout_sec,
        source_override=job.base_path,
    )
    return future, job


def _run_candidate_autopilot(
    *,
    timeout_sec: int,
    max_workers: Optional[int] = None,
    shuffle_seed: Optional[int] = None,
) -> int:
    if shuffle_seed is not None:
        random.seed(shuffle_seed)

    candidates = collect_compress_candidates()
    print(f"[genetic_algo] autopilot: found {len(candidates)} compression candidates", file=sys.stderr)
    jobs = _jobs_from_candidates(candidates)

    if not jobs:
        print("[genetic_algo] autopilot: no compression candidates found", file=sys.stderr)
        return 1

    desired_workers = max_workers if max_workers is not None else os.cpu_count() or 1
    worker_count = max(1, min(desired_workers, len(jobs)))
    job_iter = _iter_shuffled_jobs(jobs)
    if job_iter is None:
        print("[genetic_algo] autopilot: job iterator unavailable", file=sys.stderr)
        return 1

    print(
        (
            f"[genetic_algo] autopilot: {len(jobs)} job/stripper combos, "
            f"workers={worker_count}, timeout={timeout_sec}s"
        ),
        file=sys.stderr,
    )
    print("[genetic_algo] autopilot: press Ctrl+C to stop", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        pending: dict[object, GAJob] = {}
        try:
            for _ in range(worker_count):
                future, job = _submit_job(executor, job_iter, timeout_sec)
                pending[future] = job

            while pending:
                done, _ = wait(list(pending.keys()), return_when=FIRST_COMPLETED)
                for future in done:
                    job = pending.pop(future, None)
                    if job is None:
                        continue
                    try:
                        future.result()
                    except Exception as exc:  # pylint: disable=broad-except
                        print(
                            f"[genetic_algo] autopilot error for {job.label()}: {exc}",
                            file=sys.stderr,
                        )
                    future_next, job_next = _submit_job(executor, job_iter, timeout_sec)
                    pending[future_next] = job_next
        except KeyboardInterrupt:
            print("[genetic_algo] autopilot interrupted; cancelling pending jobs", file=sys.stderr)
            for future in pending:
                future.cancel()

    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run genetic deflate optimizer over stripped sources.")
    parser.add_argument("task_dir", nargs="?", help="Task directory (e.g., base_yu)")
    parser.add_argument("task_id", nargs="?", type=int, help="Task ID (e.g., 151)")
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
        help="Timeout in seconds for the GA binary (omit or <=0 for no timeout)",
    )
    parser.add_argument(
        "--use-zlib",
        dest="use_zopfli",
        action="store_false",
        help="Use zlib instead of zopfli for initial compression",
    )
    parser.add_argument(
        "--list-strippers",
        action="store_true",
        help="List available stripper names and exit",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=None,
        help="(autopilot) maximum number of concurrent GA runs",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="(autopilot) random seed for shuffling candidate order",
    )

    args = parser.parse_args(argv)

    if args.list_strippers:
        for name in sorted(strippers.keys()):
            print(name)
        return 0

    if args.task_dir is None and args.task_id is None:
        timeout = args.timeout_sec if args.timeout_sec and args.timeout_sec > 0 else 1200
        print('[genetic_algo] running in autopilot mode', file=sys.stderr)
        if args.use_zopfli is False:
            print("[genetic_algo] warning: --use-zlib is ignored in autopilot mode", file=sys.stderr)
        return _run_candidate_autopilot(
            timeout_sec=timeout,
            max_workers=args.max_workers,
            shuffle_seed=args.seed,
        )

    if (args.task_dir is None) != (args.task_id is None):
        parser.error("task_dir and task_id must be provided together")

    if args.max_workers is not None:
        print("[genetic_algo] warning: --max-workers ignored when task is specified", file=sys.stderr)
    if args.seed is not None:
        print("[genetic_algo] warning: --seed ignored when task is specified", file=sys.stderr)

    timeout_sec: Optional[int] = args.timeout_sec
    if timeout_sec is not None and timeout_sec <= 0:
        timeout_sec = None

    common_kwargs = {
        "task_dir": args.task_dir,
        "task_id": args.task_id,
        "timeout_sec": timeout_sec,
    }

    if args.stripper:
        solve(
            stripper_name=args.stripper,
            use_zopfli=args.use_zopfli,
            **common_kwargs,
        )
        return 0

    names = sorted(strippers.keys())
    max_workers = len(names) * 2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                solve,
                stripper_name=name,
                use_zopfli=use_zopfli,
                **common_kwargs,
            ): (name, use_zopfli)
            for name in names
            for use_zopfli in [True, False]
        }
        for future in as_completed(futures):
            name, use_zopfli = futures[future]
            try:
                future.result()
            except Exception as exc:  # pylint: disable=broad-except
                print(
                    (
                        f"[genetic_algo] error: solve raised for {name} "
                        f"({'zopfli' if use_zopfli else 'zlib'}): {exc}"
                    ),
                    file=sys.stderr,
                )
                traceback.print_exc()
    return 0



if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

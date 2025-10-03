# 時間がかかるかわりに強いoptimizer
# optimizer_results/genetic_algo/ に途中状態や最終状態のdeflate fileを保存している
# プログラム改変後に再度走らせたい場合は current_states / input_deflate / input_variable を削除してから再実行で良い

import argparse
import os
import random
import re
import shutil
import sys
import threading
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, as_completed, wait
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Callable, Iterator, Optional, Sequence
import tempfile
import subprocess
import traceback

import zlib
import zopfli

from deflate_optimizer.dump_deflate_stream import dump_deflate_stream
from deflate_optimizer.load_deflate_text import load_deflate_stream
from deflate_optimizer.enumerate_variable_occurrences import list_var_occurrences
from deflate_optimizer.variable_conflict import build_conflict_report
from compress import get_embed_str, optimize_deflate_stream, determine_wbits, signed_str
from get_compression_candidates import CandidateEntry, CompressionCandidate, collect_compress_candidates
from strip import strippers
from utils import get_code_paths, viz_deflate_url

GA_OUTPUT_ROOT = Path("optimizer_results/genetic_algo")


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
    use_zopfli: bool

    def label(self) -> str:
        codec = "zopfli" if self.use_zopfli else "zlib"
        return f"{self.task_dir}/task{self.task_id:03d}:{self.stripper}:{codec}"


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


def _work_dir_for(
    task_dir: str,
    task_id: int,
    stripper_name: str,
    use_zopfli: bool,
) -> Path:
    repo_root = Path(__file__).resolve().parent
    cache_dir = repo_root / "optimizer_results" / "genetic_algo"
    codec = "zopfli" if use_zopfli else "zlib"
    return cache_dir / f"{task_dir}-{task_id}-{stripper_name}-{codec}"


def _matches_original_snapshot(
    *,
    task_dir: str,
    task_id: int,
    stripper_name: str,
    use_zopfli: bool,
    source_path: Path,
    snapshot_bytes: Optional[bytes] = None,
) -> tuple[bool, bytes]:
    source_path = Path(source_path)
    if not source_path.is_absolute():
        source_path = source_path.resolve()

    if snapshot_bytes is None:
        _, _, snapshot_bytes = _strip_source_for_snapshot(source_path)

    work_dir = _work_dir_for(task_dir, task_id, stripper_name, use_zopfli)
    original_snapshot_path = work_dir / f"task{task_id:03d}_original.py"

    try:
        if original_snapshot_path.exists() and original_snapshot_path.read_bytes() == snapshot_bytes:
            return True, snapshot_bytes
    except OSError:
        pass

    return False, snapshot_bytes


def _clear_ga_inputs(work_dir: Path) -> None:
    for name in ("input_deflate.txt", "input_variable.txt", "current_states.txt"):
        try:
            (work_dir / name).unlink()
        except FileNotFoundError:
            continue


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


def _build_python_payload(
    compressed: bytes,
    *,
    lib_name: str = "zlib",
) -> tuple[bytes, int]:
    extra_args = determine_wbits(compressed)
    prefix = (
        f"#coding:L1\nimport {lib_name}\nexec({lib_name}.decompress(bytes("
    ).encode()
    suffix = b",'L1')" + extra_args.encode() + b"))"
    embed = get_embed_str(compressed)
    payload = prefix + embed + suffix
    extra_overhead = len(embed) - (len(compressed) + 2)
    return payload, extra_overhead


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as tmp_file:
            tmp_file.write(data)
            tmp_file.flush()
            os.fsync(tmp_file.fileno())
        os.replace(tmp_path, path)
    finally:
        try:
            os.remove(tmp_path)
        except FileNotFoundError:
            pass


def _atomic_write_text(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    _atomic_write_bytes(path, text.encode(encoding))


class _StableTextMonitor:
    def __init__(
        self,
        source: Path,
        *,
        dest: Optional[Path] = None,
        normalizer: Optional[Callable[[str], str]] = None,
    ) -> None:
        self.source = source
        self.dest = dest
        self.normalizer = normalizer or (lambda text: text)
        self._last_value: Optional[str] = None
        self._last_written: Optional[str] = None

    def check(self) -> Optional[str]:
        try:
            raw_text = self.source.read_text(encoding="utf-8")
        except OSError:
            self._last_value = None
            self._last_written = None
            return None

        normalized = self.normalizer(raw_text)
        if not normalized:
            self._last_value = normalized
            self._last_written = None
            return None

        if normalized == self._last_value:
            if self.dest is not None and normalized != self._last_written:
                _atomic_write_text(self.dest, raw_text, encoding="utf-8")
                self._last_written = normalized
            return normalized

        self._last_value = normalized
        self._last_written = None
        return None

def _load_deflate_snapshot(
    deflate_path: Path,
    *,
    retries: int = 3,
    delay_sec: float = 0.05,
) -> Optional[tuple[int, bytes]]:
    last_exc: Optional[Exception] = None
    for attempt in range(retries):
        try:
            text = deflate_path.read_text(encoding="utf-8").strip()
        except OSError as exc:
            last_exc = exc
            if attempt + 1 < retries:
                time.sleep(delay_sec)
                continue
            raise exc
        if not text:
            return None

        try:
            return load_deflate_stream(StringIO(text))
        except Exception as exc:  # pylint: disable=broad-except
            last_exc = exc
            if attempt + 1 < retries:
                time.sleep(delay_sec)
                continue
    if last_exc is not None:
        raise last_exc
    return None


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

    out_deflate_tmp = work_dir / "output_deflate.txt~tmp"
    out_variable_tmp = work_dir / "output_variable.txt~tmp"
    states_tmp = work_dir / "current_states.txt~tmp"

    _atomic_write_text(deflate_path, deflate_text, encoding="utf-8")
    _atomic_write_text(variable_path, variable_text, encoding="utf-8")

    for path in (out_deflate_tmp, out_variable_tmp, states_tmp):
        try:
            path.unlink()
        except FileNotFoundError:
            pass

    if states_path.exists():
        try:
            _atomic_write_text(states_tmp, states_path.read_text(encoding="utf-8"), encoding="utf-8")
        except OSError:
            pass

    cmd = [
        str(binary_path),
        str(deflate_path),
        str(variable_path),
        str(out_deflate_tmp),
        str(out_variable_tmp),
        str(states_tmp),
    ]

    deflate_monitor = _StableTextMonitor(out_deflate_tmp)
    variable_monitor = _StableTextMonitor(out_variable_tmp, dest=out_variable_path)
    states_monitor = _StableTextMonitor(states_tmp, dest=states_path)

    # 一度最適化した圧縮結果を覚えて再利用する
    snapshot_warning_emitted = False
    last_deflate_written: Optional[str] = None

    py_output_best_len: Optional[int] = None
    try:
        py_output_best_len = py_output_path.stat().st_size
    except FileNotFoundError:
        py_output_best_len = None
    except OSError:
        py_output_best_len = None

    lib_name = "zlib"

    def snapshot_once() -> Optional[tuple[int, bytes]]:
        nonlocal snapshot_warning_emitted, py_output_best_len, last_deflate_written
        variable_monitor.check()
        states_monitor.check()

        stable_deflate_text = deflate_monitor.check()
        if stable_deflate_text is None:
            return None

        normalized_deflate = stable_deflate_text.strip()
        if not normalized_deflate:
            return None

        try:
            bit_length, compressed = load_deflate_stream(StringIO(normalized_deflate))
        except Exception as exc:  # pylint: disable=broad-except
            if not snapshot_warning_emitted:
                print(
                    (
                        "[genetic_algo] warning: failed to parse in-progress GA output; "
                        f"will retry on next snapshot ({exc})"
                    ),
                    file=sys.stderr,
                )
                snapshot_warning_emitted = True
            return None

        snapshot_warning_emitted = False

        if normalized_deflate != last_deflate_written:
            _atomic_write_text(out_deflate_path, normalized_deflate, encoding="utf-8")
            last_deflate_written = normalized_deflate

        res, extra_overhead = _build_python_payload(compressed, lib_name=lib_name)

        _atomic_write_bytes(output_path, compressed)

        current_best = py_output_best_len
        if current_best is None:
            try:
                current_best = py_output_path.stat().st_size
            except FileNotFoundError:
                current_best = None
            except OSError:
                current_best = None
        if current_best is None or len(res) < current_best:
            _atomic_write_bytes(py_output_path, res)
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

    for src, dst in (
        (out_deflate_path, out_deflate_tmp),
        (out_variable_path, out_variable_tmp),
        (states_path, states_tmp),
    ):
        if not src.exists():
            continue
        try:
            shutil.copyfile(src, dst)
        except OSError:
            pass

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


def _strip_source_for_snapshot(source_path: Path) -> tuple[str, str, bytes]:
    raw_code = source_path.read_text(encoding="utf-8")
    strip_fn = strippers.get("forplain", next(iter(strippers.values())))
    try:
        stripped = strip_fn(raw_code)
    except Exception:
        stripped = raw_code
    if isinstance(stripped, bytes):
        stripped_bytes = stripped
        stripped_text = stripped.decode("utf-8", errors="replace")
    else:
        stripped_text = stripped
        stripped_bytes = stripped_text.encode("utf-8")
    return raw_code, stripped_text, stripped_bytes


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
    raw_source_code, stripped_snapshot, snapshot_bytes = _strip_source_for_snapshot(source_path)
    source_code = raw_source_code
    source_bytes = raw_source_code.encode("utf-8")

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

    work_dir = _work_dir_for(task_dir, task_id, stripper_name, use_zopfli)
    work_dir.parent.mkdir(parents=True, exist_ok=True)
    output_path = work_dir / "result.deflate"
    py_output_path = work_dir / f"task{task_id:03d}.py"

    work_dir.mkdir(parents=True, exist_ok=True)
    original_snapshot_path = work_dir / f"task{task_id:03d}_original.py"
    try:
        _atomic_write_bytes(original_snapshot_path, snapshot_bytes)
    except OSError:
        try:
            _atomic_write_text(original_snapshot_path, stripped_snapshot, encoding="utf-8")
        except OSError:
            pass

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
    _atomic_write_bytes(output_path, final_bytes)

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
        if stdout_excerpt:
            print(f"[genetic_algo]   stdout: {stdout_excerpt}", file=sys.stderr)
        if stderr_excerpt:
            print(f"[genetic_algo]   stderr: {stderr_excerpt}", file=sys.stderr)



def _jobs_from_candidates(
    candidates: Sequence[CompressionCandidate],
    *,
    skip_if_unchanged: bool,
) -> list[GAJob]:
    jobs: list[GAJob] = []
    for cand in candidates:
        for entry in cand.entries:
            base_path = entry.base_path
            task_dir = base_path.parent.name
            snapshot_bytes: Optional[bytes] = None
            for stripper in entry.strippers:
                for use_zopfli in (True, False):
                    matches, snapshot_bytes = _matches_original_snapshot(
                        task_dir=task_dir,
                        task_id=cand.task_id,
                        stripper_name=stripper,
                        use_zopfli=use_zopfli,
                        source_path=base_path,
                        snapshot_bytes=snapshot_bytes,
                    )
                    codec = "zopfli" if use_zopfli else "zlib"
                    label = f"{task_dir}/task{cand.task_id:03d}:{stripper}:{codec}"
                    if matches:
                        print(
                            f"[genetic_algo] {label} snapshot matches current source",
                            file=sys.stderr,
                        )
                        if skip_if_unchanged:
                            print(
                                f"[genetic_algo] skip {label}: source unchanged from snapshot",
                                file=sys.stderr,
                            )
                            continue
                    else:
                        print(
                            f"[genetic_algo] {label} snapshot differs; resetting GA inputs",
                            file=sys.stderr,
                        )
                        _clear_ga_inputs(
                            _work_dir_for(task_dir, cand.task_id, stripper, use_zopfli)
                        )
                    jobs.append(
                        GAJob(
                            task_id=cand.task_id,
                            task_dir=task_dir,
                            base_path=base_path,
                            stripper=stripper,
                            use_zopfli=use_zopfli,
                        )
                    )
    return jobs


def _iter_shuffled_jobs(jobs: Sequence[GAJob], shuffle) -> Iterator[GAJob]:
    job_list = list(jobs)
    if not job_list:
        return
    while True:
        if shuffle:
            random.shuffle(job_list)
        for job in job_list:
            yield job


def _load_original_code_from_deflate(deflate_path: Path) -> bytes | None:
    try:
        text = deflate_path.read_text(encoding="utf-8")
    except OSError:
        return None
    try:
        _, deflate = load_deflate_stream(StringIO(text))
    except Exception:  # pylint: disable=broad-except
        return None

    raw: bytes | None = None
    for wbits in (-15, -9, 15):
        try:
            raw = zlib.decompress(deflate, wbits)
            break
        except Exception:  # pylint: disable=broad-except
            continue
    if raw is None:
        try:
            raw = zlib.decompress(deflate)
        except Exception:  # pylint: disable=broad-except
            return None
    strip_fn = strippers.get("forplain", next(iter(strippers.values())))
    try:
        stripped = strip_fn(raw.decode("utf-8"))
        return stripped if isinstance(stripped, bytes) else stripped.encode("utf-8")
    except Exception:  # pylint: disable=broad-except
        return raw


def copy_original_codes() -> int:
    if not GA_OUTPUT_ROOT.exists():
        return 0

    created = 0
    for deflate_path in GA_OUTPUT_ROOT.rglob("input_deflate.txt"):
        work_dir = deflate_path.parent
        code_bytes = _load_original_code_from_deflate(deflate_path)
        if code_bytes is None:
            continue
        scripts = sorted(
            p for p in work_dir.glob("task*.py") if "_original" not in p.name
        )
        for script_path in scripts:
            match = re.search(r"task(\d{3})\.py$", script_path.name)
            if not match:
                continue
            original_path = work_dir / f"task{match.group(1)}_original.py"
            try:
                _atomic_write_bytes(original_path, code_bytes)
            except OSError:
                continue
            created += 1
    return created


def refresh_outputs_from_existing(
    *,
    task_dir: Optional[str],
    task_id: Optional[int],
) -> int:
    if not GA_OUTPUT_ROOT.exists():
        return 0

    if task_dir is not None and task_id is not None:
        pattern = f"{task_dir}-{task_id:03d}-*/output_deflate.txt"
        candidates = GA_OUTPUT_ROOT.glob(pattern)
    else:
        candidates = GA_OUTPUT_ROOT.glob("*/output_deflate.txt")

    refreshed = 0
    for output_deflate_path in sorted(candidates):
        work_dir = output_deflate_path.parent
        try:
            snapshot = _load_deflate_snapshot(output_deflate_path)
        except Exception as exc:  # pylint: disable=broad-except
            print(
                f"[genetic_algo] warning: failed to parse {output_deflate_path}: {exc}",
                file=sys.stderr,
            )
            continue
        if snapshot is None:
            print(
                f"[genetic_algo] warning: {output_deflate_path} has no data; skipping",
                file=sys.stderr,
            )
            continue
        bit_length, compressed = snapshot

        result_path = work_dir / "result.deflate"
        try:
            _atomic_write_bytes(result_path, compressed)
        except OSError as exc:
            print(
                f"[genetic_algo] warning: failed to write {result_path}: {exc}",
                file=sys.stderr,
            )
            continue

        payload, extra_overhead = _build_python_payload(compressed)
        scripts = sorted(
            p for p in work_dir.glob("task*.py") if "_original" not in p.name
        )
        if not scripts:
            inferred = None
            if task_dir is not None and task_id is not None:
                inferred = work_dir / f"task{task_id:03d}.py"
            else:
                match = re.search(r"-(\d+)-", work_dir.name)
                if match:
                    inferred = work_dir / f"task{int(match.group(1)) :03d}.py"
            if inferred is not None:
                scripts = [inferred]

        for script_path in scripts:
            try:
                _atomic_write_bytes(script_path, payload)
            except OSError as exc:
                print(
                    f"[genetic_algo] warning: failed to write {script_path}: {exc}",
                    file=sys.stderr,
                )

        message = "" if extra_overhead == 0 else f" encode:{signed_str(extra_overhead)}"
        print(
            (
                f"[genetic_algo] refreshed {work_dir}: {len(compressed)} bytes, "
                f"bits={bit_length}{message}"
            ),
            file=sys.stderr,
        )
        refreshed += 1

    return refreshed


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
        use_zopfli=job.use_zopfli,
        timeout_sec=timeout_sec,
        source_override=job.base_path,
    )
    return future, job


def _run_candidate_autopilot(
    *,
    timeout_sec: int,
    max_workers: Optional[int] = None,
    shuffle_seed: Optional[int] = None,
    skip_if_unchanged: bool,
) -> int:
    if shuffle_seed is not None:
        random.seed(shuffle_seed)

    candidates = collect_compress_candidates()
    total_entries = sum(len(c.entries) for c in candidates)
    print(
        (
            f"[genetic_algo] autopilot: found {len(candidates)} tasks "
            f"({total_entries} base entries)"
        ),
        file=sys.stderr,
    )
    jobs = _jobs_from_candidates(candidates, skip_if_unchanged=skip_if_unchanged)

    if not jobs:
        print("[genetic_algo] autopilot: no compression candidates found", file=sys.stderr)
        return 1

    desired_workers = max_workers if max_workers is not None else os.cpu_count() or 1
    worker_count = max(1, min(desired_workers, len(jobs)))
    job_iter = _iter_shuffled_jobs(jobs, shuffle=shuffle_seed != -1)
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
                future, job = _submit_job(
                    executor,
                    job_iter,
                    timeout_sec,
                )
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
                    future_next, job_next = _submit_job(
                        executor,
                        job_iter,
                        timeout_sec,
                    )
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
        help="(autopilot) random seed for shuffling candidate order. If seed=-1, shuffle is disabled.",
    )
    parser.add_argument(
        "--skip-unchanged",
        action="store_true",
        help="Skip GA runs when the original snapshot matches the current source",
    )
    # _original.py の再生成（ゴミが残っていた場合に使う）
    # 更新可否判定は _original.py の diff で判定するので、これを適当に動かすと --skip-unchanged が全部スキップ判定になる
    parser.add_argument(
        "--copy-original-codes",
        action="store_true",
        help="Populate *_original.py snapshots under optimizer_results/genetic_algo and exit",
    )
    # 成果物の再生成、途中でバグってるコードが混入したときとかに使うかも
    parser.add_argument(
        "--refresh-from-output",
        action="store_true",
        help=(
            "Update result.deflate and task*.py from existing output_deflate.txt files "
            "under optimizer_results/genetic_algo"
        ),
    )

    args = parser.parse_args(argv)

    if args.copy_original_codes:
        created = copy_original_codes()
        print(f"[genetic_algo] copied {created} original snapshots")
        return 0

    if args.refresh_from_output:
        if (args.task_dir is None) != (args.task_id is None):
            parser.error("task_dir and task_id must be provided together when using --refresh-from-output")
        refreshed = refresh_outputs_from_existing(
            task_dir=args.task_dir,
            task_id=args.task_id,
        )
        print(f"[genetic_algo] refreshed {refreshed} GA work directories")
        return 0

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
            skip_if_unchanged=args.skip_unchanged,
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

    assert args.task_dir is not None
    assert args.task_id is not None

    source_path = _resolve_source(args.task_dir, args.task_id)
    if not source_path.is_absolute():
        source_path = source_path.resolve()

    common_kwargs = {
        "task_dir": args.task_dir,
        "task_id": args.task_id,
        "timeout_sec": timeout_sec,
        "source_override": source_path,
    }

    snapshot_bytes_cache: Optional[bytes] = None

    def should_run(stripper_name: str, use_zopfli: bool) -> bool:
        nonlocal snapshot_bytes_cache
        matches, snapshot_bytes_cache = _matches_original_snapshot(
            task_dir=args.task_dir,
            task_id=args.task_id,
            stripper_name=stripper_name,
            use_zopfli=use_zopfli,
            source_path=source_path,
            snapshot_bytes=snapshot_bytes_cache,
        )
        codec = "zopfli" if use_zopfli else "zlib"
        label = f"{args.task_dir}/task{args.task_id:03d}:{stripper_name}:{codec}"
        if matches:
            print(
                f"[genetic_algo] {label} snapshot matches current source",
                file=sys.stderr,
            )
            if args.skip_unchanged:
                print(
                    f"[genetic_algo] skip {label}: source unchanged from snapshot",
                    file=sys.stderr,
                )
                return False
            return True

        print(
            f"[genetic_algo] {label} snapshot differs; resetting GA inputs",
            file=sys.stderr,
        )
        _clear_ga_inputs(_work_dir_for(args.task_dir, args.task_id, stripper_name, use_zopfli))
        return True

    if args.stripper:
        if should_run(args.stripper, args.use_zopfli):
            solve(
                stripper_name=args.stripper,
                use_zopfli=args.use_zopfli,
                **common_kwargs,
            )
        return 0

    names = sorted(strippers.keys())
    combos = [
        (name, use_zopfli)
        for name in names
        for use_zopfli in (True, False)
        if should_run(name, use_zopfli)
    ]

    if not combos:
        return 0

    max_workers = len(names) * 2 if names else 1
    worker_count = max(1, min(max_workers, len(combos)))
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = {
            executor.submit(
                solve,
                stripper_name=name,
                use_zopfli=use_zopfli,
                **common_kwargs,
            ): (name, use_zopfli)
            for name, use_zopfli in combos
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

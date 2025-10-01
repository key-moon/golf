"""Utilities for discovering genetic algorithm compression targets.

This module gathers base solution files whose stripped/minified form, after
zopfli compression, is competitive with the best option for each task.  It is
primarily used to feed the genetic deflate optimizer with promising
candidates.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from compress import cached_zopfli, determine_wbits, get_embed_str
from strip import strippers as default_strippers
from utils import get_code_paths

_TASK_ID_RE = re.compile(r"task(\d+)", re.IGNORECASE)
_PREFIX = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes("
_SUFFIX_PREFIX = b",'L1')"


@dataclass(frozen=True, slots=True)
class CompressionCandidate:
    """Represents the best base source for a compressed task."""

    task_id: int
    dist_path: Path
    base_path: Path
    strippers: list[str]
    best_length: int
    lengths: dict[str, int]

    def as_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "dist_path": str(self.dist_path),
            "base_path": str(self.base_path),
            "strippers": list(self.strippers),
            "best_length": self.best_length,
            "lengths": dict(self.lengths),
        }


def _task_id_from_path(path: Path) -> int | None:
    match = _TASK_ID_RE.search(path.stem)
    if not match:
        return None
    try:
        return int(match.group(1))
    except ValueError:
        return None


def _looks_like_zlib_encoded_task(path: Path, *, read_size: int = 512) -> bool:
    try:
        head = path.read_bytes()[:read_size]
    except OSError:
        return False
    return (
        b"#coding:L1" in head
        and b"import zlib" in head
        and b"zlib.decompress" in head
    )


def _iter_base_paths(base_glob: str, task_id: int) -> Iterable[Path]:
    for path_str in sorted(get_code_paths(base_glob, task_id)):
        path = Path(path_str)
        if path.suffix != ".py":
            continue
        yield path


def _compressed_length(source: str | bytes, *, fast_zopfli: bool) -> int:
    if isinstance(source, str):
        source_bytes = source.encode("utf-8")
    else:
        source_bytes = source
    deflate = cached_zopfli(source_bytes, fast=fast_zopfli)
    embed = get_embed_str(deflate)
    suffix = _SUFFIX_PREFIX + determine_wbits(deflate).encode() + b"))"
    return len(_PREFIX) + len(embed) + len(suffix)


def _compute_stripper_lengths(
    source_bytes: bytes,
    strippers_map: Mapping[str, object],
    *,
    fast_zopfli: bool,
) -> dict[str, int]:
    lengths: dict[str, int] = {}
    for name, strip_fun in strippers_map.items():
        try:
            stripped = strip_fun(source_bytes)
        except Exception:
            continue
        try:
            length = _compressed_length(stripped, fast_zopfli=fast_zopfli)
        except Exception:
            continue
        lengths[name] = length
    return lengths


def _best_candidate_for_task(
    *,
    task_id: int,
    dist_path: Path,
    base_glob: str,
    strippers_map: Mapping[str, object],
    max_extra: int,
    fast_zopfli: bool,
) -> CompressionCandidate | None:
    best_candidate: CompressionCandidate | None = None
    best_length: int | None = None

    for base_path in _iter_base_paths(base_glob, task_id):
        try:
            source_bytes = base_path.read_bytes()
        except OSError:
            continue

        lengths = _compute_stripper_lengths(
            source_bytes,
            strippers_map,
            fast_zopfli=fast_zopfli,
        )
        if not lengths:
            continue

        base_best = min(lengths.values())
        if best_length is not None and base_best >= best_length:
            continue

        selected = sorted(
            name for name, length in lengths.items() if length <= base_best + max_extra
        )
        if not selected:
            continue

        filtered_lengths = {name: lengths[name] for name in selected}
        best_candidate = CompressionCandidate(
            task_id=task_id,
            dist_path=dist_path,
            base_path=base_path,
            strippers=selected,
            best_length=base_best,
            lengths=filtered_lengths,
        )
        best_length = base_best

    return best_candidate


def collect_compress_candidates(
    *,
    dist_dir: str | Path = "dist",
    base_glob: str = "base_*",
    strippers_map: Mapping[str, object] | None = None,
    max_extra: int = 5,
    fast_zopfli: bool = True,
) -> list[CompressionCandidate]:
    dist_path = Path(dist_dir)
    strip_map: Mapping[str, object] = strippers_map or default_strippers

    candidates: list[CompressionCandidate] = []
    for dist_file in sorted(dist_path.glob("task*.py")):
        if not _looks_like_zlib_encoded_task(dist_file):
            continue
        task_id = _task_id_from_path(dist_file)
        if task_id is None:
            continue
        candidate = _best_candidate_for_task(
            task_id=task_id,
            dist_path=dist_file,
            base_glob=base_glob,
            strippers_map=strip_map,
            max_extra=max_extra,
            fast_zopfli=fast_zopfli,
        )
        if candidate is not None:
            candidates.append(candidate)
    return candidates


def _format_plain(candidates: Sequence[CompressionCandidate]) -> str:
    lines: list[str] = []
    for cand in candidates:
        parts = ", ".join(
            f"{name}({cand.lengths.get(name, cand.best_length)})" for name in cand.strippers
        )
        lines.append(
            f"{cand.task_id:03d} {cand.base_path} -> len={cand.best_length} :: [{parts}]"
        )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="List base files suitable for genetic_algo compression runs.",
    )
    parser.add_argument("--dist-dir", default="dist", help="Directory containing task outputs (default: dist)")
    parser.add_argument("--base-glob", default="base_*", help="Glob pattern for base solutions (default: base_*)")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of plain text.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output.",
    )
    parser.add_argument(
        "--delta",
        type=int,
        default=5,
        help="Include strip options within this many bytes of the best (default: 5)",
    )
    parser.add_argument(
        "--slow-zopfli",
        action="store_true",
        help="Use the slower, fully optimised zopfli pipeline",
    )

    args = parser.parse_args(argv)

    candidates = collect_compress_candidates(
        dist_dir=args.dist_dir,
        base_glob=args.base_glob,
        max_extra=args.delta,
        fast_zopfli=not args.slow_zopfli,
    )

    if args.json:
        indent = 2 if args.pretty else None
        print(json.dumps([cand.as_dict() for cand in candidates], indent=indent))
    else:
        print(_format_plain(candidates))

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

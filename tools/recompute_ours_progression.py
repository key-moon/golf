#!/usr/bin/env python3
"""
Recompute ours' task score progressions from git history and save to data/task_score_progressions.

For each dist/taskNNN.py, we traverse git history (following renames) and record
(length in bytes) changes with commit timestamps.

Usage:
  python tools/recompute_ours_progression.py [--name ours]

Notes:
- Only appends an entry when the length changes.
- If a file doesn't exist in a commit, it's skipped for that commit.
- Final result overwrites the existing ours file.
"""
from __future__ import annotations
import subprocess
import sys
import os
import datetime as dt
from typing import Optional

from tqdm import tqdm

# Repo root (two levels up from this file)
REPO_ROOT = os.path.dirname(os.path.dirname(__file__))


def run_git(cmd: list[str], cwd: Optional[str] = None, text=True) -> subprocess.CompletedProcess:
  return subprocess.run(cmd, cwd=cwd or REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=text)


def get_commits_for_path(path: str) -> list[tuple[str, int]]:
  """Return list of (commit_hash, unix_ts) for the given file path, oldest first."""
  # --follow to track renames, --diff-filter=AMDR to include add/move/delete/rename
  proc = run_git(["git", "log", "--follow", "--format=%H;%ct", "--", path])
  if proc.returncode != 0:
    return []
  lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
  items: list[tuple[str, int]] = []
  for line in lines:
    if ";" not in line:
      continue
    h, ts = line.split(";", 1)
    try:
      items.append((h, int(ts)))
    except ValueError:
      continue
  # git log returns newest first; reverse to oldest first
  items.reverse()
  return items


def get_file_size_at_commit(path: str, commit: str) -> Optional[int]:
  """Return file size in bytes for path at commit, or None if file missing."""
  proc = run_git(["git", "show", f"{commit}:{path}"], text=False)
  if proc.returncode != 0:
    return None
  return len(proc.stdout)


def recompute(name: str = "ours") -> None:
  # Lazy import after adjusting sys.path to avoid top-level import ordering issues
  if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
  from public_data import init_empty_progressions, save_user_progressions  # type: ignore

  progressions = init_empty_progressions()

  for task_id in tqdm(range(1, 401)):
    rel_path = os.path.join("dist", f"task{task_id:03}.py")
    commits = get_commits_for_path(rel_path)
    history = progressions[task_id - 1]
    last_size: Optional[int] = None if len(history) == 0 else history[-1]["score"]  # type: ignore[index]

    for commit, ts in commits:
      size = get_file_size_at_commit(rel_path, commit)
      if size is None:
        continue
      if last_size == size:
        continue
      history.append({
        "date": dt.datetime.utcfromtimestamp(ts),
        "score": size,
      })
      last_size = size

    progressions[task_id - 1] = history

  save_user_progressions(name, progressions)
  print(f"[+] Recomputed and saved progressions for '{name}'.")


if __name__ == "__main__":
  name = "ours"
  if len(sys.argv) > 1 and sys.argv[1] in ("-n", "--name") and len(sys.argv) > 2:
    name = sys.argv[2]
  recompute(name)

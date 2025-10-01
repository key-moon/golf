import dataclasses
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Callable
import json
import hashlib
from dataclasses import dataclass

from tqdm import tqdm

from checker import check, CheckRes
import compress
from dataclass_wizard import JSONWizard
from public_data import TaskSubmissionWithName, get_scores_per_task, record_ours_task_score_progression, _PAT_BEST, _PAT_EQ
from strip import strippers
from utils import get_code_paths, get_task

GA_OUTPUT_ROOT = Path("optimizer_results/genetic_algo")
GA_DIR_PATTERN = re.compile(r"^(?P<base>.+)-(?P<task>\d+)-(?P<stripper>.+)-(?P<method>zopfli|zlib)$")

def check_str(task_id: int, code: str | bytes, task, checked_hash):
  digest = hashlib.sha256(code.encode() if isinstance(code, str) else code).hexdigest()
  tmp_path = f"tmp/{digest}{task_id:03d}.py"
  code_hash = f"{task_id:03d}|{digest}"
  if code_hash in checked_hash:
    return CheckRes(**{"outputs": [], **checked_hash[code_hash]})
  if isinstance(code, str):
    open(tmp_path, "w").write(code)
  if isinstance(code, bytes):
    open(tmp_path, "wb").write(code)
  res = check(tmp_path, task, resume_tqdm=False)
  checked_hash[code_hash] = dataclasses.asdict(res)
  del checked_hash[code_hash]["outputs"]
  if f"tmp.{digest}{task_id:03d}" in sys.modules:
    del sys.modules[f"tmp.{digest}{task_id:03d}"]
  if os.path.exists(tmp_path):
    os.remove(tmp_path)
  return res

@dataclass
class TaskResult(JSONWizard):
  task: int
  success: bool
  message: str = ""
  base_path: str | None = None
  compressor: str | None = None
  length: int | None = None

  @staticmethod
  def md_header():
    return "| Task | Base | Compressor | Length | Best | Goods | Message |\n" + \
           "|------|------|------------|--------|------|-------|---------|\n"

  def md_row(self, best_sub: TaskSubmissionWithName | None):
      def local_link(title, path):
        return f"[{title}](/{path})"

      task = f"{self.task:03}"
      base = local_link(self.base_path.split('/')[0], self.base_path) if self.base_path is not None else "-"
      checker = self.compressor if self.compressor else "-"

      length = local_link(self.length, f"dist/task{task}.py") if self.length is not None else "-"

      if self.length is not None and best_sub:
        best, best_person = best_sub["score"], best_sub["name"]
        diff = self.length - best
        best = f"{best} {'🟢' if diff < 0 else '🔴' if diff > 0 else ''}"
        length = f"{length} ({'+' if diff > 0 else ''}{diff})"
      else:
        best = str(best_sub["score"]) if best_sub else "-"

      return "| " +  " | ".join([
        local_link(task, f"vis/task{task}.png"),
        base,
        checker,
        length,
        best,
        local_link("vis-many", f"vis_many/task{task}.png"),
        self.message
      ]) + " |\n"

@dataclass
class RunResult(JSONWizard):
  score: int
  results: list[TaskResult]


def _collect_ga_results(task_id: int) -> list[tuple[Path, Path | None, str, str]]:
  if not GA_OUTPUT_ROOT.exists():
    return []
  pattern = f"task{task_id:03d}.py"
  results: list[tuple[Path, Path | None, str, str]] = []
  for candidate in GA_OUTPUT_ROOT.rglob(pattern):
    if not candidate.is_file():
      continue
    match = GA_DIR_PATTERN.match(candidate.parent.name)
    if not match:
      continue
    try:
      dir_task = int(match.group("task"))
    except ValueError:
      continue
    if dir_task != task_id:
      continue
    stripper = match.group("stripper")
    method = match.group("method")
    base_root = match.group("base")
    base_source = Path(f"{base_root}/task{task_id:03d}.py") if base_root else None
    results.append((candidate, base_source if base_source.exists() else None, stripper, method))
  return results


def handle_results(results: list[TaskResult]):
  success_tasks = [*filter(lambda x: x.success, results)]
  accepted = len(success_tasks)
  score = sum(2500 - res.length for res in success_tasks if res.length is not None)

  with open("dist/results.json", "w") as results_file:
    results_file.write(RunResult(score, results).to_json())

  print(f"accepted: {accepted}/400, {score=}")

  # Update ours progression snapshot from current dist files/lengths
  current_scores: dict[int, int | None] = {}
  for r in results:
    current_scores[r.task] = r.length if r.length is not None else None
  record_ours_task_score_progression(current_scores)

  others_bests = get_scores_per_task()

  def first_non_ours(entries: list[TaskSubmissionWithName]) -> TaskSubmissionWithName | None:
    for entry in entries:
      if entry["name"] != "ours":
        return entry
    return None

  others_best_entries = [first_non_ours(bests) for bests in others_bests]

  others_bests_sum = sum(
    max(1, 2500 - best["score"])
    for best in others_best_entries
    if best is not None
  )

  def best_score(entry: TaskSubmissionWithName | None, default: int | float) -> int | float:
    return entry["score"] if entry is not None else default

  def our_length(res: TaskResult) -> int:
    return res.length if res.length is not None else 999999

  results_with_best: list[tuple[TaskResult, TaskSubmissionWithName | None]] = list(zip(results, others_best_entries))

  other_mds: list[tuple[str, str, Callable[[tuple[TaskResult, TaskSubmissionWithName | None]], float | int]]] = [
    ("best", "README.md", lambda x: best_score(x[1], float("inf"))),
    ("task", "stats/task-sorted.md", lambda x: x[0].task),
    ("ratio", "stats/ratio-sorted.md", lambda x: -our_length(x[0]) / max(best_score(x[1], 10), 10)),
    ("length", "stats/length-sorted.md", lambda x: -our_length(x[0])),
    ("diff", "stats/best-sorted.md", lambda x: best_score(x[1], 999999) - our_length(x[0])),
  ]

  for name, path, keyfunc in other_mds:
    with open(path, "w") as file:
      if path == "README.md":
        file.write("# Golf Stats\n\n")
        file.write(f"Accepted: {accepted}/400\n")
        file.write(f"Score: {score}\n\n")
        file.write(f"Best Score: {others_bests_sum}\n\n")
        file.write("- [leaderboard](https://www.kaggle.com/competitions/google-code-golf-2025/leaderboard)\n")
        file.write("- [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml#gid=0)\n\n")

      file.write("\n**other stats**\n")
      for other_name, other_path, _ in other_mds:
        if name == other_name: continue
        file.write(f"- [sorted by {other_name}](/{other_path})\n")

      file.write(f"\n\n## sorted by {name}\n\n")
      file.write(TaskResult.md_header())
      for stat, best in sorted(results_with_best, key=keyfunc):
        file.write(stat.md_row(best))

if __name__ == "__main__":
  os.makedirs("dist", exist_ok=True)
  os.makedirs("stats", exist_ok=True)
  os.makedirs(".cache", exist_ok=True)

  DISALLOW_RETIRE = ["base_keymoon", "base_yu", "base_kq5y", "base_zatsu"]

  INVALID = b"A" * 0x1000
  checked_hash = json.load(open(".cache/checked_cache.json", "r"))
  results: list[TaskResult] = []
  for i in tqdm(range(1, 401)):
    task = get_task(i)
    dist_path = f"dist/task{i:03}.py"
    if os.path.exists(dist_path):
      shortest = open(dist_path, "rb").read()
      best_result = TaskResult(i, True, "⚠️ regression?", dist_path, "previous", len(shortest))
    else:
      shortest = INVALID
      best_result = TaskResult(i, False)
    
    for base_path in get_code_paths("base_*", i):
      code = open(base_path).read().strip()
      code_for_check = "\n".join([l for l in code.split("\n") if not(_PAT_BEST.match(l) or _PAT_EQ.match(l))]) # <- splitlineにするとbyteリテラルテクが死ぬので注意
      if check_str(i, code_for_check, task, checked_hash).correct != 1.0:
        print(f"{base_path}: check failed")
        shutil.move(base_path, f"{base_path}~wa")
        continue
      
      for stripper, strip in strippers.items():
        code = strip(open(base_path).read())
        comp_name, compressed, _, compress_msg = compress.compress(code, best=best_result.length)
        if len(compressed) <= len(shortest):
          shortest = compressed
          best_result = TaskResult(i, True, compress_msg, base_path, f"{stripper}/{comp_name}", len(compressed))

    for ga_path, ga_base_source, ga_stripper, ga_method in _collect_ga_results(i):
      try:
        ga_bytes = ga_path.read_bytes()
      except OSError:
        continue
      if len(ga_bytes) < len(shortest):
        shortest = ga_bytes
        base_path_for_result = ga_base_source.as_posix() if ga_base_source is not None else ga_path.as_posix()
        best_result = TaskResult(
          i,
          True,
          "",
          base_path_for_result,
          f"{ga_stripper}/genetic-algo({ga_method})",
          len(ga_bytes),
        )

    if shortest == INVALID:
      print(f"[!] failed: vis/task{i:03}.png")
      results.append(TaskResult(i, False, "❌ WA"))
      continue

    if check_str(i, shortest, task, checked_hash).correct != 1.0:
      print(f"task {i}: stripped code check failed")
      print(f"{shortest=}")
      json.dump(checked_hash, open(".cache/checked_cache.json", "w"))
      exit(1)

    assert best_result.base_path is not None
    if not best_result.base_path.startswith("dist"):
      for base_path in get_code_paths("base_*", i):
        if base_path == best_result.base_path: continue
        if base_path.split("/")[0] in DISALLOW_RETIRE: continue
        print(f"[!] retire: {base_path}")
        shutil.move(base_path, f"{base_path}~retire")
    open(f"dist/task{i:03}.py", "wb").write(shortest)
    results.append(best_result)
  json.dump(checked_hash, open(".cache/checked_cache.json", "w"))
  handle_results(results)

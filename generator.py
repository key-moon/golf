import dataclasses
import os
import shutil
import sys
from typing import Callable
import json
import hashlib
from dataclasses import dataclass

from tqdm import tqdm

from checker import check, CheckRes
import compress
from dataclass_wizard import JSONWizard
from public_data import TaskSubmissionWithName, get_scores_per_task
from strip import strippers
from utils import get_code_paths, get_task

def check_str(task_id: int, code: str | bytes, task, checked_hash):
  digest = hashlib.sha256(code.encode() if isinstance(code, str) else code).hexdigest()
  tmp_path = f"tmp/{digest}.py"
  code_hash = f"{task_id:03d}|{digest}"
  if code_hash in checked_hash:
    return CheckRes(**{"outputs": [], **checked_hash[code_hash]})
  if isinstance(code, str):
    open(tmp_path, "w").write(code)
  if isinstance(code, bytes):
    open(tmp_path, "wb").write(code)
  res = check(tmp_path, task)
  checked_hash[code_hash] = dataclasses.asdict(res)
  del checked_hash[code_hash]["outputs"]
  if f"tmp.{digest}" in sys.modules:
    del sys.modules[f"tmp.{digest}"]
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


def handle_results(results: list[TaskResult]):
  success_tasks = [*filter(lambda x: x.success, results)]
  accepted = len(success_tasks)
  score = sum(2500 - res.length for res in success_tasks if res.length is not None)

  with open("dist/results.json", "w") as results_file:
    results_file.write(RunResult(score, results).to_json())

  print(f"accepted: {accepted}/400, {score=}")

  others_bests = get_scores_per_task()
  others_bests_sum = sum(bests[0]["score"] for bests in others_bests)

  other_mds: list[tuple[str, str, Callable[[tuple[TaskResult, list[TaskSubmissionWithName]]], int | float]]] = [
    ("diff", "README.md", lambda x: x[1][0]["score"] - (x[0].length if x[0].length else 999999)),
    ("task", "stats/task-sorted.md", lambda x: x[0].task),
    ("ratio", "stats/ratio-sorted.md", lambda x: -(x[0].length if x[0].length else 999999) / others_bests[x[0].task - 1][0]["score"]),
    ("length", "stats/length-sorted.md", lambda x: -(x[0].length if x[0].length else 999999)),
    ("best", "stats/best-sorted.md", lambda x: x[1][0]["score"]),
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
      for stat, bests in sorted(zip(results, others_bests), key=keyfunc):
        file.write(stat.md_row(bests[0]))

if __name__ == "__main__":
  os.makedirs("dist", exist_ok=True)
  os.makedirs("stats", exist_ok=True)
  os.makedirs(".cache", exist_ok=True)

  DISALLOW_RETIRE = ["base_keymoon", "base_yu"]

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
      if check_str(i, code, task, checked_hash).correct != 1.0:
        print(f"{base_path}: check failed")
        shutil.move(base_path, f"{base_path}~wa")
        continue
      
      for stripper, strip in strippers.items():
        code = strip(open(base_path).read())
        comp_name, compressed, _, compress_msg = compress.compress(code, best=best_result.length)
        if len(compressed) <= len(shortest):
          shortest = compressed
          best_result = TaskResult(i, True, compress_msg, base_path, f"{stripper}/{comp_name}", len(compressed))

    if shortest == INVALID:
      print(f"[!] failed: vis/task{i:03}.png")
      results.append(TaskResult(i, False, "❌ WA"))
      continue
    
    assert best_result.base_path is not None
    # retire all other codes
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

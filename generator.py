import base64
import os
import shutil
import sys
import zlib
import json
import dataclasses
import hashlib

from tqdm import tqdm

from checker import check, CheckRes
import compress
from public_data import get_scores_per_task
from strip import strippers
from utils import get_code_paths, get_task
import pandas as pd

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

@dataclasses.dataclass
class TaskResult:
  task: int
  success: bool
  message: str = ""
  base_path: str | None = None
  compressor: str | None = None
  length: int | None = None

  # TODO
  def md_row(self): ...


score = 0
accepted = 0

DISALLOW_RETIRE = ["base_keymoon", "base_yu"]

INVALID = b"A" * 0x1000
if __name__ == "__main__":
  checked_hash = json.load(open(".cache/checked_cache.json", "r"))
  stats = []
  for i in tqdm(range(1, 401)):
    task = get_task(i)
    dist_path = f"dist/task{i:03}.py"
    if os.path.exists(dist_path):
      shortest = open(dist_path, "rb").read()
      best_result = TaskResult(i, True, "⚠️ regression?", dist_path, "previons", len(shortest))
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
      stats.append(TaskResult(i, False, "❌ WA"))
      continue
    
    assert best_result.base_path is not None
    # retire all other codes
    if not best_result.base_path.startswith("dist"):
      for base_path in get_code_paths("base_*", i):
        if base_path == best_result.base_path: continue
        if base_path.split("/")[0] in DISALLOW_RETIRE: continue
        print(f"[!] retire: {base_path}")
        shutil.move(base_path, f"{base_path}~retire")

    # 圧縮後のチェックはしない
    # compressed = check_str(i, shortest, task, checked_hash)
    # if compressed.correct != 1.0:
    #   print(f"[!] compression failed: {compressed.message}")
    #   exit(1)

    score += 2500 - len(shortest)
    accepted += 1
    open(f"dist/task{i:03}.py", "wb").write(shortest)
    stats.append(best_result)

  print(f"accepted: {accepted}/400, {score=}")
  json.dump(checked_hash, open(".cache/checked_cache.json", "w"))

  others_best = get_scores_per_task()

  # Write stats to README
  def emit_table(stats,writer,b="."):
    writer.write("| Task | Base | Compressor | Length | Best | Goods | Message |\n")
    writer.write("|------|------|------------|--------|------|-------|---------|\n")
    for stat in stats:
      task = f"{stat['task']:03}"

      base = f"[{stat['base_path'].split('/')[0]}]({b}/{stat['base_path']})" if stat["success"] else "-"
      checker = stat["compressor"] if stat["success"] else "-"

      length = f"[{stat['length']}]({b}/dist/task{task}.py)" if stat["success"] else "-"
      best_sub = others_best[int(stat['task']) - 1][0]
      best, best_person = best_sub["score"], best_sub["name"]
      if stat["success"] and best != "-":
        diff = stat["length"] - best
        best = f"{best} {'🟢' if diff < 0 else '🔴' if diff > 0 else ''} by {best_person}"
        length = f"{length} ({'+' if diff > 0 else ''}{diff})"
      message = stat["message"]
      writer.write(f"| [{task}]({b}/vis/task{task}.png) | {base} | {checker} | {length} | {best} | [vis-many]({b}/vis_many/task{task}.png) | {message} |\n")

  with open("README.md", "w") as file:
    file.write("# Golf Stats\n\n")

    file.write(f"Accepted: {accepted}/400\n")
    file.write(f"Score: {score}\n\n")
    file.write("- [leaderboard](https://www.kaggle.com/competitions/google-code-golf-2025/leaderboard)\n")
    file.write("- [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml#gid=0)\n\n")
    file.write("Alt Tables:\n")
    file.write("- [sorted by task](stats/task-sorted.md)\n")
    file.write("- [sorted by ratio](stats/ratio-sorted.md)\n")
    file.write("- [sorted by length](stats/length-sorted.md)\n")
    file.write("- [sorted by best](stats/best-sorted.md)\n\n")
    file.write("## Task Details\n\n")
    emit_table(sorted(stats, key=lambda x: int(others_best[x['task'] - 1]) - (x["length"] if x["length"] is not None else 999999)), file)
  with open("stats/task-sorted.md", "w") as file:
    file.write("- [README](../README.md)\n")
    file.write("- [sorted by ratio](ratio-sorted.md)\n")
    file.write("- [sorted by length](length-sorted.md)\n")
    file.write("- [sorted by best](best-sorted.md)\n\n")
    file.write("## sorted by task\n\n")
    emit_table(stats, file, b="..")
  with open("stats/ratio-sorted.md", "w") as file:
    file.write("- [README](../README.md)\n")
    file.write("- [sorted by task](task-sorted.md)\n")
    file.write("- [sorted by length](length-sorted.md)\n")
    file.write("- [sorted by best](best-sorted.md)\n\n")
    file.write("## sorted by ratio\n\n")
    emit_table(sorted(stats, key=lambda x: -(x["length"] if x["length"] is not None else 999999) / int(others_best[x['task'] - 1])), file, b="..")
  with open("stats/length-sorted.md", "w") as file:
    file.write("- [README](../README.md)\n")
    file.write("- [sorted by task](task-sorted.md)\n")
    file.write("- [sorted by ratio](ratio-sorted.md)\n")
    file.write("- [sorted by best](best-sorted.md)\n\n")
    file.write("## sorted by length\n\n")
    emit_table(sorted(stats, key=lambda x: -(x["length"] if x["length"] is not None else 999999)), file, b="..")
  with open("stats/best-sorted.md", "w") as file:
    file.write("- [README](../README.md)\n")
    file.write("- [sorted by task](task-sorted.md)\n")
    file.write("- [sorted by ratio](ratio-sorted.md)\n")
    file.write("- [sorted by length](length-sorted.md)\n\n")
    file.write("## sorted by best\n\n")
    emit_table(sorted(stats, key=lambda x: int(others_best[x['task'] - 1])), file, b="..")


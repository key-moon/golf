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

def read_others_best():
  csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?gid=1427788625&single=true&output=csv"
  df = pd.read_csv(csv_url)
  best_values = df.iloc[7:407, 1].tolist()
  return [v if isinstance(v, str) else "-" for v in best_values]

score = 0
accepted = 0

DISALLOW_RETIRE = ["base_keymoon", "base_yu"]

LONG = b"A" * 0x1000
if __name__ == "__main__":
  checked_hash = json.load(open("checked_cache.json", "r"))
  stats = []
  for i in tqdm(range(1, 401)):
    task = get_task(i)
    dist_path = f"dist/task{i:03}.py"
    if os.path.exists(dist_path):
      shortest = open(dist_path, "rb").read()
      task_stat = {
        "task": i,
        "base_path": dist_path,
        "compressor": "previous",
        "length": len(shortest),
        "message": "regression?",
        "success": True
      }
    else:
      shortest = LONG
      task_stat = {
        "task": i,
        "base_path": None,
        "compressor": None,
        "length": None,
        "message": None,
        "success": False
      }
    for base_path in get_code_paths("base_*", i):
      code = open(base_path).read().strip()
      if check_str(i, code, task, checked_hash).correct != 1.0:
        print(f"{base_path}: check failed")
        shutil.move(base_path, f"{base_path}~wa")
        continue
      
      for stripper, strip in strippers.items():
        code = strip(open(base_path).read())
        if check_str(i, code, task, checked_hash).correct != 1.0:
          print(f"{base_path}: strip failed, {check_str(i, code, task, checked_hash).message}")
          task_stat["base_path"] = base_path
          task_stat["message"] = check_str(i, code, task, checked_hash).message
          stats.append(task_stat)
          exit(1)
          continue

        comp_name, compressed = compress.compress(code)
        if len(compressed) <= len(shortest):
          shortest = compressed
          task_stat["base_path"] = base_path
          task_stat["compressor"] = f"{stripper}/{comp_name}"
          task_stat["length"] = len(compressed)
          task_stat["message"] = "AC"
          task_stat["success"] = True

    if shortest == LONG:
      print(f"[!] failed: vis/task{i:03}.png")
      task_stat["message"] = "WA"
      stats.append(task_stat)
      continue

    if not task_stat["base_path"].startswith("dist"):
      for base_path in get_code_paths("base_*", i):
        if base_path == task_stat["base_path"]: continue
        if base_path.split("/")[0] in DISALLOW_RETIRE: continue
        print(f"[!] retire: {base_path}")
        shutil.move(base_path, f"{base_path}~retire")


    # 圧縮後のチェックをしない
    # compressed = check_str(i, shortest, task, checked_hash)
    # if compressed.correct != 1.0:
    #   print(f"[!] compression failed: {compressed.message}")
    #   task_stat["message"] = compressed.message
    #   task_stat["success"] = False
    #   stats.append(task_stat)
    #   exit(1)

    score += 2500 - len(shortest)
    accepted += 1
    open(f"dist/task{i:03}.py", "wb").write(shortest)
    stats.append(task_stat)

  print(f"accepted: {accepted}/400, {score=}")
  json.dump(checked_hash, open("checked_cache.json", "w"))

  others_best = read_others_best()
  # Write stats to README
  with open("README.md", "w") as readme:
    readme.write("# Golf Stats\n\n")
    readme.write(f"Accepted: {accepted}/400\n")
    readme.write(f"Score: {score}\n\n")
    readme.write("- [leaderboard](https://www.kaggle.com/competitions/google-code-golf-2025/leaderboard)\n- [spreadsheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml#gid=0)\n\n")
    readme.write("## Task Details\n\n")
    readme.write("| Task | Success | Base | Compressor | Length | Best | Goods | Message |\n")
    readme.write("|------|---------|------|------------|--------|------|-------|---------|\n")
    for stat in stats:
      task = f"{stat['task']:03}"
      success = (("✅" if stat["message"] == "AC" else "❗") if "arcdsl" not in stat["base_path"] else "⚠️") if stat["success"] else "❌"
      base = f"[{stat['base_path'].split("/")[0]}]({stat['base_path']})" if stat["success"] else "-"
      checker = stat["compressor"] if stat["success"] else "-"

      length = str(stat["length"]) if stat["success"] else "-"
      best = others_best[stat['task'] - 1]
      if stat["success"] and best != "-":
        if stat["length"] < int(best):
          best = f"{best} 🟢"
        elif stat["length"] > int(best):
          best = f"{best} 🔴"
      message = stat["message"]
      readme.write(f"| [{task}](vis/task{task}.png) | {success} | {base} | {checker} | [{length}](dist/task{task}.py) | {best} | [prompt](prompts/task{task}.txt) / [vis-many](vis_many/task{task}.png) | {message} |\n")

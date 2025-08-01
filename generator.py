import base64
import shutil
import sys
import zlib

from checker import check
import compress
from strip import strip
from utils import get_code_paths, get_task
import os

def check_str(code: str | bytes, task):
    tmp_path = "tmp/tmp.py"
    if isinstance(code, str):
      open(tmp_path, "w").write(code)
    if isinstance(code, bytes):
      open(tmp_path, "wb").write(code)
    res = check(tmp_path, task)
    if "tmp.tmp" in sys.modules:
      del sys.modules["tmp.tmp"]
    shutil.rmtree('tmp/__pycache__', ignore_errors=True)
    return res

score = 0
accepted = 0

SLOW = ["base_yu/task002.py", "base_yu/task396.py"]

LONG = b"A" * 0x1000
if __name__ == "__main__":
  stats = []
  for i in range(1, 401):
    task = get_task(i)
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
      do_check = base_path not in SLOW
      if do_check and check(base_path, task).correct != 1.0:
        continue
      
      print(base_path)
      code = strip(open(base_path).read())
      if do_check and check_str(code, task).correct != 1.0:
        print(f"{base_path}: strip failed, {check_str(code, task).message}")
        task_stat["base_path"] = base_path
        task_stat["message"] = check_str(code, task).message
        stats.append(task_stat)
        exit(1)
        continue

      cmp, compressed = compress.compress(code)
      if len(compressed) < len(shortest):
        shortest = compressed
        task_stat["base_path"] = base_path
        task_stat["compressor"] = cmp
        task_stat["length"] = len(compressed)
        task_stat["success"] = True

    if shortest == LONG:
      print(f"[!] failed: vis/task{i:03}.png")
      task_stat["message"] = "WA"
      stats.append(task_stat)
      continue
    if task_stat["base_path"] not in SLOW:
      compressed = check_str(shortest, task)
      if compressed.correct != 1.0:
        print(f"[!] compression failed: {compressed.message}")
        task_stat["message"] = compressed.message
        task_stat["success"] = False
        stats.append(task_stat)
        exit(1)

    score += 2500 - len(shortest)
    accepted += 1
    open(f"dist/task{i:03}.py", "wb").write(shortest)
    stats.append(task_stat)

  print(f"accepted: {accepted}/400, {score=}")

  # Write stats to README
  with open("README.md", "w") as readme:
    readme.write("# Golf Stats\n\n")
    readme.write(f"Accepted: {accepted}/400\n")
    readme.write(f"Score: {score}\n\n")
    readme.write("## Task Details\n\n")
    readme.write("| Task | Success | Base | Compressor | Length | Goods | Message |\n")
    readme.write("|------|---------|------|------------|--------|-------|---------|\n")
    for stat in stats:
      task = f"{stat['task']:03}"
      success = ("✅" if "arcdsl" not in stat["base_path"] else "⚠️") if stat["success"] else "❌"
      base = f"[{stat['base_path']}]({stat['base_path']})" if stat["success"] else "-"
      checker = stat["compressor"] if stat["success"] else "-"

      length = str(stat["length"]) if stat["success"] else "-"
      message = stat["message"] if not stat["success"] else "-"
      readme.write(f"| [{task}](vis/task{task}.png) | {success} | [{base}]({base}) | {checker} | [{length}](dist/task{task}.py) | [prompt](prompts/task{task}.txt) / [vis-many](vis_many/task{task}.png) | {message} |\n")

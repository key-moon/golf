import glob
import json

def parse_range_str(range_str: str):
  s = set()
  for part in range_str.strip().split(","):
    if "-" in part:
      start, end = map(int, part.split("-"))
      s.update(range(start, end + 1))
    else:
      s.add(int(part))
  return sorted(s)

def get_code_paths(base_path: str, i: int):
  return glob.glob(f"{base_path}/task{i:03}*.py")

def get_task(i: int):
  return json.load(open(f"tasks/task{i:03}.json", "r"))
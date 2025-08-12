import glob
import json
from typing import TypedDict

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


Case = TypedDict('Case', {'input': list[list[int]], 'output': list[list[int]]})
Cases = list[Case]
Task = TypedDict('Task', {'train': list[Case], 'test': list[Case], 'arc-gen': list[Case]})


def get_task(i: int) -> Task:
  return json.load(open(f"tasks/task{i:03}.json", "r"))

def get_cases(i: int) -> Cases:
  task = get_task(i)
  return task["train"] + task["test"] + task["arc-gen"]

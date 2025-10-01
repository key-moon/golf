import base64
import glob
import json
import os
import pickle
from typing import Callable, TypeVar, TypedDict


def signed_str(x: int):
  return f"+{x}" if 0 <= x else str(x)

def parse_range_str(range_str: str):
  s = set()
  for part in range_str.strip().split(","):
    if "-" in part:
      start, end = map(int, part.split("-"))
      s.update(range(start, end + 1))
    else:
      s.add(int(part))
  return sorted(s)

def get_code_paths(base_path: str, i: int, skip_generated=False, include_retire=False):
  paths = glob.glob(f"{base_path}/task{i:03}*.py")
  if include_retire:
    paths = paths + glob.glob(f"{base_path}/task{i:03}*.py~retire")
  if skip_generated:
    paths = [path for path in paths if "arc" not in path and "notebooks" not in path and "code" not in path]
  return paths


Case = TypedDict('Case', {'input': list[list[int]], 'output': list[list[int]]})
Cases = list[Case]
Task = TypedDict('Task', {'train': list[Case], 'test': list[Case], 'arc-gen': list[Case]})

WORKSPACE_DIR = os.path.dirname(__file__)

def get_task(i: int) -> Task:
  return json.load(open(os.path.join(WORKSPACE_DIR, "tasks", f"task{i:03}.json"), "r"))

def get_cases(i: int) -> Cases:
  task = get_task(i)
  return task["train"] + task["test"] + task["arc-gen"]

OSC = "\x1b]8;;"
BEL = "\x07"

def openable_uri(title: str, uri: str):
  return f"{OSC}{uri}{BEL}{title}{OSC}{BEL}"

def viz_plane_url(plane: bytes):
  return f"https://deflate-viz.pages.dev?text={base64.b64encode(plane).decode().replace('+', '%2B').replace('/', '%2F').replace('=', '%3D')}"

def viz_deflate_url(deflate: bytes):
  return f"https://deflate-viz.pages.dev?deflate={base64.b64encode(deflate).decode().replace('+', '%2B').replace('/', '%2F').replace('=', '%3D')}"

T = TypeVar("T")

CACHE_DIR = os.path.join(os.path.dirname(__file__), ".cache")
def pickle_cache(cache_name: str, func: Callable[[], T]) -> T:
  cache_path = os.path.join(CACHE_DIR, cache_name)
  if os.path.exists(cache_path):
    with open(cache_path, "rb") as f:
      return pickle.load(f)
  result = func()
  with open(cache_path, "wb") as f:
    pickle.dump(result, f)
  return result

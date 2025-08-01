import copy
import glob
import json
import multiprocessing.pool
import os
import sys
import traceback
import multiprocessing

from utils import parse_range_str

def check(path: str, task: dict):
  assert path.endswith(".py")
  module_name = path[:-3].replace("/", ".")
  try:
    parent_module = __import__(module_name)
  except SyntaxError as e:
    return 0, e.msg
  module = parent_module
  for s in module_name.split(".")[1:]:
    module = getattr(module, s)
  if not hasattr(module, "p"):
    return 0.0, "no attribute p"
  program = getattr(module, "p")
  if not callable(program):
    return 0.0, "p is not callable"
  tests = task["train"] + task["test"] + task["arc-gen"]
  wrong, right = 0, 0

  errors = set()
  with multiprocessing.Pool(1) as pool:
    for example in tests:
      example_copy = copy.deepcopy(example)
      try:
        result = pool.apply_async(program, (example_copy["input"],))
        output = result.get(timeout=0.2)
        if output == example_copy["output"]:
          right += 1
        else:
          wrong += 1
      except TimeoutError as e:
        errors.add("timeout")
        break
      except Exception as e:
        tb = traceback.format_exception(type(e), e, e.__traceback__)
        errors.add(tb[0])
        wrong += 1

  if errors:
    return right / len(tests), "\n\n".join(errors)
  return right / len(tests), "ok"

if __name__ == "__main__":
  dirname = sys.argv[1] if 2 <= len(sys.argv) else "dist"
  range_str = sys.argv[2] if 3 <= len(sys.argv) else "1-400"
  
  print(f"{dirname=}")
  for i in parse_range_str(range_str):
    for hoge in get_base_code_paths(dirname, i):
      if not os.path.exists(hoge): continue
      task = json.load(open(f"tasks/task{i:03}.json", "r"))
      correct, msg = check(hoge, task)
      if correct == 1.:
        print(f"✅ {hoge}")
      else:
        print(f"❌ {hoge}")
        print(f"{correct=}" if msg == "ok" else msg)
  
import copy
import glob
import json
import multiprocessing.pool
import os
from signal import alarm
import signal
import sys
from time import sleep
import traceback
import multiprocessing

from strip import strip
from utils import get_code_paths, get_task, parse_range_str

class TimeoutException(Exception): pass
def handler(signum, frame):
  raise TimeoutException()
signal.signal(signal.SIGALRM, handler)

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
  for example in tests:
    example_copy = copy.deepcopy(example)
    try:
      signal.setitimer(signal.ITIMER_REAL, 0.2)
      # signal.alarm(1)
      output = program(example_copy["input"])
      signal.alarm(0)
      if output == example_copy["output"]:
        right += 1
      else:
        wrong += 1
    except TimeoutException as e:
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
    task = get_task(i)
    for code_path in get_code_paths(dirname, i):
      if not os.path.exists(code_path): continue
      correct, msg = check(code_path, task)
      if correct == 1.:
        with open(code_path, "r") as f:
          code = strip(f.read().strip())
        print(f"✅ {code_path} {len(code)=}")
      else:
        print(f"❌ {code_path}")
        print(f"{correct=}" if msg == "ok" else msg)

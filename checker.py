import copy
from dataclasses import dataclass
import os
import signal
import sys
import traceback
from typing import Optional, Tuple
import matplotlib.pyplot as plt

import numpy as np

from task_viz import cmap, norm
from strip import strip
from utils import get_code_paths, get_task, parse_range_str

class TimeoutException(Exception): pass
def handler(signum, frame):
  raise TimeoutException()
signal.signal(signal.SIGALRM, handler)

Matrix = list[list[int]]
@dataclass
class CheckRes:
  outputs: list[Tuple[Matrix, Optional[Matrix]]]
  correct: float
  message: str

def check(path: str, task: dict):
  assert path.endswith(".py")
  module_name = path[:-3].replace("/", ".")
  try:
    parent_module = __import__(module_name)
  except SyntaxError as e:
    return CheckRes([], 0, e.msg)
  module = parent_module
  for s in module_name.split(".")[1:]:
    module = getattr(module, s)
  if not hasattr(module, "p"):
    return CheckRes([], 0.0, "no attribute p")
  program = getattr(module, "p")
  if not callable(program):
    return CheckRes([], 0.0, "p is not callable")
  tests = task["train"] + task["test"] + task["arc-gen"]
  wrong, right = 0, 0

  errors = set()
  outputs = []
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
        outputs.append(output)
        wrong += 1
    except TimeoutException as e:
      outputs.append(None)
      errors.add("timeout")
      break
    except Exception as e:
      signal.alarm(0)
      outputs.append(None)
      tb = traceback.format_exception(type(e), e, e.__traceback__)
      errors.add(tb[0])
      wrong += 1

  if errors:
    return CheckRes(outputs, right / len(tests), "\n\n".join(errors))
  return CheckRes(outputs, right / len(tests), "ok")

def visualize_outputs(task, outputs, num_visualize, path):
    tasks  = []
    tasks += [(f"train_{i}", t) for i, t in enumerate(task['train'])]
    tasks += [(f"test_{i}", t) for i, t in enumerate(task['test'])]
    tasks += [(f"arcgen_{i}", t) for i, t in enumerate(task['arc-gen'])]
    fig, axes = plt.subplots(num_visualize, 3, figsize=(5 * 3, 5 * num_visualize))
    for idx, (name, task) in enumerate(tasks[:num_visualize]):
      mat_inp = np.array(task['input']) 
      shape_i = mat_inp.shape
      mat_out = np.array(task['output'])
      shape_o = mat_out.shape
      axes[idx, 0].set_title(f"{shape_i}")
      axes[idx, 0].imshow(mat_inp, cmap=cmap, norm=norm)
      axes[idx, 1].set_title(f"{shape_o}")
      axes[idx, 1].imshow(mat_out, cmap=cmap, norm=norm)
      axes[idx, 1].axis('off')
      if outputs[idx] is not None:
        mat_out_pred = np.array(outputs[idx])
        shape_p = mat_out_pred.shape
        axes[idx, 2].set_title(f"{shape_p}")
        axes[idx, 2].imshow(mat_out_pred, cmap=cmap, norm=norm)
      else:
        axes[idx, 2].set_title("FAILED")
        axes[idx, 2].axis('off')
    plt.tight_layout()
    plt.savefig(path)

if __name__ == "__main__":
  dirname = sys.argv[1] if 2 <= len(sys.argv) else "dist"
  range_str = sys.argv[2] if 3 <= len(sys.argv) else "1-400"
  
  print(f"{dirname=}")
  for i in parse_range_str(range_str):
    task = get_task(i)
    for code_path in get_code_paths(dirname, i):
      if not os.path.exists(code_path): continue
      res = check(code_path, task)
      if len(res.outputs) > 0:
        visualize_outputs(task, res.outputs, min(5, len(res.outputs)), f"vis_output/task{i:03}.png")
      if res.correct == 1.:
        with open(code_path, "r") as f:
          code = strip(f.read().strip())
        print(f"✅ {code_path} {len(code)=}")
      else:
        print(f"❌ {code_path}")
        print(f"{res.correct=}" if res.message == "ok" else res.message)

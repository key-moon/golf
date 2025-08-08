import copy
from dataclasses import dataclass
import os
import signal
import sys
import traceback
from typing import Optional, Tuple
import matplotlib.pyplot as plt
import inspect
import builtins, sys

import numpy as np

import compress
from task_viz import cmap, norm
from strip import strip_for_plain, strip_for_zlib
from utils import get_code_paths, get_task, parse_range_str
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)

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

trust_paths = [
  "base_code/",
  "base_arcdsl/",
  "base_keymoon/",
  "base_yu/",
]

def check(path: str, task: dict, knockout=-1):
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
  for case, example in enumerate(tests):
    example_copy = copy.deepcopy(example)
    try:
      signal.setitimer(signal.ITIMER_REAL, 4)
      module.CASE = module._CASE = case
      # signal.alarm(1)
      if "case" in inspect.signature(program).parameters:
       output = program(example_copy["input"], case=case)
      else:
       output = program(example_copy["input"])
      signal.alarm(0)
      if output == example_copy["output"]:
        right += 1
      else:
        outputs.append((example, case, output))
        wrong += 1
        if 0 < knockout and knockout <= wrong:
          break
    except TimeoutException as e:
      outputs.append((example, case, None))
      errors.add("timeout")
      break
    except Exception as e:
      signal.alarm(0)
      outputs.append((example, case, None))
      tb = traceback.format_exception(type(e), e, e.__traceback__.tb_next)
      errors.add("\n".join(tb))
      wrong += 1

  correct = right / len(tests)
  if errors:
    return CheckRes(outputs, correct, "\n\n".join(errors))
  return CheckRes(outputs, correct, "ok" if right == len(tests) else f"{correct=}")

def visualize_outputs(outputs, path):
    num_visualize = min(len(outputs), 10)
    fig, axes = plt.subplots(max(2,num_visualize), 3, figsize=(5 * 3, 5 * num_visualize))
    for idx, (task, case, output) in enumerate(outputs):
      if num_visualize <= idx: break
      mat_inp = np.array(task['input']) 
      shape_i = mat_inp.shape
      mat_out = np.array(task['output'])
      shape_o = mat_out.shape
      axes[idx, 0].set_title(f"{case} / {shape_i}")
      axes[idx, 0].imshow(mat_inp, cmap=cmap, norm=norm)
      axes[idx, 1].set_title(f"{shape_o}")
      axes[idx, 1].imshow(mat_out, cmap=cmap, norm=norm)
      axes[idx, 1].axis('off')
      if output is not None:
        try:
          mat_out_pred = np.array(output)
          shape_p = mat_out_pred.shape
          axes[idx, 2].set_title(f"{shape_p}")
          axes[idx, 2].imshow(mat_out_pred, cmap=cmap, norm=norm)
        except:
          print(f"weird shape: {output}")
      else:
        axes[idx, 2].set_title("FAILED")
        axes[idx, 2].axis('off')
    plt.tight_layout()
    plt.savefig(path)

if __name__ == "__main__":
  dirname = sys.argv[1] if 2 <= len(sys.argv) else "dist"
  range_str = sys.argv[2] if 3 <= len(sys.argv) else "1-400"
  
  r = parse_range_str(range_str)
  do_vis = len(r) < 10

  success = 0
  print(f"{dirname=}")
  for i in r:
    task = get_task(i)
    for code_path in get_code_paths(dirname, i):
      if not os.path.exists(code_path): continue
      res = check(code_path, task)
      try:
        with open(code_path, "r") as f:
          orig_code = f.read().strip()
          code = strip_for_plain(orig_code)
          compressed = compress.compress(strip_for_zlib(orig_code), force_compress=True)[1]
      except UnicodeDecodeError:
        with open(code_path, "rb") as f:
          code = compressed = f.read()
      if res.correct == 1.:
        print(f"✅ {code_path} {len(code)=} {len(compressed)=}")
        success += 1
      else:
        print(f"❌ {code_path} {len(code)=}")
        print(f"{res.correct=}" if res.message == "ok" else res.message)
      if len(res.outputs) > 0 and do_vis:
        vis_path=f"vis_output/task{i:03}.png"
        visualize_outputs(res.outputs, vis_path)
        print(f"{vis_path=}")
  print(f"success: {success}/{len(r)}")
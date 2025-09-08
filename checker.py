import copy
from dataclasses import dataclass
import json
import os
import signal
import sys
import traceback
from typing import Any, Optional, Tuple
from dataclass_wizard import JSONWizard
import matplotlib.pyplot as plt
import inspect
import sys

import numpy as np
from tqdm import tqdm

import compress
from viz import cmap, norm, printmat
from strip import ZLIB_GOLF_BANNER, og_strip, strip_for_plain, strip_for_zlib
from utils import WORKSPACE_DIR, Case, Task, get_code_paths, get_task, openable_uri, parse_range_str, viz_deflate_url, viz_plane_url
import warnings
import argparse

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

class TimeoutException(Exception): pass
def handler(signum, frame):
  raise TimeoutException()
signal.signal(signal.SIGALRM, handler)

Matrix = list[list[int]]

@dataclass
class Output(JSONWizard):
  case: Case
  casenum: int
  output: Optional[Matrix]
  dumps: list[Any]
  verdict: bool

@dataclass
class CheckRes(JSONWizard):
  outputs: list[Output]
  correct: float
  message: str

trust_paths = [
  "base_code/",
  "base_arcdsl/",
  "base_keymoon/",
  "base_yu/",
]

def check(path: str, task: Task, knockout=-1) -> CheckRes:
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
  outputs: list[Output] = []
  for casenum, case in enumerate(tqdm(tests)):
    example_copy = copy.deepcopy(case)
    dumps = []
    try:
      # signal.setitimer(signal.ITIMER_REAL, 4)
      # signal.alarm(1)
      module.CASE = casenum
      module.ANSWER = module.CORRECT = module.EXPECTED = example_copy["output"]
      module.DUMP = lambda x,defalut=False: dumps.append(json.loads(json.dumps(x)))or defalut or x
      module.PRINT = lambda *x: print(*x)or x[0]
      module.PRINTMAT = lambda x: printmat(x)or x
      output: Matrix = program(example_copy["input"]) # pyright: ignore[reportAssignmentType]
      signal.alarm(0)
      verdict = json.loads(json.dumps(output)) == example_copy["output"]
      outputs.append(Output(case, casenum, output, dumps, verdict))
      if verdict:
        right += 1
      else:
        wrong += 1
    except TimeoutException as e:
      outputs.append(Output(case, casenum, None, dumps+["ERROR: timeout"], False))
      errors.add("timeout")
      break
    except Exception as e:
      signal.alarm(0)
      tb = traceback.format_exception(type(e), e, e.__traceback__.tb_next)
      errors.add("\n".join(tb))
      outputs.append(Output(case, casenum, None, dumps+[f"ERROR: {tb}"], False))
      wrong += 1
    if 0 < knockout and knockout <= wrong:
      break
  correct = right / len(tests)
  if errors:
    return CheckRes(outputs, correct, "\n\n".join(errors))
  return CheckRes(outputs, correct, "ok" if right == len(tests) else f"{correct=}")

def visualize_outputs(outputs: list[Output], path):
    num_visualize = min(len(outputs), 10)
    fig, axes = plt.subplots(max(2,num_visualize), 3, figsize=(5 * 3, 5 * num_visualize))
    for idx, output_obj in enumerate(outputs):
      if num_visualize <= idx: break
      case, casenum, output = output_obj.case, output_obj.casenum, output_obj.output
      mat_inp = np.array(case['input']) 
      shape_i = mat_inp.shape
      mat_out = np.array(case['output'])
      shape_o = mat_out.shape
      axes[idx, 0].set_title(f"{casenum} / {shape_i}")
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
  parser = argparse.ArgumentParser(description="Checker script for golf tasks.")
  parser.add_argument("dirname", nargs="?", default="dist", help="Directory name containing code files")
  parser.add_argument("range_str", nargs="?", default="1-400", help="Range string for tasks")
  parser.add_argument("--strip", "-s", action="store_true", help="Only strip code and exit")
  parser.add_argument("--knockout", "-k", type=int, default=-1, help="Maximum number of wrongs before stopping (default -1 = disabled)")
  args = parser.parse_args()

  dirname = args.dirname
  range_str = args.range_str
  knockout = args.knockout
  r = parse_range_str(range_str)
  username = os.environ.get("USER", "unknown")
  do_vis = len(r) < 10 and username != "keymoon"

  success = 0
  print(f"{dirname=}")
  for i in r:
    task = get_task(i)
    for code_path in get_code_paths(dirname, i):
      if not os.path.exists(code_path): continue
      res = check(code_path, task, knockout)
      try:
        with open(code_path, "r") as f:
          orig_code = f.read().strip()
          code = strip_for_plain(orig_code).encode()
          stripped = og_strip(orig_code) if ZLIB_GOLF_BANNER in orig_code else strip_for_zlib(orig_code)
          compress_method, compressed, raw_compressed, _ = compress.compress(stripped, fast=True, force_compress=True)
      
          if args.strip:
            if code.decode("L1") in orig_code:
              print(f"[!] Stripped code exists in {code_path}")
            else:
              with open(code_path, "a") as f:
                f.write("\n\n# stripped:")
                for line in code.decode().split("\n"):
                  f.write(f"\n# {line}")
              print(f"[+] Appended code to {code_path}")
      except UnicodeDecodeError:
        with open(code_path, "rb") as f:
          code = compressed = f.read()
        compress_method = "unknown"
        raw_compressed = b""
      if res.correct == 1.:
        print(f"✅ {code_path} {len(code)=} {len(compressed)=} (optimal: {len(raw_compressed) + 60})")
        success += 1
      else:
        print(f"❌ {code_path} {len(code)=} {len(compressed)=} (optimal: {len(raw_compressed) + 60})")
        print(f"{res.correct=}")
        # if res.message != "ok": print(res.message)
      compressed_msg = openable_uri("compressed", viz_deflate_url(raw_compressed)) if compress_method.startswith("zlib") else f"(not compressed by zlib)"
      print(f"{openable_uri('stripped code', viz_plane_url(code))} / {compressed_msg}")

      json.dump({ "task": i, "outputs": [output.to_dict() for output in res.outputs] }, open(os.path.join(WORKSPACE_DIR, "tmp", "outputs.json"), "w"))
      print("http://localhost:5000/judge")

      wrong_outputs = [*filter(lambda x: not x.verdict, res.outputs)]
      if len(wrong_outputs) > 0 and do_vis:
        vis_path=f"vis_output/task{i:03}.png"
        visualize_outputs(wrong_outputs, vis_path)
        print(f"{vis_path=}")
  print(f"success: {success}/{len(r)}")
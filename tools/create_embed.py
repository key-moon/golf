"""
s=%DICT%
def p(g):
 %PREFIX%
 return s[%INDEX%]
"""

from tqdm import tqdm
from compress import compress
from utils import get_task

def tuphash(inp): return hash((*zip(*inp),))

def hasher_tuphashmod(cases):
  mod = len(cases)
  tuphashes = [tuphash(inp) for inp, _ in cases]
  assert len(tuphashes) == len(set(tuphashes))
  while True:
    keys = [h%mod for h in tuphashes]
    if len(set(keys)) != len(keys):
      mod += 1
      continue
    
    dic = repr({k: v for k, v in zip(keys, [out for _, out in cases])}).replace(" ", "")
    return f"p=lambda g:{dic}[hash((*zip(*g),))%{mod}]"

def is_worth_embed(cases):
  oups = [out for _, out in cases]
  oups_embed = compress(repr(oups).replace(" ", ""))[1]
  print(f"{len(oups_embed)=}")
  return len(oups_embed) <= 2500

for i in tqdm(range(1, 401)):
  task = get_task(i)
  seen_inputs = set()
  cases = []
  for case in task["train"] + task["test"] + task["arc-gen"]:
      if tuphash(case["input"]) not in seen_inputs:
          seen_inputs.add(tuphash(case["input"]))
          cases.append((case["input"], case["output"]))
  if not is_worth_embed(cases):
    continue
  print(f"[+] create embedding for {i}...")
  open(f"base_embed/task{i:03}_tuphashmod.py", "w").write(hasher_tuphashmod(cases))

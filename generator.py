import base64
import copy
import importlib
import json
import os
import glob
import re
import sys
import zlib

from checker import check, get_task

def get_base_code_paths(i):
  return glob.glob(f"base_code/task{i:03}*.py")

def strip(code: str):
  lines = code.splitlines()
  if len(lines) == 1: return code
  res = ""
  basic_indent = len(lines[1]) - len(lines[1].lstrip(' '))
  for l in lines:
    indent = len(l) - len(l.lstrip(' '))
    if l.find("#"):
      l = l.split("#")[0]
    res += " " * (indent // basic_indent) + l.strip()
    res += "\n"
  return res.strip()

def vanilla(code: str):
  return code.strip()
def compress_zlib_b85(code: str):
  compressed_code = base64.b85encode(zlib.compress(code.encode(), level=9))
  return f"import zlib;import base64;exec(zlib.decompress(base64.b85decode({compressed_code!r})))"
def compress_zlib_repr_bytes(code: str):
  compressed_code = zlib.compress(code.encode(), level=9)
  return f"import zlib;exec(zlib.decompress({compressed_code!r}))"

compressors = [vanilla, compress_zlib_b85, compress_zlib_repr_bytes]

def check_str(code: str, task):
    tmp_path = "tmp/tmp.py"
    open(tmp_path, "w").write(code)
    res = check(tmp_path, task)
    del sys.modules["tmp.tmp"]
    return res

LONG = "A" * 0x1000
for i in range(1, 401):
  task = get_task(i)
  shortest = LONG
  for base_path in get_base_code_paths(i):
    if check(base_path, task)[0] != 1.0:
      continue
    
    code = strip(open(base_path).read())
    if check_str(code, task)[0] != 1.0:
      print(f"{base_path}: strip failed")
      input("> ")
      continue

    a = sorted(zip([cmp(code) for cmp in compressors], compressors), key=lambda x: len(x[0]))
    print(f"{base_path}: {' / '.join(f'{cmp.__name__}->{len(code)}' for code, cmp in a)}")

    for code, cmp in a:
      res = check_str(code, task)
      if res[0] != 1.0:
        print(f"[!] failed: {res}")
    
    compressed = a[0][0]
    if len(compressed) < len(shortest):
      shortest = compressed

  if shortest == LONG:
    continue
  open(f"dist/task{i:03}.py", "w").write(shortest)

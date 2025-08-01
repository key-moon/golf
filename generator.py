import base64
import shutil
import sys
import zlib

from checker import check
from strip import strip
from utils import get_code_paths, get_task
import os

def raw(code: str):
  return code.strip().encode()
def compress(code: str):
  compressed_code = zlib.compress(code.encode(), level=9)

  # TODO: r"" とか使うとマシになったりするかも / "\n" にして """ -> " とかのほうが実は効率いいケースもある
  compressed_code = compressed_code.replace(b"\\", b"\\\\")
  # null byteはソースコードに入れられない null byte を \0 に置換したとき、\01 みたいなのが間違って解釈されるのを防ぐ
  for i in range(8): compressed_code = compressed_code.replace(b"\x00" + f"{i}".encode(), b"\\000" + f"{i}".encode())
  # \r はなんかパースされたあとに \n になっちゃう
  compressed_code = compressed_code.replace(b"\x00", b"\\0").replace(b"\x0d", b"\\r")

  if b"'" not in compressed_code and b"\n" not in compressed_code:
    sep = "'"
  elif b'"' not in compressed_code and b"\n" not in compressed_code:
    sep = '"'
  elif b'"""' not in compressed_code and not compressed_code.endswith(b'"'):
    sep = '"""'
  elif b'"""' not in compressed_code and not compressed_code.endswith(b"'"):
    sep = "'''"
  else:
    # TODO: 流石にないと思うけど末尾の " とかを消す
    compressed_code.replace(b'"""', b'\\"""')
    sep = '"""'

  res = f"#coding:latin_1\nimport zlib;exec(zlib.decompress(bytes(map(ord,{sep}".encode() + compressed_code + f"{sep}))))".encode()
  return res
# def compress_zlib_b85(code: str):
#   compressed_code = base64.b85encode(zlib.compress(code.encode(), level=9))
#   return f"import zlib;import base64;exec(zlib.decompress(base64.b85decode({compressed_code!r})))".encode()


compressors = [raw, compress]

def check_str(code: str | bytes, task):
    tmp_path = "tmp/tmp.py"
    if isinstance(code, str):
      open(tmp_path, "w").write(code)
    if isinstance(code, bytes):
      open(tmp_path, "wb").write(code)
    res = check(tmp_path, task)
    if "tmp.tmp" in sys.modules:
      del sys.modules["tmp.tmp"]
    shutil.rmtree('tmp/__pycache__', ignore_errors=True)
    return res

score = 0
accepted = 0

SLOW = ["base_yu/task002.py", "base_yu/task396.py"]

LONG = b"A" * 0x1000
if __name__ == "__main__":
  stats = []
  for i in range(1, 401):
    task = get_task(i)
    shortest = LONG
    task_stat = {
      "task": i,
      "base_path": None,
      "compressor": None,
      "length": None,
      "message": None,
      "success": False
    }
    for base_path in get_code_paths("base_*", i):
      do_check = base_path not in SLOW
      if do_check and check(base_path, task).correct != 1.0:
        continue
      
      print(base_path)
      code = strip(open(base_path).read())
      if do_check and check_str(code, task).correct != 1.0:
        print(f"{base_path}: strip failed, {check_str(code, task).message}")
        task_stat["base_path"] = base_path
        task_stat["message"] = check_str(code, task).message
        stats.append(task_stat)
        exit(1)
        continue

      a = sorted(zip([cmp(code) for cmp in compressors], compressors), key=lambda x: len(x[0]))
      print(f"{base_path}: {' / '.join(f'{cmp.__name__}->{len(code)}' for code, cmp in a)}")

      if do_check:
        for code, cmp in a:
          res = check_str(code, task)
          if res.correct != 1.0:
            print(f"[!] compression failed: {cmp.__name__}, {res.message}")
            task_stat["base_path"] = base_path
            task_stat["compressor"] = cmp.__name__
            task_stat["message"] = res.message
            stats.append(task_stat)
            exit(1)
      
      compressed = a[0][0]
      if len(compressed) < len(shortest):
        shortest = compressed
        task_stat["base_path"] = base_path
        task_stat["compressor"] = a[0][1].__name__
        task_stat["length"] = len(compressed)
        task_stat["success"] = True

    if shortest == LONG:
      print(f"[!] failed: vis/task{i:03}.png")
      task_stat["message"] = "WA"
      stats.append(task_stat)
      continue
    score += 2500 - len(shortest)
    accepted += 1
    open(f"dist/task{i:03}.py", "wb").write(shortest)
    stats.append(task_stat)

  print(f"accepted: {accepted}/400, {score=}")

  # Write stats to README
  with open("README.md", "w") as readme:
    readme.write("# Compression Stats\n\n")
    readme.write(f"Accepted: {accepted}/400\n")
    readme.write(f"Score: {score}\n\n")
    readme.write("## Task Details\n\n")
    readme.write("| Task | Success | Base | Compressor | Length | Goods | Message |\n")
    readme.write("|------|---------|------|------------|--------|-------|---------|\n")
    for stat in stats:
      task = f"{stat['task']:03}"
      success = "✅" if stat["success"] else "❌"
      base = stat["base_path"] if stat["success"] else "-"
      checker = stat["compressor"] if stat["success"] else "-"

      length = str(stat["length"]) if stat["success"] else "-"
      message = stat["message"] if not stat["success"] else "-"
      readme.write(f"| [{task}](vis/task{task}.png) | {success} | [{base}]({base}) | {checker} | [{length}](dist/task{task}.py) | [prompt](prompts/task{task}.txt) / [vis-many](vis_many/task{task}.png) | {message} |\n")

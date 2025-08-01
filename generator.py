import base64
import shutil
import sys
import zlib

from checker import check
from strip import strip
from utils import get_code_paths, get_task

def vanilla(code: str):
  return code.strip().encode()
def compress_zlib_latin_1(code: str):
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

compressors = [vanilla, compress_zlib_latin_1]

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

LONG = b"A" * 0x1000
if __name__ == "__main__":
  for i in range(1, 401):
    task = get_task(i)
    shortest = LONG
    for base_path in get_code_paths("base_*", i):
      if check(base_path, task).correct != 1.0:
        continue
      
      code = strip(open(base_path).read())
      if check_str(code, task).correct != 1.0:
        print(f"{base_path}: strip failed, {check_str(code, task)}")
        exit(1)
        continue

      a = sorted(zip([cmp(code) for cmp in compressors], compressors), key=lambda x: len(x[0]))
      print(f"{base_path}: {' / '.join(f'{cmp.__name__}->{len(code)}' for code, cmp in a)}")

      for code, cmp in a:
        res = check_str(code, task)
        if res.correct != 1.0:
          print(f"[!] compression failed: {cmp.__name__}, {res}")
          exit(1)
      
      compressed = a[0][0]
      if len(compressed) < len(shortest):
        shortest = compressed

    if shortest == LONG:
      print(f"[!] failed: vis/task{i:03}.png")
      continue
    score += 2500 - len(shortest)
    accepted += 1
    open(f"dist/task{i:03}.py", "wb").write(shortest)
  print(f"accepted: {accepted}/400, {score=}")

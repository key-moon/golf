from ast import literal_eval
import bz2
import lzma
import time
from typing import Tuple
import zlib
import zopfli

import warnings
import hashlib
import os

import zopfli.zlib

warnings.filterwarnings("ignore", category=SyntaxWarning)

# [
#   b'\\"', b"\\'", b'\\0', b'\\1', b'\\2', b'\\3', b'\\4', b'\\5', b'\\6', b'\\7',
#   b'\\N', b'\\U', b'\\a', b'\\b', b'\\f', b'\\n', b'\\r', b'\\t', b'\\u', b'\\v', b'\\x'
# ]
should_escapes = []
for i in range(1, 256):
  if i == ord("\\") or i == ord("\n") or i == ord("\r"):
    continue
  orig = "\\" + chr(i)
  s = "'''" + orig + "'''"
  try:
   if orig != literal_eval(s):
     should_escapes.append(orig.encode())
  except:
    should_escapes.append(orig.encode())

DOUBLE_ESCAPE_PLACEHOLDER = b"%%DOUBLE_ESCAPE%%"

def check_lit(lit: bytes, b: bytes):
  try:
    evaluated = bytes(map(ord,literal_eval(lit.decode(encoding="L1"))))
    if evaluated != b:
      print(f"[!] failed to create embed str {lit,b=} {evaluated=}")
      input("> ")
      assert False
  except Exception as e:
    print(f"[!] failed to create embed str {lit,b=}\n{e=}")
    input("> ")
    assert False

# TODO: 文字列を途中で分割して別の区切り文字を使うようにするとか r"" とか
def get_embed_str(b: bytes):
  orig = b
  # TODO: これ "\\" -> "\\\" にするほうが効率いいかもという気はする 考慮することが多くなってかなり嫌だが
  #       "\"*n -> "\"*(2n-1) かな
  b = b.replace(b"\\\\", DOUBLE_ESCAPE_PLACEHOLDER)
  
  for should_escape in should_escapes:
    b = b.replace(should_escape, b"\\" + should_escape)

  # null byte を \0 に置換したとき、\01 みたいなのが間違って解釈されるのを防ぐ
  for i in range(8):
    b = b.replace(b"\\\x00" + f"{i}".encode(), b"\\\\\\000" + f"{i}".encode())
    b = b.replace(b"\x00" + f"{i}".encode(), b"\\000" + f"{i}".encode())
  
  b = b.replace(b"\\\x00", b"\\\\\\0").replace(b"\x00", b"\\0")
  b = b.replace(b"\\\r", b"\\\\\\r").replace(b"\r", b"\\r")
  
  if b[-1] == b'\\'[0]:
    b += b'\\'

  # \r はなんかパースされたあとに \n になっちゃう
  l: list[bytes] = []
  for sep in (b"'", b'"', b"'''", b'"""'):
    if len(sep) == 1:
      t = b.replace(b'\\\n', b'\\\\\\n').replace(b'\n', b'\\n') \
           .replace(sep, b'\\'+sep) \
           .replace(DOUBLE_ESCAPE_PLACEHOLDER, b"\\\\\\\\")
      l.append(sep + t + sep)
      check_lit(sep + t + sep, orig)
    else:
      # TODO: 流石にないと思うけど """ とかを消す
      if sep in b: continue
      t = b.replace(b'\\\n', b'\\\\\n') \
           .replace(DOUBLE_ESCAPE_PLACEHOLDER, b"\\\\\\\\")
      t = t[:-1] + b'\\' + t[-1:] if t.endswith(sep[:1]) else t
      l.append(sep + t + sep)
      check_lit(sep + t + sep, orig)
  res = min(l, key=len)
  return res


CACHE_DIR = os.path.join(os.path.dirname(__file__), ".cache")
def slow_cache_decorator(cache_dir: str = CACHE_DIR, cache_threshold=0.5):
  def decorator(func):
    def wrapper(val: bytes, *args, **kwargs):
      sha1_hash = hashlib.sha1(val).hexdigest()
      subdir = os.path.join(cache_dir, sha1_hash[:2])
      os.makedirs(subdir, exist_ok=True)

      cache_path = os.path.join(subdir, sha1_hash[2:])
      if os.path.exists(cache_path):
        with open(cache_path, "rb") as f:
          return f.read()
      else:
        t = time.time()
        result = func(val, *args, **kwargs)
        took = time.time() - t
        if cache_threshold < took:
          with open(cache_path, "wb") as f:
            f.write(result)
        return result
    return wrapper
  return decorator

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "zopfli"))
def cached_zopfli(val: bytes):
  return zopfli.zlib.compress(val, numiterations=50)[2:-4]

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "lzma"))
def cached_lzma(val: bytes):
  a = lzma.compress(val, lzma.FORMAT_ALONE, preset=9 | lzma.PRESET_EXTREME)
  return a

# オーバーヘッド: 61 or 65 byte ('"' と '"""'の差)
# '#coding:L1;import zlib;exec(zlib.decompress("""...""".encode("L1")))'
# 他テンプレート案
# '#coding:L1;import zlib;exec(zlib.decompress(bytes(map(ord,"""..."""))))'
# '#coding:L1;import zlib;a=zlib.open(__file__);a._fp.seek(??);exec(a.read());"""..."""'
# '#coding:L1;import zlib;exec(zlib.decompress(open(__file__,"rb").read()[??:??]))"""..."""'
def compress(code: str, force_compress=False) -> Tuple[str, bytes]:
  compressions = [
    ("zlib", lambda x: zlib.compress(x, level=9, wbits=-9), ",-9"),
    ("zlib-15", lambda x: zlib.compress(x, level=9, wbits=-15), ",-15"),
    ("zlib-zopfli", lambda x: cached_zopfli(x), ",-15"),
    ("lzma", lambda x: cached_lzma(x),""),
    ("bz2", lambda x: bz2.compress(x, compresslevel=9),""),
  ]
  l = []
  if not force_compress:
    l.append(("raw",code.encode()))
  for name, cmp, extra_args in compressions:
    lib_name = name.split("-")[0]
    compressed_code = cmp(code.encode())
    embed = get_embed_str(compressed_code)
    # res = f"#coding:L1\nimport {lib_name};exec({lib_name}.decompress(bytes(map(ord,".encode() + embed + b"))" + extra_args.encode() + b"))"
    res = f"#coding:L1\nimport {lib_name};exec({lib_name}.decompress(".encode() + embed + b".encode('L1')" + extra_args.encode() + b"))"
    l.append((name,res))
  return min(l, key=lambda x: len(x[1]))

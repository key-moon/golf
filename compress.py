from ast import literal_eval
import bz2
import lzma
import secrets
from typing import Tuple
import zlib

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

print(should_escapes)

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


# オーバーヘッド: 64 or 68 byte ('"' と '"""'の差)
# '#coding:L1;import zlib;exec(zlib.decompress(bytes(map(ord,"""..."""))))'
# 他テンプレート案
# '#coding:L1;import zlib;exec(zlib.decompress(open(__file__,"rb").read()[??:??]))"""..."""'
# '#coding:L1;import zlib;a=zlib.open(__file__);a._fp.seek(??);exec(a.read());"""..."""'
def compress(code: str, force_compress=False) -> Tuple[str, bytes]:
  compressions = [
    ("zlib", lambda x: zlib.compress(x, level=9, wbits=-9), ",-9"),
    ("zlib-15", lambda x: zlib.compress(x, level=9, wbits=-15), ",-15"),
    ("lzma", lambda x: lzma.compress(x, lzma.FORMAT_ALONE),""),
    ("bz2", lambda x: bz2.compress(x, compresslevel=9),""),
  ]
  l = []
  if not force_compress:
    l.append(("raw",code.encode()))
  for name, cmp, extra_args in compressions:
    lib_name = name.split("-")[0]
    compressed_code = cmp(code.encode())
    embed = get_embed_str(compressed_code)
    res = f"#coding:L1\nimport {lib_name};exec({lib_name}.decompress(bytes(map(ord,".encode() + embed + b"))" + extra_args.encode() + b"))"
    l.append((name,res))
  return min(l, key=lambda x: len(x[1]))

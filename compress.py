import bz2
import lzma
from typing import Tuple
import zlib

def get_embed_str(b: bytes):
  # TODO: r"" とか使うとマシになったりするかも
  b = b.replace(b"\\", b"\\\\")
  # null byteはソースコードに入れられない null byte を \0 に置換したとき、\01 みたいなのが間違って解釈されるのを防ぐ
  for i in range(8): b = b.replace(b"\x00" + f"{i}".encode(), b"\\000" + f"{i}".encode())
  # \r はなんかパースされたあとに \n になっちゃう
  b = b.replace(b"\x00", b"\\0").replace(b"\x0d", b"\\r")

  l = []
  for sep in (b"'", b'"', b"'''", b'"""'):
    if len(sep) == 1:
      l.append(sep + b.replace(b'\n', b'\\n').replace(sep, b"\\"+sep) + sep)
    else:
      # TODO: 流石にないと思うけど """ とかを消す
      l.append(sep + (b[:-1] + b'\\' + sep if b.endswith(sep[:1]) else b) + sep)
  return min(l, key=len)

# オーバーヘッド: 64 or 68 byte ('"' と '"""'の差)
# '#coding:L1;import zlib;exec(zlib.decompress(bytes(map(ord,""""""))))'
def compress(code: str, force_compress=False) -> Tuple[str, bytes]:
  compressions = [
    ("zlib", lambda x: zlib.compress(x, level=9, wbits=-9), ",-9"),
    ("zlib-15", lambda x: zlib.compress(x, level=9, wbits=-15), ",-15"),
    ("lzma-xz", lambda x: lzma.compress(x, lzma.FORMAT_XZ),""),
    ("lzma-alone", lambda x: lzma.compress(x, lzma.FORMAT_ALONE),""),
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
  return min(l[::-1], key=lambda x: len(x[1]))
  
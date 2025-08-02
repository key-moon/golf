import bz2
import lzma
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

def compress(code: str):
  compressions = [
    ("zlib", lambda x: zlib.compress(x, level=9)),
    ("lzma", lambda x: lzma.compress(x)),
    ("bz2", lambda x: bz2.compress(x, compresslevel=9))
  ]
  l = [("raw",code.encode())]
  for name, cmp in compressions:
    compressed_code = cmp(code.encode())
    embed = get_embed_str(compressed_code)
    res = f"#coding:latin_1\nimport {name};exec({name}.decompress(bytes(map(ord,".encode() + embed + "))))".encode()
    l.append((name,res))
  return min(l, key=lambda x: len(x[1]))
  
import zlib
def compress_zlib_repr_bytes(code):
  compressed_code = zlib.compress(code.encode(), level=9)
  print(compressed_code)
  a = compressed_code.decode("utf-16")
  print(a)
  return f"import zlib;exec(zlib.decompress({compressed_code!r}))"

s = 'あいうえお'  # BMP内の文字のみ
b = s.encode('utf-16')
print(b)
print(b[2:].decode("utf-16"))

code = """
def p(g):return[sum((g[i%3]if g[i//3][j]else[0]*3 for j in (0,1,2)),[])for i in range(9)]
""".strip()

res = compress_zlib_repr_bytes(code)

print(res)

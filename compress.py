from ast import literal_eval
import bz2
import lzma
import sys
import time
from typing import Callable, Optional, Tuple
import zlib
import zopfli

import warnings
import hashlib
import os
import subprocess
import tempfile
from io import StringIO

from deflate_optimizer.optimizer import optimize_deflate_stream
from deflate_optimizer.dump_deflate_stream import dump_deflate_stream
from deflate_optimizer.load_deflate_text import load_deflate_stream
from deflate_optimizer.enumerate_variable_occurrences import list_var_occurrences
from deflate_optimizer.variable_conflict import build_conflict_report
import zopfli.zlib

from strip import strippers
from utils import get_code_paths, openable_uri, parse_range_str, signed_str, viz_deflate_url

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
    def wrapper(val: bytes, *args, use_cache=True, **kwargs):
      sha1_hash = hashlib.sha1(val).hexdigest()
      subdir = os.path.join(cache_dir, sha1_hash[:2])
      cache_path = os.path.join(subdir, sha1_hash[2:])
      if use_cache and os.path.exists(cache_path):
        with open(cache_path, "rb") as f:
          return f.read()
      else:
        t = time.time()
        result = func(val, *args, **kwargs)
        took = time.time() - t
        if use_cache and cache_threshold < took:
          os.makedirs(subdir, exist_ok=True)
          with open(cache_path, "wb") as f:
            f.write(result)
        return result
    return wrapper
  return decorator

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "zopfli"))
def cached_zopfli(val: bytes, fast=False):
  zopfli_param = 300 if fast else 2000
  compressed = zopfli.zlib.compress(val, numiterations=zopfli_param, blocksplitting=False)[2:-4]
  compressed_splitting = zopfli.zlib.compress(val, numiterations=zopfli_param)[2:-4]
  if len(compressed_splitting) < len(compressed):
    # print(f"!! {openable_uri('no split', viz_deflate_url(compressed_splitting))} / {openable_uri('split', viz_deflate_url(compressed))}")
    compressed = compressed_splitting
  if fast:
    return compressed
  return optimize_deflate_stream(
    compressed,
    lambda x: len(get_embed_str(x)),
    num_iteration=5000,
    num_perturbation=3,
    tolerance_bit=16,
    # terminate_threshold=2 + len(val) + 1,
    seed=1234
  )


def optimize_deflate_ours(deflate: bytes, num_iter: int) -> bytes:
  text = dump_deflate_stream(deflate)
  with tempfile.NamedTemporaryFile("w", delete=False) as f:
    f.write(text)
    tmp_path = f.name
  optimizer = os.path.join(os.path.dirname(__file__), "deflate_optimizer_cpp", "optimizer")
  try:
    result = subprocess.run([optimizer, tmp_path, str(num_iter)], capture_output=True, text=True, check=True)
    optimized_text = result.stdout
    if not optimized_text.strip():
      return deflate
  finally:
    try:
      os.remove(tmp_path)
    except OSError:
      pass
  _, optimized = load_deflate_stream(StringIO(optimized_text))
  return optimize_deflate_stream(
    optimized,
    lambda x: len(get_embed_str(x)),
    num_iteration=5000,
    num_perturbation=3,
    tolerance_bit=16,
    # terminate_threshold=2 + len(val) + 1,
    seed=1234
  )

def optimize_deflate_ours2(code: bytes, deflate: bytes, num_iter: int) -> bytes:
  text = dump_deflate_stream(deflate)
  with tempfile.NamedTemporaryFile("w", delete=False) as f:
    f.write(text)
    tmp_path = f.name
  var_occs_text = list_var_occurrences(code, as_text=True, nostrip=True, include_exec=True)
  var_occs = list_var_occurrences(code, as_text=False, nostrip=True, include_exec=True)
  var_conflicts = build_conflict_report(code, var_occs, assume_preprocessed=True, as_text=True)
  with tempfile.NamedTemporaryFile("w", delete=False) as f:
    f.write(var_occs_text)
    f.write(var_conflicts)
    tmp_var_path = f.name
  
  optimizer = os.path.join(os.path.dirname(__file__), "deflate_optimizer_cpp", "variable_optimizer")
  try:
    result = subprocess.run([optimizer, tmp_path, tmp_var_path, str(num_iter), str(num_iter)], capture_output=True, text=True, check=True)
    optimized_text = result.stdout
    if not optimized_text.strip():
      return deflate
  finally:
    try:
      os.remove(tmp_path)
      os.remove(tmp_var_path)
    except OSError:
      pass
  _, optimized = load_deflate_stream(StringIO(optimized_text))

  return optimize_deflate_stream(
    optimized,
    lambda x: len(get_embed_str(x)),
    num_iteration=5000,
    num_perturbation=3,
    tolerance_bit=16,
    # terminate_threshold=2 + len(val) + 1,
    seed=1234
  )

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "zopfli_cpp"))
def cached_zopfli_ours(val: bytes, fast=False):
  zopfli_param = 300 if fast else 2000
  num_iter = 10
  compressed = zopfli.zlib.compress(val, numiterations=zopfli_param, blocksplitting=False)[2:-4]
  # compressed_splitting = zopfli.zlib.compress(val, numiterations=zopfli_param)[2:-4]
  # if len(compressed_splitting) < len(compressed):
  # compressed = compressed_splitting
  if fast:
    return compressed
  return optimize_deflate_ours(compressed, num_iter=num_iter)

def cached_zopfli_ours2(val: bytes, use_zopfli, num_iter=10, fast=False):
  zopfli_param = 300 if fast else 2000
  if use_zopfli:
    compressed = zopfli.zlib.compress(val, numiterations=zopfli_param, blocksplitting=False)[2:-4]
    # compressed_splitting = zopfli.zlib.compress(val, numiterations=zopfli_param)[2:-4]
    # if len(compressed_splitting) < len(compressed):
    # compressed = compressed_splitting
  else:
    compressed_9 = zlib.compress(val, level=9, wbits=-9)
    compressed_15 = zlib.compress(val, level=9, wbits=-15)
    compressed = compressed_9 if len(compressed_9) < len(compressed_15) else compressed_15
  if fast:
    return compressed
  return optimize_deflate_ours2(val, compressed, num_iter=num_iter)

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "zopfli_cpp_var"))
def cached_zopfli_ours_varopt_with_zopfli(val: bytes, fast=False):
  return cached_zopfli_ours2(val, use_zopfli=True, num_iter=10, fast=fast)

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "zopfli_cpp_var_no_zopfli"))
def cached_zopfli_ours_varopt_without_zopfli(val: bytes, fast=False):
  return cached_zopfli_ours2(val, use_zopfli=False, num_iter=10, fast=fast)

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "zopfli_cpp_var_slow"))
def cached_zopfli_ours_varopt_with_zopfli_slow(val: bytes, fast=False):
  return cached_zopfli_ours2(val, use_zopfli=True, num_iter=1000, fast=fast)

@slow_cache_decorator(cache_dir=os.path.join(CACHE_DIR, "lzma"))
def cached_lzma(val: bytes):
  a = lzma.compress(val, lzma.FORMAT_ALONE, preset=9 | lzma.PRESET_EXTREME)
  return a

def determine_wbits(compressed: bytes):
  try:
    zlib.decompress(compressed, wbits=-9)
    return ",-9"
  except:
    return ",-15"  

# オーバーヘッド: 60 or 64 byte ('"' と '"""'の差)
# '#coding:L1;import zlib;exec(zlib.decompress(bytes("""...""","L1")))'
# 他テンプレート案
# '#coding:L1;import zlib;exec(zlib.decompress("""...""".encode("L1")))'
# '#coding:L1;import zlib;exec(zlib.decompress(bytes(map(ord,"""..."""))))'
# '#coding:L1;import zlib;a=zlib.open(__file__);a._fp.seek(??);exec(a.read());"""..."""'
# '#coding:L1;import zlib;exec(zlib.decompress(open(__file__,"rb").read()[??:??]))"""..."""'
def compress(code: str, best: Optional[int]=None, fast=False, use_cache=True, force_compress=False) -> Tuple[str, bytes, bytes, str]:
  compressions: list[tuple[str, Callable[[bytes], bytes], Callable[[bytes], str]]] = [
    ("zlib-9", lambda x: zlib.compress(x, level=9, wbits=-9), lambda _: ",-9"),
    ("zlib", lambda x: zlib.compress(x, level=9, wbits=-15), lambda _: ",-15"),
    ("zlib-zopfli", lambda x: cached_zopfli(x, fast, use_cache=use_cache), determine_wbits),
    ("zlib-zopfli-cpp", lambda x: cached_zopfli_ours(x, fast, use_cache=use_cache), determine_wbits),
    ("zlib-zopfli-cpp-var-zopfli", lambda x: cached_zopfli_ours_varopt_with_zopfli(x, fast, use_cache=use_cache), determine_wbits),
    ("zlib-zopfli-cpp-var-nozopfli", lambda x: cached_zopfli_ours_varopt_without_zopfli(x, fast, use_cache=use_cache), determine_wbits),
    # ("zlib-zopfli-cpp-var-zopfli-slow", lambda x: cached_zopfli_ours_varopt_with_zopfli_slow(x, fast, use_cache=use_cache), determine_wbits), # 時間かけてたくさんイテレーションを回すやつ
    ("lzma", lambda x: cached_lzma(x),lambda _: ""),
    ("bz2", lambda x: bz2.compress(x, compresslevel=9),lambda _: ""),
  ]
  l = []
  worth_compress = True
  if not force_compress:
    if best is None:
      best = len(code)
    compressed_length = len(zlib.compress(code.encode()))
    if 1000 < len(code):
      compressed_length = min(compressed_length, len(cached_lzma(code.encode())))
    worth_compress = (60 - (15 if compressed_length < 400 else 30)) <= (best - compressed_length)
    l.append(("raw", code.encode(), "", "" if worth_compress else "not worth compress"))
  
  if worth_compress:
    for name, cmp, extra_args_fun in compressions:
      lib_name = name.split("-")[0]
      raw_compressed = cmp(code.encode())
      embed = get_embed_str(raw_compressed)

      extra_overhead = len(embed) - (len(raw_compressed) + 2)

      extra_args = extra_args_fun(raw_compressed)
      res = f"#coding:L1\nimport {lib_name}\nexec({lib_name}.decompress(bytes(".encode() + embed + b",'L1')" + extra_args.encode() + b"))"

      message = "" if extra_overhead == 0 else f"encode:{signed_str(extra_overhead)}"
      l.append((name, res, raw_compressed, message))

  mn = min(l, key=lambda x: len(x[1]))
  return mn

def get_uncompressed_content(content: bytes) -> tuple[str, bytes | None]:
  if b".decompress(" in content:
    try:
      lib = content.split(b"\n")[1].split(b";")[0][len(b"import "):].decode()
      compressor = __import__(lib)
      start_idx = content.index(b"bytes(") + len(b"bytes(")
      end_idx = content.index(b",'L1'")
      payload = literal_eval(content[start_idx:end_idx].decode("L1")).encode("L1")
      if lib == "zlib":
        return compressor.decompress(payload, -15).decode(), payload
      else:
        return compressor.decompress(payload).decode(), payload
    except Exception as e:
      return "# failed to decompress", None
  else:
    try:
      return content.decode(), None
    except Exception:
      return "# failed to decode", None

def get_content_summary(content: bytes) -> str:
  code, deflate_payload = get_uncompressed_content(content)
  if deflate_payload:
    res = ""
    res += f"# before compress: {len(code)} bytes\n"
    res += code.replace("\t", " ")
    return res
  else:
    return content.decode("L1")

if __name__ == "__main__":
  dirname = sys.argv[1] if 2 <= len(sys.argv) else "dist"
  range_str = sys.argv[2] if 3 <= len(sys.argv) else "1-400"
  
  r = parse_range_str(range_str)

  print(f"{dirname=}")
  for i in r:
    for code_path in get_code_paths(dirname, i):
      if not os.path.exists(code_path): continue
      orig_code = open(code_path, "rb").read()
      code, deflate_payload = get_uncompressed_content(orig_code)

      if b"zlib.decompress" in orig_code and deflate_payload:
        sha1_hash = hashlib.sha1(code.encode()).hexdigest()
        cache_path = f".cache/zopfli/{sha1_hash[:2]}/{sha1_hash[2:]}"
        print(f"[+] orig len: {len(orig_code)} / raw deflate: {len(deflate_payload)} / unpacked len({openable_uri('viz', viz_deflate_url(deflate_payload))}): {len(code)}")
        if os.path.exists(cache_path):
          print(f"[+] cache exists(len: {len(open(cache_path, 'rb').read())}): {cache_path}")
      else:
        print(f"[+] len: {len(orig_code)}")
      for stripper, strip in strippers.items():
        code = strip(code)
        comp_name, compressed, raw, compress_msg = compress(code, use_cache=False)
        res_msg = f" - {stripper=} / {comp_name=}: {len(compressed)}"
        if comp_name.startswith("zlib"):
          res_msg += f" ({openable_uri('viz', viz_deflate_url(raw))})"
        if compress_msg:
          res_msg += f" ({compress_msg})"
        print(res_msg)

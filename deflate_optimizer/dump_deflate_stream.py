# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from io import StringIO
import glob
import os

import zopfli.zlib
import strip
from bitio import BitReader
from blocks import Block


def dump_deflate_stream(deflated_bytes: bytes) -> str:
  tw = StringIO()
  reader = BitReader(deflated_bytes)
  blocks = []
  while not blocks or not blocks[-1].bfinal:
    blocks.append(Block.load(reader))
    blocks[-1].dump_string(tw)
  return tw.getvalue()

if __name__ == '__main__':
  ZOPFLI_NUM_ITER = 1000
  BLOCKSPLITTING=False
  OPTIMIZER_NUM_ITER = 2000

  for path in glob.glob('data/compeval/*/*.py'):
    new_path = path.replace("data/compeval", "./tmp/ziptext", 1)
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    print(f'--- {path} ---')
    code = open(path, "rb").read()
    plain = strip.strip_for_zlib(code).encode()
    deflate = zopfli.zlib.compress(plain, numiterations=ZOPFLI_NUM_ITER, blocksplitting=BLOCKSPLITTING)[2:-4]
    # if len(plain) <= len(deflate) + 10: continue # cut-off
    text = dump_deflate_stream(deflate)
    with open(new_path + '.deflated', 'wb') as f:
      f.write(deflate)
    with open(new_path + '_deflated.txt', 'w') as f:
      f.write(text)

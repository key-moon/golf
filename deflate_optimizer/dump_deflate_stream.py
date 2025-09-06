# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import StringIO

import zopfli.zlib
from compress import get_embed_str
from deflate_optimizer.optimizer import optimize_deflate_stream
# from deflate_optimizer import optimize_deflate_stream
from utils import get_code_paths, openable_uri, viz_deflate_url
import strip
import zlib
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

  for i in range(1, 401):
    print(get_code_paths("base_*", i))
    for base_path in get_code_paths("base_*", i):
      if "arc" in base_path: continue
      code = open(base_path, "rb").read()
      plain = strip.strip_for_zlib(code).encode()
      deflate = zopfli.zlib.compress(plain, numiterations=ZOPFLI_NUM_ITER, blocksplitting=BLOCKSPLITTING)[2:-4]
      if len(plain) <= len(deflate) + 10: continue # cut-off
      # if len(plain) <= len(deflate) + 81: continue
      print(dump_deflate_stream(deflate))

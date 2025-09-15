# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+
# Usage:  python3 -m deflate_optimizer.load_deflate_text <path_to_deflate_dumped_text>

from __future__ import annotations
from io import StringIO
import glob
import os
import sys
import base64

from .bitio import BitWriter
from .blocks import Block
from .blocks.stored import StoredBlock
from .blocks.fixed_huffman import FixedHuffmanBlock
from .blocks.dynamic_huffman import DynamicHuffmanBlock
from utils import viz_deflate_url


def load_deflate_stream(tw: StringIO) -> bytes:
  writer = BitWriter()
  while True:
    block = Block.load_from_text(tw)
    block.dump(writer)
    if block.bfinal:
      break
  return writer.num_written_bits(), writer.get_bytes()


if __name__ == '__main__':
  path = None
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    print(f'Usage: python3 -m deflate_optimizer.load_deflate_text <path_to_deflate_dumped_text>', file=sys.stderr)
    sys.exit(1)
  
  with open(path, 'r') as f:
    text = f.read()
    tw = StringIO(text)
    cnt, b = load_deflate_stream(tw)
    print()
    print(f'Raw deflate bytes (base64): {base64.b64encode(b).decode()}')
    print(f'total bit length : {cnt}')
    print(f'total byte length: {len(b)}')
    print(f'deflate URL: {viz_deflate_url(b)}')

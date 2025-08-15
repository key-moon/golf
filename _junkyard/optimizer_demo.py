# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

import zopfli.zlib
from compress import get_embed_str
from deflate_optimizer import DynamicHuffmanBlock, optimize_deflate_stream, BitReader, BitWriter, Block
from utils import get_code_paths, openable_uri, viz_deflate_url
import strip
import zlib

for i in range(1, 401):
  for base_path in get_code_paths("base_*", i):
    code = open(base_path, "rb").read()
    plain = strip.strip_for_zlib(code).encode()
    if 2000 <= len(code): continue
    deflate = zopfli.zlib.compress(plain)[2:-4]
    print(base_path)
    optimized = optimize_deflate_stream(
        deflate,
        lambda x: len(get_embed_str(x)),
        num_iteration=5000,
        num_perturbation=3,
        tolerance_bit=16,
        terminate_threshold=2 + len(deflate) + 1,
        seed=1234,
        verbose=True
    )
    assert zlib.decompress(optimized, wbits=-15) == plain

if __name__ == "__main__":
    import zlib, os
    plain = open("base_arcdsl/task002.py~retire", "rb").read()
    print(openable_uri("plain", viz_deflate_url(plain)))
    # wbits=-15 で raw deflate
    deflate = zopfli.zlib.compress(plain)[2:-4]
    assert zlib.decompress(deflate, wbits=-15) == plain
    
    reader = BitReader(deflate)
    blocks: list[Block] = []
    while not blocks or not blocks[-1].bfinal:
        blocks.append(Block.load(reader))

    assert isinstance(blocks[0], DynamicHuffmanBlock)

    w = BitWriter()
    # for b in blocks:
    #     b.dump(w)
    # assert zlib.decompress(w.get_bytes(), wbits=-15) == plain

    optimized = optimize_deflate_stream(
        deflate,
        lambda x: len(get_embed_str(x)),
        num_iteration=5000,
        num_perturbation=3,
        tolerance_bit=16,
        terminate_threshold=2 + len(deflate) + 1,
        seed=1234,
        verbose=True
    )

    assert zlib.decompress(optimized, wbits=-15) == plain

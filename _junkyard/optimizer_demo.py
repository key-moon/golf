# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

import zopfli.zlib
from compress import get_embed_str
from deflate_optimizer import DynamicHuffmanBlock, optimize_deflate_stream, BitReader, BitWriter, Block
from utils import openable_uri, viz_deflate_url

if __name__ == "__main__":
    import zlib, os
    plain = open("base_arcdsl/task002.py~retire", "rb").read()
    print(openable_uri("plain", viz_deflate_url(plain)))
    # wbits=-15 で raw deflate
    deflate = zopfli.zlib.compress(plain)[2:-4]
    assert zlib.decompress(deflate, wbits=-15) == plain
    forb = [0x00, 0x0a]
    def score(data: bytes) -> int:
        s = len(data)
        for b in data:
            if b in forb:
                s += 1
        return s
    
    reader = BitReader(deflate)
    blocks: list[Block] = []
    while not blocks or not blocks[-1].bfinal:
        blocks.append(Block.load(reader))

    assert isinstance(blocks[0], DynamicHuffmanBlock)
    print(blocks[0].header.cl_code.lengths)
    print(blocks[0].header.litlen_code.lengths)
    print(blocks[0].header.dist_code.lengths)

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

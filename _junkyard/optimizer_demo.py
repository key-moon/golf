# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

import zopfli.zlib
from compress import get_embed_str
from deflate_optimizer.optimizer import optimize_deflate_stream
# from deflate_optimizer import optimize_deflate_stream
from utils import get_code_paths, openable_uri, viz_deflate_url
import strip
import zlib

ZOPFLI_NUM_ITER = 1000
BLOCKSPLITTING=False
OPTIMIZER_NUM_ITER = 2000

total_length = 0
initial_losses = []
losses = []
for i in range(1, 401):
  for base_path in get_code_paths("base_*", i):
    if "arc" in base_path: continue
    code = open(base_path, "rb").read()
    plain = strip.strip_for_zlib(code).encode()
    deflate = zopfli.zlib.compress(plain, numiterations=ZOPFLI_NUM_ITER, blocksplitting=BLOCKSPLITTING)[2:-4]
    if len(code) <= len(deflate) + 81: continue
    optimal_len = len(deflate) + 3

    optimized = optimize_deflate_stream(
        deflate,
        lambda x: len(get_embed_str(x)),
        num_iteration=OPTIMIZER_NUM_ITER,
        num_perturbation=3,
        tolerance_bit=16,
        # terminate_threshold=optimal_len,
        seed=1234,
        verbose=True
    )
    # assert zlib.decompress(optimized, wbits=-15) == plain, base_path
    
    diff = len(get_embed_str(optimized)) - optimal_len
    print(f"{'✅' if diff == 0 else '❌'}: {base_path} (+{diff}, {openable_uri('orig', viz_deflate_url(deflate))}, {openable_uri('optimized', viz_deflate_url(optimized))})")
    losses.append(diff)
    initial_losses.append(len(get_embed_str(deflate)) - optimal_len)
    total_length += len(deflate)


"""
params: ZOPFLI_NUM_ITER=1000 blocksplitting=False OPTIMIZER_NUM_ITER=2000
         total: 215 cases / 35135 chars
  initial loss: 257 (0.007314643517859684 loss per char)
optimized loss: 10 (0.00028461647929415115 loss per char)
"""



"""
params: ZOPFLI_NUM_ITER=1000 blocksplitting=True OPTIMIZER_NUM_ITER=2000
         total: 215 cases / 35148 chars
  initial loss: 296 (0.008421531808353248 loss per char)
optimized loss: 38 (0.0010811425970183226 loss per char)
"""

print(f"params: {ZOPFLI_NUM_ITER=} {BLOCKSPLITTING=} {OPTIMIZER_NUM_ITER=}")
print(f"         total: {len(losses)} cases / {total_length} chars")
print(f"  initial loss: {sum(initial_losses)} ({sum(initial_losses) / total_length} loss per char)")
print(f"optimized loss: {sum(losses)} ({sum(losses) / total_length} loss per char)")

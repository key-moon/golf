from collections import defaultdict
from dataclasses import dataclass
import random
from typing import Callable, Optional

from deflate_optimizer.huffman import is_valid_huffman_lengths
from . import Block, DynamicHuffmanBlock, DynamicHuffmanHeader, LitToken, MatchToken, Token , _length_to_code_and_extra_for_dump, _distance_to_code_and_extra_for_dump, build_header_from_lengths
from .bitio import BitReader, BitWriter, dumps


def perturb_swap(lengths: list[int], rng: random.Random) -> None:
    idxs = [i for i, l in enumerate(lengths) if l > 0]
    if len(idxs) < 2: return
    i, j = rng.sample(idxs, 2)
    lengths[i], lengths[j] = lengths[j], lengths[i]

def perturb_add_dummy_adjacent(lengths: list[int], rng: random.Random, maxbits: int = 15) -> None:
    if not any(lengths): return
    maxlen = max(l for l in lengths)
    cands = [i for i, l in enumerate(lengths) if l == maxlen]
    if not cands: return
    i = rng.choice(cands)
    if lengths[i] < maxbits:
        lengths[i] += 1
    j = i + rng.choice([-1, 1])
    if 0 <= j < len(lengths) and lengths[j] == 0:
        lengths[j] = min(maxbits, lengths[i])

def random_perturb_lengths(litlen: list[int], dist: list[int], num: int, rng: random.Random) -> tuple[list[int], list[int]]:
    l = list(litlen); d = list(dist)
    for _ in range(num):
        if rng.random() < 0.6:
            if rng.random() < 0.5: perturb_swap(l, rng)
            else: perturb_add_dummy_adjacent(l, rng, 15)
        else:
            if rng.random() < 0.5: perturb_swap(d, rng)
            else: perturb_add_dummy_adjacent(d, rng, 15)
    return l, d

def _collect_usage(tokens: list[Token]) -> tuple[dict[int, int], dict[int, int], int]:
    token_usage = defaultdict(lambda: 0, { 256: 1 }) 
    dist_usage = defaultdict(lambda: 0)
    extrabits = 0
    for t in tokens:
        if isinstance(t, LitToken):
            token_usage[t.lit] = token_usage[t.lit] + 1
        else:
            assert isinstance(t, MatchToken)
            l_code, _, l_extrabits = _length_to_code_and_extra_for_dump(t.length)
            token_usage[l_code] = token_usage[l_code] + 1; extrabits += l_extrabits
            d_code, _, d_extrabits = _distance_to_code_and_extra_for_dump(t.distance)
            dist_usage[d_code] = dist_usage[d_code] + 1; extrabits += d_extrabits
    return dict(token_usage), dict(dist_usage), extrabits

@dataclass
class OptimizeResult:
    best_block: Block
    best_bits: int
    best_score: int
    tried: int
    accepted: int

def _huffmanheader_bits(header: DynamicHuffmanHeader):
    writer = BitWriter()
    header.dump(writer)
    return len(writer._buf) + writer._bitcnt

def _total_bits_from_usage(huffman_lengths: list[int], usage: dict[int, int]):
    res = 0
    for key, count in usage.items():
        if len(huffman_lengths) <= key or huffman_lengths[key] == 0:
            return 1 << 60 # inf
        res += count * huffman_lengths[key]
    return res

ScoreFunc = Callable[[bytes], int]

def optimize_deflate_block(
    base_block: DynamicHuffmanBlock,
    score_func: ScoreFunc,
    prefix_bits: BitWriter=BitWriter(),
    suffix_bits: BitWriter=BitWriter(),
    num_iteration: int = 3000,
    num_perturbation: int = 3,
    tolerance_bit: int = 16,
    terminate_threshold: int=0,
    seed: Optional[int] = None,
) -> OptimizeResult:
    rng = random.Random(seed)
    base_bytes = dumps(base_block)
    base_score = score_func(base_bytes)

    litlen_usage, dist_usage, extra_bits = _collect_usage(base_block.tokens)
    def estimate_block_bits(header: DynamicHuffmanHeader):
        bits  = 0
        bits += extra_bits
        bits += _huffmanheader_bits(header)
        bits += _total_bits_from_usage(header.dist_code.lengths, dist_usage)
        bits += _total_bits_from_usage(header.litlen_code.lengths, litlen_usage)
        return bits
    
    base_bits = estimate_block_bits(base_block.header)
    best_block = base_block
    best_bits  = base_bits
    best_score = base_score

    tried = 0
    accepted = 0
    for _ in range(num_iteration):
        if best_score <= terminate_threshold:
            break

        new_lit, new_dist = random_perturb_lengths(base_block.header.litlen_code.lengths, base_block.header.dist_code.lengths, num_perturbation, rng)
        # 採用条件の例
        if not is_valid_huffman_lengths(new_lit, 15): continue
        if not is_valid_huffman_lengths(new_dist, 15): continue
        tried += 1

        header = build_header_from_lengths(new_lit, new_dist)

        est_bits = estimate_block_bits(header)
        if est_bits - base_bits > tolerance_bit:
            continue

        # 候補ブロック（bfinal は元を継承）
        cand_block = DynamicHuffmanBlock(bfinal=base_block.bfinal, header=header, tokens=base_block.tokens)

        res = (prefix_bits | BitWriter(cand_block) | suffix_bits)
        # res = (prefix_bits | BitWriter(cand_block))

        # すでに決定されてるbufferだけ用いたい
        sc = score_func(res.get_bytes())
        accepted += 1
        if (sc < best_score) or (sc == best_score and est_bits < best_bits):
            best_score = sc
            best_block = cand_block
            best_bits  = est_bits

    return OptimizeResult(
        best_block=best_block,
        best_bits=best_bits,
        best_score=best_score,
        tried=tried,
        accepted=accepted,
    )

def optimize_deflate_stream(
    deflate_stream: bytes,
    score_func: ScoreFunc,
    num_iteration: int = 3000,
    num_perturbation: int = 3,
    tolerance_bit: int = 16,
    terminate_threshold=0,
    seed: Optional[int] = None,
    verbose=False
) -> bytes:
    reader = BitReader(deflate_stream)
    blocks: list[Block] = []
    while not blocks or not blocks[-1].bfinal:
        blocks.append(Block.load(reader))

    res = BitWriter()
    for i, block in enumerate(blocks):
        if isinstance(block, DynamicHuffmanBlock):
            block_bytes = dumps(block)
            if verbose: print(f"[block#{i}] initial_length={len(block_bytes)} initial_score={score_func(block_bytes)}")
            prefix = BitWriter(res._bitbuf, res._bitcnt)
            suffix = BitWriter()
            # if not block.bfinal:
            #     suffix.write_bytes(dumps(blocks[i + 1])[:1])
            r = optimize_deflate_block(
                block,
                prefix_bits=prefix,
                suffix_bits=suffix,
                score_func=score_func,
                num_iteration=num_iteration,
                num_perturbation=num_perturbation,
                tolerance_bit=tolerance_bit,
                terminate_threshold=terminate_threshold,
                seed=seed,
            )
            r.best_block.dump(res)
            if verbose: print(f"[block#{i}] tried={r.tried} accepted={r.accepted} best_score={r.best_score} bits~={r.best_bits}")
        else:
            if verbose: print(f"[block#{i}] Skipped (not DynHuffman)")
            block.dump(res)
    return res.get_bytes()

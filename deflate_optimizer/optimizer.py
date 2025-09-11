from collections import defaultdict
from dataclasses import dataclass
import math
import random
from typing import Callable, Optional

from deflate_optimizer.blocks import Block, LitToken, MatchToken, Token
from deflate_optimizer.blocks.dynamic_huffman import CL_ORDER, DynamicHuffmanBlock, DynamicHuffmanCodeLengthCode, DynamicHuffmanHeader, rle_code_lengths_stream, rle_code_lengths_stream_greedy
from deflate_optimizer.blocks.huffman import distance_to_code_and_extra, length_to_code_and_extra
from deflate_optimizer.huffman import FastHuffman, is_valid_huffman_lengths
from deflate_optimizer.rle_dp_helper import RLE_DP_TABLE
from .bitio import BitReader, BitWriter, dumps

def hclen_from_cl_lengths(cl_lengths: list[int]) -> int:
    last = -1
    for i in range(len(CL_ORDER)-1, -1, -1):
        if cl_lengths[CL_ORDER[i]] != 0:
            last = i; break
    if last < 0: last = 0
    return max(0, (last + 1) - 4)

def kraft_overflow(lengths: list[int]) -> bool:
    total = 0.0
    for l in lengths:
        if l > 0:
            total += 1.0 / (1 << l)
            if total > 1.0 + 1e-12:
                return True
    return False

def fix_lengths_kraft(lengths: list[int], maxbits: int):
    lens = list(lengths)
    while kraft_overflow(lens):
        cands = [(l, i) for i, l in enumerate(lens) if 0 < l < maxbits]
        if not cands:
            raise ValueError("Cannot satisfy Kraft inequality within maxbits")
        cands.sort()
        extended = False
        for l, idx in cands:
            lens[idx] = l + 1
            if not kraft_overflow(lens):
                extended = True
                break
            lens[idx] = l
        if not extended:
            l, idx = cands[0]
            lens[idx] = min(maxbits, l + 1)
    return lens

def lengths_from_freq(freqs: list[int], maxbits: int) -> list[int]:
    import heapq
    n = len(freqs)
    nodes = [(f, i) for i, f in enumerate(freqs) if f > 0]
    lens = [0]*n
    if not nodes:
        return lens
    if len(nodes) == 1:
        lens[nodes[0][1]] = 1
        return lens
    heap = []
    for f, i in nodes:
        heapq.heappush(heap, (f, i))
    nxt = n
    parent: dict[int,int] = {}
    while len(heap) >= 2:
        f1, a1 = heapq.heappop(heap)
        f2, a2 = heapq.heappop(heap)
        nid = nxt; nxt += 1
        parent[a1] = nid; parent[a2] = nid
        heapq.heappush(heap, (f1+f2, nid))
    for _, i in nodes:
        d = 0; cur = i
        while cur in parent:
            d += 1; cur = parent[cur]
        lens[i] = d
    for i, l in enumerate(lens):
        if l > maxbits: lens[i] = maxbits
    lens = fix_lengths_kraft(lens, maxbits)
    return lens

def _last_nonzero_index(a: list[int]) -> int:
    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            return i
    return -1

def build_header_from_lengths(
    litlen_lengths: list[int],
    dist_lengths: list[int],
    cl_lengths: list[int],
):
    l_last = _last_nonzero_index(litlen_lengths)
    d_last = _last_nonzero_index(dist_lengths)
    num_litlen = max(l_last + 1, 257)
    num_dist   = max(d_last + 1, 1)
    litlen_lengths, dist_lengths = litlen_lengths[:num_litlen], dist_lengths[:num_dist]
    hlit  = num_litlen - 257
    hdist = num_dist   - 1

    # TODO: 律動はこっちに加えてもよいかも
    # 前iterationで使ったcl_lengthsを使って再度DPでRLE決定
    rle_stream = RLE_DP_TABLE.rle_code_lengths_stream(litlen_lengths, dist_lengths, cl_lengths)

    # CL 頻度 → 制限長ハフマン（max=7）
    cl_freq = [0]*19
    for sym,_,_ in rle_stream:
        cl_freq[sym] += 1
    cl_lengths_raw = lengths_from_freq(cl_freq, maxbits=7)

    # HCLEN 決定
    hclen = hclen_from_cl_lengths(cl_lengths_raw)

    # マスク（宣言範囲外は 0）
    active = set(CL_ORDER[:hclen + 4])
    cl_lengths = [ (cl_lengths_raw[i] if i in active else 0) for i in range(19) ]

    return DynamicHuffmanHeader(
        hlit,
        hdist,
        hclen,
        DynamicHuffmanCodeLengthCode(cl_lengths),
        FastHuffman(litlen_lengths),
        FastHuffman(dist_lengths)
    )

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
        if rng.random() < 0.65:
            perturb_swap(l, rng)
            # if rng.random() < 0.5: perturb_swap(l, rng)
            # else: perturb_add_dummy_adjacent(l, rng, 15)
        else:
            perturb_swap(d, rng)
            # if rng.random() < 0.5: perturb_swap(d, rng)
            # else: perturb_add_dummy_adjacent(d, rng, 15)
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
            l_code, _, l_extrabits = length_to_code_and_extra(t.length)
            token_usage[l_code] = token_usage[l_code] + 1; extrabits += l_extrabits
            d_code, _, d_extrabits = distance_to_code_and_extra(t.distance)
            dist_usage[d_code] = dist_usage[d_code] + 1; extrabits += d_extrabits
    return dict(token_usage), dict(dist_usage), extrabits

@dataclass
class OptimizeResult:
    best_block: DynamicHuffmanBlock
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
    best_score = base_score

    best_bits  = base_bits
    bestbits_litlen, bestbits_dist = base_block.header.litlen_code.lengths, base_block.header.dist_code.lengths

    tried = 0
    accepted = 0
    while terminate_threshold < best_score and tried < num_iteration:
        new_litlen, new_dist = random_perturb_lengths(bestbits_litlen, bestbits_dist, num_perturbation, rng)

        if not is_valid_huffman_lengths(new_litlen, 15): continue
        if not is_valid_huffman_lengths(new_dist, 15): continue

        tried += 1
        header = build_header_from_lengths(new_litlen, new_dist, best_block.header.cl_code.lengths)

        est_bits = estimate_block_bits(header)
        if est_bits - base_bits > tolerance_bit:
            continue

        cand_block = DynamicHuffmanBlock(bfinal=base_block.bfinal, header=header, tokens=base_block.tokens)

        res = (prefix_bits | BitWriter(cand_block) | suffix_bits)

        # すでに決定されてるbufferだけ用いたい
        sc = score_func(res._buf)
        accepted += 1
        if sc < best_score:
            best_score = sc
            best_block = cand_block
        if est_bits < best_bits:
            bestbits_litlen, bestbits_dist = new_litlen, new_dist
            best_bits = est_bits

    return OptimizeResult(
        best_block=best_block,
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
            if not block.bfinal:
                suffix.write_bits(dumps(blocks[i + 1])[0], 7)
            else:
                suffix.write_bits(0, 7)
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
            if verbose: print(f"[block#{i}] tried={r.tried} accepted={r.accepted} best_score={r.best_score}")
        else:
            if verbose: print(f"[block#{i}] Skipped (not DynHuffman)")
            block.dump(res)
    return res.get_bytes()

def anneal_header(base_block: DynamicHuffmanBlock, iteration=100000, seed=1234):
    rng = random.Random(seed)

    litlen_usage, dist_usage, extra_bits = _collect_usage(base_block.tokens)
    def estimate_block_bits(header: DynamicHuffmanHeader):
        bits  = 0
        bits += extra_bits
        bits += _huffmanheader_bits(header)
        bits += _total_bits_from_usage(header.dist_code.lengths, dist_usage)
        bits += _total_bits_from_usage(header.litlen_code.lengths, litlen_usage)
        return bits
    
    current_bits = estimate_block_bits(base_block.header)
    best_header = base_block.header

    best_bits = current_bits
    bestbits_litlen, bestbits_dist = base_block.header.litlen_code.lengths, base_block.header.dist_code.lengths

    tried = 0
    accepted = 0
    
    starttemp, endtemp = max(dist_usage.values()), 1

    for i in range(iteration):
        temp = starttemp + (endtemp - starttemp) * i / iteration

        new_litlen, new_dist = random_perturb_lengths(bestbits_litlen, bestbits_dist, 1, rng)

        if not is_valid_huffman_lengths(new_litlen, 15): continue
        if not is_valid_huffman_lengths(new_dist, 15): continue

        tried += 1
        header = build_header_from_lengths(new_litlen, new_dist)

        est_bits = estimate_block_bits(header)
        prob = math.exp(est_bits - current_bits)
        if prob < random.random():
            continue

        cand_block = DynamicHuffmanBlock(bfinal=base_block.bfinal, header=header, tokens=base_block.tokens)

        res = (prefix_bits | BitWriter(cand_block) | suffix_bits)

        # すでに決定されてるbufferだけ用いたい
        sc = score_func(res._buf)
        accepted += 1
        if sc < best_score:
            best_score = sc
            best_block = cand_block
        if est_bits < best_bits:
            bestbits_litlen, bestbits_dist = new_litlen, new_dist
            best_bits = est_bits

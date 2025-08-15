
# =========================================================
# Helpers for dump-time reverse mapping
# =========================================================

def _length_to_code_and_extra_for_dump(length: int) -> Tuple[int,int,int]:
    if length < 3 or length > 258:
        raise ValueError("length out of range")
    if length == 258:
        return 285, 0, 0
    for i in range(len(LEN_BASES)-1):
        base = LEN_BASES[i]; nextb = LEN_BASES[i+1]
        if base <= length < nextb:
            return 257 + i, length - base, LEN_EXTRA[i]
    return 285, 0, 0

def _distance_to_code_and_extra_for_dump(distance: int) -> Tuple[int,int,int]:
    if distance < 1 or distance > 32768:
        raise ValueError("distance out of range")
    for i in range(len(DIST_BASES)):
        base = DIST_BASES[i]
        nextb = DIST_BASES[i+1] if i+1 < len(DIST_BASES) else 1<<30
        if base <= distance < nextb:
            return i, distance - base, DIST_EXTRA[i]
    raise RuntimeError("distance mapping failed")



# ---------- 概算ビット数 ----------
def _last_nonzero_index(a: List[int]) -> int:
    for i in range(len(a)-1, -1, -1):
        if a[i] != 0: return i
    return -1

def estimate_block_bits(tokens: List["Token"], litlen_lengths: List[int], dist_lengths: List[int]) -> int:
    bits = 1 + 2  # BFINAL + BTYPE
    # HLIT/HDIST/CL + RLE
    l_last = _last_nonzero_index(litlen_lengths)
    d_last = _last_nonzero_index(dist_lengths)
    num_litlen = max(l_last + 1, 257)
    num_dist   = max(d_last + 1, 1)
    litlen_eff = (litlen_lengths[:num_litlen] + [0]*(num_litlen-len(litlen_lengths))) if len(litlen_lengths) < num_litlen else litlen_lengths[:num_litlen]
    dist_eff   = (dist_lengths[:num_dist] + [0]*(num_dist-len(dist_lengths))) if len(dist_lengths) < num_dist else dist_lengths[:num_dist]
    rle = rle_code_lengths_stream(litlen_eff, dist_eff)
    # CL は頻度から maxbits=7
    cl_freq = [0]*19
    for sym,_,_ in rle: cl_freq[sym] += 1
    cl_lengths = lengths_from_freq(cl_freq, 7)
    hclen = hclen_from_cl_lengths(cl_lengths)
    bits += 5 + 5 + 4
    bits += 3 * (hclen + 4)
    cl_table = FastHuffman(cl_lengths)  # 先読みテーブルで長さ n を得るためだけに使用
    for sym,_,extra_bits in rle:
        # code 長は dec_table 設計から復元できないので enc_map を参照
        # ただし概算なので「ビット長＝lengths[sym]」で十分
        l = cl_lengths[sym]
        if l == 0:  # HCLEN マスクの可能性→安全側で重みを足す
            return 1 << 60
        bits += l + extra_bits

    # 本体（リテラル / 長さ / 距離）
    lit_lens  = litlen_eff
    dist_lens = dist_eff
    for t in tokens:
        if isinstance(t, LitToken):
            l = lit_lens[t.lit] if t.lit < len(lit_lens) else 0
            if l <= 0: return 1 << 60
            bits += l
        else:
            lcode, _, lbits = _length_to_code_and_extra_for_dump(t.length)
            l = lit_lens[lcode] if lcode < len(lit_lens) else 0
            if l <= 0: return 1 << 60
            bits += l + lbits
            dcode, _, dbits = _distance_to_code_and_extra_for_dump(t.distance)
            dl = dist_lens[dcode] if dcode < len(dist_lens) else 0
            if dl <= 0: return 1 << 60
            bits += dl + dbits
    # EOB
    eob = lit_lens[256] if 256 < len(lit_lens) else 0
    if eob <= 0: return 1 << 60
    bits += eob
    return bits

def _ensure_eob_and_dist(litlen: List[int], dist: List[int]) -> Tuple[List[int], List[int]]:
    l = list(litlen); d = list(dist)
    if len(l) <= 256: l += [0]*(257 - len(l))
    if l[256] == 0: l[256] = 1
    if not any(x > 0 for x in d):
        d = list(d) or [0]
        d[0] = max(1, d[0])
    return l, d

def perturb_swap(lengths: List[int], rng: random.Random) -> None:
    idxs = [i for i, l in enumerate(lengths) if l > 0]
    if len(idxs) < 2: return
    i, j = rng.sample(idxs, 2)
    lengths[i], lengths[j] = lengths[j], lengths[i]

def perturb_add_dummy_adjacent(lengths: List[int], rng: random.Random, maxbits: int = 15) -> None:
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

def random_perturb_lengths(litlen: List[int], dist: List[int], num: int, rng: random.Random) -> Tuple[List[int], List[int]]:
    l = list(litlen); d = list(dist)
    for _ in range(num):
        if rng.random() < 0.6:
            if rng.random() < 0.5: perturb_swap(l, rng)
            else: perturb_add_dummy_adjacent(l, rng, 15)
        else:
            if rng.random() < 0.5: perturb_swap(d, rng)
            else: perturb_add_dummy_adjacent(d, rng, 15)
    l, d = _ensure_eob_and_dist(l, d)
    l = fix_lengths_kraft(l, 15)
    d = fix_lengths_kraft(d, 15)
    return l, d

# ---------- エンコード（ブロック単体の bytes 出力） ----------
def _encode_dynamic_block_bytes(block: "DynamicHuffmanBlock") -> bytes:
    bw = BitWriter()
    block.dump(bw)
    return bw.get_bytes()

@dataclass
class OptimizeResult:
    best_bytes: bytes
    best_bits: int
    best_score: int
    best_litlen: List[int]
    best_dist: List[int]
    tried: int
    accepted: int

ScoreFunc = Callable[[bytes], int]

def optimize_deflate_block(
    base_block: "DynamicHuffmanBlock",
    score_func: ScoreFunc,
    num_iteration: int = 3000,
    num_perturbation: int = 3,
    tolerance_bit: int = 16,
    terminate_threshold: int=-10**100,
    seed: Optional[int] = None,
) -> OptimizeResult:
    rng = random.Random(seed)
    base_bits = estimate_block_bits(base_block.tokens, base_block.header.litlen_code.lengths, base_block.header.dist_code.lengths)
    base_bytes = _encode_dynamic_block_bytes(base_block)
    base_score = score_func(base_bytes)

    best_bytes = base_bytes
    best_bits  = base_bits
    best_score = base_score
    best_lit   = list(base_block.header.litlen_code.lengths)
    best_dist  = list(base_block.header.dist_code.lengths)

    tried = 0
    accepted = 0
    for _ in range(num_iteration):
        tried += 1

        def _is_complete_set(lengths: List[int], maxbits: int) -> bool:
            return _left_after_counts(_build_bit_counts(lengths, maxbits), maxbits) == 0

        cand_l, cand_d = random_perturb_lengths(best_lit, best_dist, num_perturbation, rng)
        # 採用条件の例
        if not _is_complete_set(cand_l, 15) or not _is_complete_set(cand_d, 15):
            continue
        est_bits = estimate_block_bits(base_block.tokens, cand_l, cand_d)
        if est_bits - base_bits > tolerance_bit:
            continue

        # 使っているシンボル集合を収集
        used_lit = _collect_used_litlen_syms(base_block.tokens)
        used_dist = _collect_used_dist_syms(base_block.tokens)

        # oversubscribe 解消 → complete 化（予約付き）→ 切詰め等を内部で実施
        cand_l, cand_d = _ensure_eob_and_dist(cand_l, cand_d)
        lit = _make_tree_complete(fix_lengths_kraft(cand_l, 15), 15, reserved=used_lit)
        dist = _make_tree_complete(fix_lengths_kraft(cand_d, 15), 15, reserved=used_dist)

        lit_eff, dist_eff, hlit, hdist, cl_codec, hclen, rle_stream = build_cl_code_for_lengths(lit, dist)

        # 候補ブロック（bfinal は元を継承）
        cand_block = DynamicHuffmanBlock(
            bfinal=base_block.bfinal,
            tokens=base_block.tokens,
            header=DynamicHuffmanHeader(
                hlit=hlit,
                hdist=hdist,
                hclen=hclen,
                cl_code=cl_codec,
                litlen_code=DynamicHuffmanCode(lit_eff),
                dist_code=DynamicHuffmanCode(dist_eff),
            ),
        )
        cand_bytes = _encode_dynamic_block_bytes(cand_block)
        sc = score_func(cand_bytes)
        accepted += 1
        if (sc < best_score) or (sc == best_score and est_bits < best_bits):
            best_score = sc
            best_bits  = est_bits
            best_bytes = cand_bytes
            best_lit   = cand_l
            best_dist  = cand_d
            if best_score <= terminate_threshold:
                break

    return OptimizeResult(
        best_bytes=best_bytes,
        best_bits=best_bits,
        best_score=best_score,
        best_litlen=best_lit,
        best_dist=best_dist,
        tried=tried,
        accepted=accepted,
    )

def optimize_deflate_stream(
    deflate_stream: bytes,
    score_func: ScoreFunc,
    num_iteration: int = 3000,
    num_perturbation: int = 3,
    tolerance_bit: int = 16,
    terminate_threshold: int=-10**100,
    seed: Optional[int] = None,
    verbose=False
) -> bytes:
    reader = BitReader(deflate_stream)
    blocks: list[Block] = []
    while not blocks or not blocks[-1].bfinal:
        blocks.append(Block.load(reader))

    res = b""
    for i, block in enumerate(blocks):
        writer = BitWriter()
        block.dump(writer)
        block_bytes = writer.get_bytes()
        if isinstance(block, DynamicHuffmanBlock):
            if verbose: print(f"[block#{i}] initial_length={len(block_bytes)} initial_score={score_func(block_bytes)}")
            r = optimize_deflate_block(
                block,
                score_func=score_func,
                num_iteration=num_iteration,
                num_perturbation=num_perturbation,
                tolerance_bit=tolerance_bit,
                terminate_threshold=terminate_threshold,
                seed=seed,
            )
            res += r.best_bytes
            if verbose: print(f"[block#{i}] tried={r.tried} accepted={r.accepted} best_score={r.best_score} bits~={r.best_bits}")
        else:
            if verbose: print(f"[block#{i}] Skipped (not DynHuffman)")
            res += block_bytes
    return res

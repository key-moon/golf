# =========================================================
# Public builder and demo
# =========================================================
def build_block_from_lengths(tokens: List[Token],
                            litlen_lengths: List[int],
                            dist_lengths: List[int],
                            bfinal: int = 1) -> DynamicHuffmanBlock:
    used_lit  = _collect_used_litlen_syms(tokens)
    used_dist = _collect_used_dist_syms(tokens)

    l0, d0 = _ensure_eob_and_dist(litlen_lengths, dist_lengths)
    l0 = _make_tree_complete(fix_lengths_kraft(l0, 15), 15, reserved=used_lit)
    d0 = _make_tree_complete(fix_lengths_kraft(d0, 15), 15, reserved=used_dist)

    lit_eff, dist_eff, hlit, hdist, cl_codec, hclen, rle_stream = build_cl_code_for_lengths(l0, d0)
    lit_code  = DynamicHuffmanCode(lit_eff);  lit_code.build()
    dist_code = DynamicHuffmanCode(dist_eff); dist_code.build()

    header = DynamicHuffmanHeader(
        hlit=hlit, hdist=hdist, hclen=hclen,
        cl_lengths=cl_codec.lengths, rle_code_lengths_stream=rle_stream
    )
    return DynamicHuffmanBlock(
        bfinal=bfinal, tokens=list(tokens),
        header=header, cl_code=cl_codec,
        litlen_code=lit_code, dist_code=dist_code
    )


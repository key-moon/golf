from dataclasses import dataclass
from typing import Optional
from deflate_optimizer.bitio import BitReader, BitWriter
from deflate_optimizer.blocks import Block, LitToken, MatchToken, Token
from deflate_optimizer.huffman import FastHuffman

LEN_BASES = [
    3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,
    35,43,51,59,67,83,99,115,131,163,195,227,258
]
LEN_EXTRA = [
    0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,
    3,3,3,3,4,4,4,4,5,5,5,5,0
]
DIST_BASES = [
    1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,
    257,385,513,769,1025,1537,2049,3073,4097,6145,8193,12289,16385,24577
]
DIST_EXTRA = [
    0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,
    7,7,8,8,9,9,10,10,11,11,12,12,13,13
]

def len_code_to_length(code: int, br: BitReader) -> int:
    if code == 285:
        return 258
    i = code - 257
    base = LEN_BASES[i]
    ebits = LEN_EXTRA[i]
    extra = br.read_bits(ebits) if ebits else 0
    return base + extra

def dist_code_to_distance(code: int, br: BitReader) -> int:
    base = DIST_BASES[code]
    ebits = DIST_EXTRA[code]
    extra = br.read_bits(ebits) if ebits else 0
    return base + extra

def length_to_code_and_extra(length: int) -> tuple[int,int,int]:
    if length < 3 or length > 258:
        raise ValueError("length out of range")
    if length == 258:
        return 285, 0, 0
    for i in range(len(LEN_BASES)-1):
        base = LEN_BASES[i]; nextb = LEN_BASES[i+1]
        if base <= length < nextb:
            return 257 + i, length - base, LEN_EXTRA[i]
    return 285, 0, 0

def distance_to_code_and_extra(distance: int) -> tuple[int,int,int]:
    if distance < 1 or distance > 32768:
        raise ValueError("distance out of range")
    for i in range(len(DIST_BASES)):
        base = DIST_BASES[i]
        nextb = DIST_BASES[i+1] if i+1 < len(DIST_BASES) else 1<<30
        if base <= distance < nextb:
            return i, distance - base, DIST_EXTRA[i]
    raise RuntimeError("distance mapping failed")

def load_tokens(br: BitReader, litlen_codec: FastHuffman, dist_codec: FastHuffman) -> list[Token]:
    toks: list[Token] = []
    while True:
        sym = litlen_codec.read(br)
        if sym < 256:
            toks.append(LitToken(sym))
        elif sym == 256:
            break
        else:
            length = len_code_to_length(sym, br)
            dcode = dist_codec.read(br)
            distance = dist_code_to_distance(dcode, br)
            toks.append(MatchToken(length=length, distance=distance))
    return toks

def dump_tokens(bw: BitWriter, tokens: list[Token], litlen_codec: FastHuffman, dist_codec: FastHuffman) -> None:
    for t in tokens:
        if isinstance(t, LitToken):
            litlen_codec.write(bw, t.lit)
        else:
            assert isinstance(t, MatchToken)
            lcode, lextra, lbits = length_to_code_and_extra(t.length)
            litlen_codec.write(bw, lcode)
            if lbits: bw.write_bits(lextra, lbits)
            dcode, dextra, dbits = distance_to_code_and_extra(t.distance)
            dist_codec.write(bw, dcode)
            if dbits: bw.write_bits(dextra, dbits)
    litlen_codec.write(bw, 256)

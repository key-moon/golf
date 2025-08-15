# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
import random
from typing import List, Tuple, Dict, Optional, Callable

from .bitio import BitReader, BitWriter, dumps
from .huffman import ensure_valid_huffman_lengths, fix_lengths_kraft, last_nonzero_index, FastHuffman

# =========================================================
# RFC1951 tables and helpers
# =========================================================

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

def reverse_bits(x: int, nbits: int) -> int:
    r = 0
    for _ in range(nbits):
        r = (r << 1) | (x & 1)
        x >>= 1
    return r

def kraft_overflow(lengths: List[int]) -> bool:
    total = 0.0
    for l in lengths:
        if l > 0:
            total += 1.0 / (1 << l)
            if total > 1.0 + 1e-12:
                return True
    return False


# =========================================================
# Tokens / Blocks
# =========================================================

class Token: ...
@dataclass
class LitToken(Token):
    lit: int

@dataclass
class MatchToken(Token):
    length: int
    distance: int

@dataclass
class Block(ABC):
    bfinal: int  # 0 or 1

    @abstractmethod
    def dump(self, bw: "BitWriter") -> None:
        raise NotImplementedError

    @staticmethod
    def load(br: "BitReader") -> "Block":
        bfinal = br.read_bit()
        btype = br.read_bits(2)
        if btype == 0b10:
            return DynamicHuffmanBlock.load_from_body(br, bfinal)
        elif btype == 0b01:
            return StaticHuffmanBlock.load_from_body(br, bfinal)
        elif btype == 0b00:
            return StoredBlock.load_from_body(br, bfinal)
        else:
            raise ValueError("Invalid reserved BTYPE=0b11")

@dataclass
class StoredBlock(Block):
    """非圧縮ブロック (BTYPE=00)。"""
    data: bytes  # 生データ

    @staticmethod
    def load_from_body(br: "BitReader", bfinal: int) -> "StoredBlock":
        # 仕様：BTYPE=00 の直後にバイト境界に合わせる
        br.align_to_next_byte()
        # LEN / NLEN (16-bit, little-endian)
        length = br.read_bits(16)
        nlen   = br.read_bits(16)
        if (length ^ nlen) != 0xFFFF:
            raise ValueError("Stored block LEN/NLEN mismatch")
        payload = br.read_bytes(length)
        return StoredBlock(bfinal=bfinal, data=payload)

    def dump(self, bw: "BitWriter") -> None:
        # ヘッダ
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b00, 2)
        # バイト境界に揃える
        bw.align_to_byte()
        length = len(self.data)
        nlen = length ^ 0xFFFF
        # 16-bit little-endian を LSB-first でそのまま書く
        bw.write_bits(length, 16)
        bw.write_bits(nlen, 16)
        # ペイロード
        for b in self.data:
            bw.write_bits(b, 8)

class HuffmanBlock(Block):
    tokens: List[Token]

def _fixed_litlen_lengths() -> List[int]:
    lens = [0]*288  # 0..287
    for s in range(0, 144):   lens[s] = 8
    for s in range(144, 256): lens[s] = 9
    for s in range(256, 280): lens[s] = 7
    for s in range(280, 288): lens[s] = 8
    return lens

def _fixed_dist_lengths() -> List[int]:
    lens = [5]*32  # 0..31
    return lens

STATIC_LITLEN_CODEC, STATIC_DIST_CODEC = FastHuffman(_fixed_litlen_lengths()), FastHuffman(_fixed_dist_lengths())

@dataclass
class StaticHuffmanBlock(HuffmanBlock):
    """固定ハフマン (BTYPE=01)"""
    tokens: List["Token"]

    @staticmethod
    def load_from_body(br: "BitReader", bfinal: int) -> "StaticHuffmanBlock":
        toks: List[Token] = []
        while True:
            sym = STATIC_LITLEN_CODEC.read(br)
            if sym < 256:
                toks.append(LitToken(sym))
            elif sym == 256:
                break
            else:
                length = len_code_to_length(sym, br)
                dcode = STATIC_DIST_CODEC.read(br)
                distance = dist_code_to_distance(dcode, br)
                toks.append(MatchToken(length=length, distance=distance))
        return StaticHuffmanBlock(bfinal=bfinal, tokens=toks)

    def dump(self, bw: "BitWriter") -> None:
        # ヘッダ
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b01, 2)

        for t in self.tokens:
            if isinstance(t, LitToken):
                STATIC_LITLEN_CODEC.write(bw, t.lit)
            else:
                assert isinstance(t, MatchToken)
                lcode, lextra, lbits = _length_to_code_and_extra_for_dump(t.length)
                STATIC_LITLEN_CODEC.write(bw, lcode)
                if lbits: bw.write_bits(lextra, lbits)
                dcode, dextra, dbits = _distance_to_code_and_extra_for_dump(t.distance)
                STATIC_DIST_CODEC.write(bw, dcode)
                if dbits: bw.write_bits(dextra, dbits)
        # EOB
        STATIC_LITLEN_CODEC.write(bw, 256)


# =========================================================
# Code-Length Alphabet utils
# =========================================================

CL_ORDER = [16,17,18, 0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15]

def rle_code_lengths_stream(litlen: List[int], dist: List[int], allow_16=True, allow_17=True, allow_18=True) -> List[Tuple[int,int,int]]:
    """
    litlen + dist のコード長列を RFC1951 の RLE で列挙。
    返値は (symbol, extra_value, extra_bits):
      - 0..15 : そのままコード長値
      - 16    : 直前の長さを 3..6 回繰り返す（2 ビットで回数-3 を表す）
      - 17    : 0 を 3..10 回
      - 18    : 0 を 11..138 回
    """
    seq = list(litlen) + list(dist)
    out: List[Tuple[int,int,int]] = []
    i = 0
    while i < len(seq):
        cur = seq[i]
        run = 1
        j = i + 1
        while j < len(seq) and seq[j] == cur:
            run += 1; j += 1

        if cur == 0:
            k = run
            while k >= 11 and allow_18:
                use = min(138, k)
                out.append((18, use - 11, 7))
                k -= use
            while k >= 3 and allow_17:
                out.append((17, k - 3, 3))
                k = 0
            out.extend([(0, 0, 0)] * k)
        else:
            out.append((cur, 0, 0))
            k = run - 1
            while k >= 3 and allow_16:
                consume = min(k, 6)
                out.append((16, consume - 3, 2))
                k -= consume
            out.extend([(cur, 0, 0)] * k)

        i = j

    return out

def hclen_from_cl_lengths(cl_lengths: List[int]) -> int:
    last = -1
    for i in range(len(CL_ORDER)-1, -1, -1):
        if cl_lengths[CL_ORDER[i]] != 0:
            last = i; break
    if last < 0: last = 0
    return max(0, (last + 1) - 4)

def lengths_from_freq(freqs: List[int], maxbits: int) -> List[int]:
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
    parent: Dict[int,int] = {}
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

@dataclass
class DynamicHuffmanCodeLengthCode:
    """Code Length Alphabet (0..18), maxbits=7"""
    lengths: List[int]
    _codec: Optional[FastHuffman] = None

    def __post_init__(self):
        self._codec = FastHuffman(self.lengths)

    def write(self, bw: BitWriter, sym: int) -> None:
        assert self._codec is not None
        self._codec.write(bw, sym)

    def read(self, br: BitReader) -> int:
        assert self._codec is not None
        return self._codec.read(br)

    @staticmethod
    def load(br: BitReader, hclen_count: int) -> "DynamicHuffmanCodeLengthCode":
        lens = [0]*19
        for i in range(hclen_count):
            sym = CL_ORDER[i]
            lens[sym] = br.read_bits(3)
        obj = DynamicHuffmanCodeLengthCode(lens)
        return obj

    def dump_lengths(self, bw: BitWriter, hclen_count: int) -> None:
        for i in range(hclen_count):
            sym = CL_ORDER[i]
            l = self.lengths[sym] if 0 <= sym < len(self.lengths) else 0
            bw.write_bits(l, 3)


@dataclass
class DynamicHuffmanCode:
    """lit/len(0..285) or dist(0..29), maxbits=15"""
    lengths: List[int]
    _codec: Optional[FastHuffman] = None

    def __post_init__(self):
        self._codec = FastHuffman(self.lengths)

    def write(self, bw: BitWriter, sym: int) -> None:
        assert self._codec is not None
        self._codec.write(bw, sym)

    def read(self, br: BitReader) -> int:
        assert self._codec is not None
        return self._codec.read(br)


# =========================================================
# Header and Block
# =========================================================

@dataclass
class DynamicHuffmanHeader:
    hlit: int
    hdist: int
    hclen: int
    cl_code: DynamicHuffmanCodeLengthCode
    litlen_code: DynamicHuffmanCode
    dist_code: DynamicHuffmanCode

    @staticmethod
    def load(br: BitReader) -> "DynamicHuffmanHeader":
        hlit  = br.read_bits(5)
        hdist = br.read_bits(5)
        hclen = br.read_bits(4)

        num_litlen = hlit + 257
        num_dist   = hdist + 1
        cl_count   = hclen + 4

        cl_code = DynamicHuffmanCodeLengthCode.load(br, cl_count)

        total = num_litlen + num_dist
        seq: List[int] = []
        prev_len = -1
        while len(seq) < total:
            sym = cl_code.read(br)
            if 0 <= sym <= 15:
                seq.append(sym)
                prev_len = sym
            elif sym == 16:
                if len(seq) == 0 or prev_len == -1:
                    raise ValueError("CL: symbol 16 used with no valid previous length")
                repeat = br.read_bits(2) + 3  # 3..6
                seq.extend([prev_len] * repeat)
            elif sym == 17:
                repeat = br.read_bits(3) + 3  # 3..10 zeros
                seq.extend([0] * repeat)
                prev_len = 0
            elif sym == 18:
                repeat = br.read_bits(7) + 11 # 11..138 zeros
                seq.extend([0] * repeat)
                prev_len = 0
            else:
                raise ValueError("Invalid CL symbol")

        assert len(seq) == num_litlen + num_dist

        litlen_lengths = seq[:num_litlen]
        dist_lengths   = seq[num_litlen:]

        if litlen_lengths[256] == 0:
            raise ValueError("EOB(256) must have non-zero code length")

        header = DynamicHuffmanHeader(
            hlit=hlit, hdist=hdist, hclen=hclen,
            cl_code=cl_code, litlen_code=DynamicHuffmanCode(litlen_lengths), dist_code=DynamicHuffmanCode(dist_lengths)
        )
        return header
    def dump(self, bw: "BitWriter") -> None:
        if len(self.litlen_code.lengths) < 257 or self.litlen_code.lengths[256] <= 0:
            raise ValueError("EOB (256) must have a non-zero code length and at least 257 litlen lengths are required.")
        ensure_valid_huffman_lengths(self.litlen_code.lengths, 15)
        ensure_valid_huffman_lengths(self.dist_code.lengths, 15)

        bw.write_bits(self.hlit, 5)
        bw.write_bits(self.hdist, 5)
        bw.write_bits(self.hclen, 4)
        self.cl_code.dump_lengths(bw, self.hclen + 4)

        allow_16, allow_17, allow_18 = [i < len(self.cl_code.lengths) and self.cl_code.lengths[i] != 0  for i in (16, 17, 18)]

        litlen_lengths = self.litlen_code.lengths
        dist_lengths = self.dist_code.lengths
        rle_stream = rle_code_lengths_stream(
            litlen_lengths,
            dist_lengths,
            allow_16, allow_17, allow_18
        )

        for sym, extra_val, extra_bits in rle_stream:
            self.cl_code.write(bw, sym)
            if extra_bits:
                bw.write_bits(extra_val, extra_bits)

# =========================================================
# 共通: CL を lit/len + dist から構築するファクトリ
# =========================================================

def _cut_and_indices(litlen: List[int], dist: List[int]) -> Tuple[List[int], List[int], int, int]:
    l_last = last_nonzero_index(litlen)
    d_last = last_nonzero_index(dist)
    num_litlen = max(l_last + 1, 257)
    num_dist   = max(d_last + 1, 1)
    return litlen[:num_litlen], dist[:num_dist], num_litlen, num_dist

def build_header_from_lengths(
    litlen_lengths: List[int],
    dist_lengths: List[int],
):
    # 後端ゼロ切詰め → HLIT/HDIST
    litlen_lengths, dist_lengths, num_litlen, num_dist = _cut_and_indices(litlen_lengths, dist_lengths)
    hlit  = num_litlen - 257
    hdist = num_dist   - 1

    # RLE 生成
    rle_stream = rle_code_lengths_stream(litlen_lengths, dist_lengths)

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
        DynamicHuffmanCode(litlen_lengths),
        DynamicHuffmanCode(dist_lengths)
    )

# =========================================================
# DynamicHuffmanBlock
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

@dataclass
class DynamicHuffmanBlock(HuffmanBlock):
    bfinal: int
    header: DynamicHuffmanHeader
    tokens: List[Token]

    @staticmethod
    def load(br: BitReader) -> "DynamicHuffmanBlock":
        blk = Block.load(br)
        if not isinstance(blk, DynamicHuffmanBlock):
            raise ValueError("Expected DynamicHuffmanBlock")
        return blk

    @staticmethod
    def load_from_body(br: BitReader, bfinal: int) -> "DynamicHuffmanBlock":
        header = DynamicHuffmanHeader.load(br)
        litlen = header.litlen_code
        dist = header.dist_code
        if not any(l > 0 for l in dist.lengths):
            raise ValueError("Distance tree has no codes")

        tokens: List[Token] = []
        while True:
            sym = litlen.read(br)
            if sym < 256:
                tokens.append(LitToken(sym))
            elif sym == 256:
                break
            else:
                length = len_code_to_length(sym, br)
                dcode  = dist.read(br)
                distance = dist_code_to_distance(dcode, br)
                tokens.append(MatchToken(length=length, distance=distance))

        return DynamicHuffmanBlock(bfinal=bfinal, header=header, tokens=tokens)

    def dump(self, bw: BitWriter) -> None:
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b10, 2)

        # --- 以降は既存どおり ---
        self.header.dump(bw)

        for t in self.tokens:
            if isinstance(t, LitToken):
                self.header.litlen_code.write(bw, t.lit)
            else:
                assert isinstance(t, MatchToken)
                lcode, lextra, lbits = _length_to_code_and_extra_for_dump(t.length)
                self.header.litlen_code.write(bw, lcode);  (bw.write_bits(lextra, lbits) if lbits else None)
                dcode, dextra, dbits = _distance_to_code_and_extra_for_dump(t.distance)
                self.header.dist_code.write(bw, dcode); (bw.write_bits(dextra, dbits) if dbits else None)
        self.header.litlen_code.write(bw, 256)


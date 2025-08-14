# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
import random
from typing import List, Sequence, Tuple, Dict, Optional, Callable, Iterable

from tqdm import tqdm

# =========================================================
# Bit I/O with lookahead (LSB-first as in Deflate)
# =========================================================

class BitWriter:
    __slots__ = ("_buf", "_bitbuf", "_bitcnt")
    def __init__(self):
        self._buf = bytearray()
        self._bitbuf = 0
        self._bitcnt = 0

    def write_bits(self, value: int, nbits: int) -> None:
        if nbits < 0:
            raise ValueError("nbits must be >= 0")
        v = value & ((1 << nbits) - 1) if nbits else 0
        self._bitbuf |= v << self._bitcnt
        self._bitcnt += nbits
        while self._bitcnt >= 8:
            self._buf.append(self._bitbuf & 0xFF)
            self._bitbuf >>= 8
            self._bitcnt -= 8

    def align_to_byte(self) -> None:
        if self._bitcnt > 0:
            self._buf.append(self._bitbuf & 0xFF)
            self._bitbuf = 0
            self._bitcnt = 0

    def get_bytes(self) -> bytes:
        self.align_to_byte()
        return bytes(self._buf)


class BitReader:
    __slots__ = ("_data","_pos","_bitbuf","_bitcnt")
    def __init__(self, data: bytes):
        self._data = data
        self._pos = 0
        self._bitbuf = 0
        self._bitcnt = 0

    def ensure_bits(self, nbits: int, allow_zerofill: bool = False) -> None:
        while self._bitcnt < nbits and self._pos < len(self._data):
            self._bitbuf |= self._data[self._pos] << self._bitcnt
            self._pos += 1
            self._bitcnt += 8
        if self._bitcnt < nbits and not allow_zerofill:
            raise EOFError("read past end")

    def peek_bits(self, nbits: int, allow_zerofill: bool = True) -> int:
        if nbits < 0:
            raise ValueError("nbits must be >= 0")
        self.ensure_bits(nbits, allow_zerofill=allow_zerofill)
        return self._bitbuf & ((1 << nbits) - 1)

    def drop_bits(self, nbits: int) -> None:
        if nbits < 0:
            raise ValueError("nbits must be >= 0")
        self.ensure_bits(nbits, allow_zerofill=False)
        self._bitbuf >>= nbits
        self._bitcnt -= nbits

    def read_bits(self, nbits: int) -> int:
        v = self.peek_bits(nbits, allow_zerofill=False)
        self.drop_bits(nbits)
        return v

    def read_bit(self) -> int:
        return self.read_bits(1)

    def align_to_next_byte(self) -> None:
        """BTYPE=00 (stored) 用：現在のパーシャルバイトの残りビットを捨ててバイト境界に進める。"""
        drop = self._bitcnt % 8
        if drop:
            self.drop_bits(drop)

    def read_bytes(self, n: int) -> bytes:
        """現在位置からちょうど n バイト取り出す（必要なら内部ビットバッファからも取り出す）。"""
        self.align_to_next_byte()
        out = bytearray()
        # まずバッファ内のフルバイトを吸い出し
        while n > 0 and self._bitcnt >= 8:
            out.append(self._bitbuf & 0xFF)
            self._bitbuf >>= 8
            self._bitcnt -= 8
            n -= 1
        # 残りは _data から
        if n > 0:
            if self._pos + n > len(self._data):
                raise EOFError("read past end")
            out += self._data[self._pos:self._pos+n]
            self._pos += n
            n = 0
        return bytes(out)

    def at_eof(self) -> bool:
        return self._pos >= len(self._data) and self._bitcnt == 0


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

def last_nonzero_index(a: List[int]) -> int:
    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            return i
    return -1

def kraft_overflow(lengths: List[int]) -> bool:
    total = 0.0
    for l in lengths:
        if l > 0:
            total += 1.0 / (1 << l)
            if total > 1.0 + 1e-12:
                return True
    return False

def fix_lengths_kraft(lengths: List[int], maxbits: int) -> List[int]:
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
        """サブクラスが実装（Dynamic/Static/Stored）"""
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


class HuffmanBlock(Block):
    tokens: List[Token]

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

@dataclass
class StaticHuffmanBlock(HuffmanBlock):
    """固定ハフマン (BTYPE=01)"""
    tokens: List["Token"]

    @staticmethod
    def load_from_body(br: "BitReader", bfinal: int) -> "StaticHuffmanBlock":
        # 固定木を構築
        lit_lens  = _fixed_litlen_lengths()
        dist_lens = _fixed_dist_lengths()
        lit = DynamicHuffmanCode(lit_lens);  lit.build()
        dist = DynamicHuffmanCode(dist_lens); dist.build()

        toks: List[Token] = []
        while True:
            sym = lit.read(br)
            if sym < 256:
                toks.append(LitToken(sym))
            elif sym == 256:
                break
            else:
                length = len_code_to_length(sym, br)
                dcode = dist.read(br)
                distance = dist_code_to_distance(dcode, br)
                toks.append(MatchToken(length=length, distance=distance))
        return StaticHuffmanBlock(bfinal=bfinal, tokens=toks)

    def dump(self, bw: "BitWriter") -> None:
        # ヘッダ
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b01, 2)
        # 固定木
        lit_lens  = _fixed_litlen_lengths()
        dist_lens = _fixed_dist_lengths()
        lit = DynamicHuffmanCode(lit_lens);  lit.build()
        dist = DynamicHuffmanCode(dist_lens); dist.build()

        for t in self.tokens:
            if isinstance(t, LitToken):
                lit.write(bw, t.lit)
            else:
                assert isinstance(t, MatchToken)
                lcode, lextra, lbits = _length_to_code_and_extra_for_dump(t.length)
                lit.write(bw, lcode)
                if lbits: bw.write_bits(lextra, lbits)
                dcode, dextra, dbits = _distance_to_code_and_extra_for_dump(t.distance)
                dist.write(bw, dcode)
                if dbits: bw.write_bits(dextra, dbits)
        # EOB
        lit.write(bw, 256)


# =========================================================
# Code-Length Alphabet utils
# =========================================================

CL_ORDER = [16,17,18, 0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15]

def rle_code_lengths_stream(litlen: List[int], dist: List[int]) -> List[Tuple[int,int,int]]:
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
        # 連長
        run = 1
        j = i + 1
        while j < len(seq) and seq[j] == cur:
            run += 1; j += 1

        if cur == 0:
            k = run
            while k >= 11:
                use = min(138, k)
                out.append((18, use - 11, 7))
                k -= use
            if k >= 3:
                out.append((17, k - 3, 3))
                k = 0
            # 残り 0..2 個はリテラル 0 をその数だけ
            out.extend([(0, 0, 0)] * k)
        else:
            # まず 1 個はリテラルで出す
            out.append((cur, 0, 0))
            k = run - 1
            # 3..6 は 16 を使う
            while k >= 6:
                out.append((16, 3, 2))  # 6回 → extra=6-3=3
                k -= 6
            if k >= 3:
                out.append((16, k - 3, 2))
                k = 0
            # 残り 1..2 回はリテラルで出す（← これが修正点）
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


# =========================================================
# Fast Huffman codec with peek (for CL and lit/len/dist)
# =========================================================

class _FastHuffman:
    __slots__ = ("enc_map","dec_table","maxbits","mask")
    def __init__(self, lengths: List[int], maxbits: int):
        self.maxbits = maxbits
        self.mask = (1 << maxbits) - 1
        pairs = [(l, s) for s, l in enumerate(lengths) if l > 0]
        if not pairs:
            raise ValueError("Huffman must have at least one non-zero length")
        pairs.sort()
        maxlen = max(l for l, _ in pairs)
        if maxlen > maxbits:
            raise ValueError("code length exceeds maxbits")

        bl_count = [0]*(maxlen+1)
        for l, _ in pairs: bl_count[l] += 1
        next_code = [0]*(maxlen+1)
        code = 0
        for bits in range(1, maxlen+1):
            code = (code + bl_count[bits-1]) << 1
            next_code[bits] = code

        enc_map: Dict[int, Tuple[int,int]] = {}
        for length, sym in pairs:
            c = next_code[length]
            next_code[length] += 1
            enc_map[sym] = (reverse_bits(c, length), length)

        size = 1 << maxbits
        dec_table: List[Tuple[int,int]] = [(-1, 0)] * size
        for sym, (code_lsb, nb) in enc_map.items():
            reps = 1 << (maxbits - nb)
            base = code_lsb
            for k in range(reps):
                idx = (k << nb) | base
                dec_table[idx] = (sym, nb)

        self.enc_map = enc_map
        self.dec_table = dec_table

    def write(self, bw: BitWriter, sym: int) -> None:
        code, n = self.enc_map[sym]
        bw.write_bits(code, n)

    def read(self, br: BitReader) -> int:
        # 最長長で先読み。末尾ギリギリでも 0 埋め peek を許容
        bits = br.peek_bits(self.maxbits, allow_zerofill=True)
        sym, n = self.dec_table[bits & self.mask]
        if n == 0 or sym < 0:
            raise ValueError("invalid Huffman prefix")
        br.drop_bits(n)  # drop は厳格（ここでは実在ビット数）
        return sym


@dataclass
class DynamicHuffmanCodeLengthCode:
    """Code Length Alphabet (0..18), maxbits=7"""
    lengths: List[int]
    _codec: Optional[_FastHuffman] = None

    def build(self) -> None:
        self._codec = _FastHuffman(self.lengths, maxbits=7)

    def write(self, bw: BitWriter, sym: int) -> None:
        if self._codec is None: self.build()
        self._codec.write(bw, sym)

    def read(self, br: BitReader) -> int:
        if self._codec is None: self.build()
        return self._codec.read(br)

    @staticmethod
    def load(br: BitReader, hclen_count: int) -> "DynamicHuffmanCodeLengthCode":
        lens = [0]*19
        for i in range(hclen_count):
            sym = CL_ORDER[i]
            lens[sym] = br.read_bits(3)
        obj = DynamicHuffmanCodeLengthCode(lens)
        obj.build()
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
    _codec: Optional[_FastHuffman] = None

    def build(self) -> None:
        self._codec = _FastHuffman(self.lengths, maxbits=15)

    def write(self, bw: BitWriter, sym: int) -> None:
        if self._codec is None: self.build()
        self._codec.write(bw, sym)

    def read(self, br: BitReader) -> int:
        if self._codec is None: self.build()
        return self._codec.read(br)


# =========================================================
# Header and Block
# =========================================================

@dataclass
class DynamicHuffmanHeader:
    hlit: int
    hdist: int
    hclen: int
    cl_lengths: List[int]
    rle_code_lengths_stream: List[Tuple[int,int,int]]

    @staticmethod
    def load(br: BitReader) -> Tuple["DynamicHuffmanHeader", DynamicHuffmanCode, DynamicHuffmanCode]:
        hlit  = br.read_bits(5)
        hdist = br.read_bits(5)
        hclen = br.read_bits(4)

        num_litlen = hlit + 257
        num_dist   = hdist + 1
        cl_count   = hclen + 4

        cl_code = DynamicHuffmanCodeLengthCode.load(br, cl_count)

        total = num_litlen + num_dist
        seq: List[int] = []
        prev_len = 0
        while len(seq) < total:
            sym = cl_code.read(br)
            if 0 <= sym <= 15:
                seq.append(sym)
                prev_len = sym
            elif sym == 16:
                if len(seq) == 0 or prev_len == 0:
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

        seq = seq[:num_litlen + num_dist]
        litlen_lengths = seq[:num_litlen]
        dist_lengths   = seq[num_litlen:]

        if litlen_lengths[256] == 0:
            raise ValueError("EOB(256) must have non-zero code length")

        header = DynamicHuffmanHeader(
            hlit=hlit, hdist=hdist, hclen=hclen,
            cl_lengths=cl_code.lengths, rle_code_lengths_stream=[]
        )
        return header, DynamicHuffmanCode(litlen_lengths), DynamicHuffmanCode(dist_lengths)


# =========================================================
# 共通: CL を lit/len + dist から構築するファクトリ
# =========================================================

def _ensure_eob_and_dist(litlen: List[int], dist: List[int]) -> Tuple[List[int], List[int]]:
    l = list(litlen); d = list(dist)
    if len(l) <= 256:
        l += [0]*(257 - len(l))
    if l[256] == 0:
        l[256] = 1
    if not any(x > 0 for x in d):
        d = list(d) or [0]
        d[0] = max(1, d[0])
    return l, d

def _cut_and_indices(litlen: List[int], dist: List[int]) -> Tuple[List[int], List[int], int, int]:
    l_last = last_nonzero_index(litlen)
    d_last = last_nonzero_index(dist)
    num_litlen = max(l_last + 1, 257)
    num_dist   = max(d_last + 1, 1)
    return litlen[:num_litlen], dist[:num_dist], num_litlen, num_dist

def build_cl_code_for_lengths(
    litlen_lengths: List[int],
    dist_lengths: List[int],
) -> Tuple[
    List[int], List[int],   # litlen_effective, dist_effective
    int, int,               # hlit, hdist
    DynamicHuffmanCodeLengthCode, int,  # cl_codec, hclen
    List[Tuple[int,int,int]]           # rle_stream
]:
    # 安全化 + Kraft
    litlen, dist = _ensure_eob_and_dist(litlen_lengths, dist_lengths)
    litlen = fix_lengths_kraft(litlen, 15)
    dist   = fix_lengths_kraft(dist, 15)

    # 後端ゼロ切り詰め → HLIT/HDIST
    litlen_eff, dist_eff, num_litlen, num_dist = _cut_and_indices(litlen, dist)
    hlit  = num_litlen - 257
    hdist = num_dist - 1

    rle_stream = rle_code_lengths_stream(litlen_eff, dist_eff)

    # CL 頻度 → 制限長ハフマン
    cl_freq = [0]*19
    for sym,_,_ in rle_stream:
        cl_freq[sym] += 1
    cl_lengths_raw = lengths_from_freq(cl_freq, maxbits=7)

    # HCLEN 決定
    hclen = hclen_from_cl_lengths(cl_lengths_raw)

    # ★ 宣言範囲外（CL_ORDER[hclen+4:]）は 0 に強制
    active = set(CL_ORDER[:hclen + 4])
    cl_lengths = [ (cl_lengths_raw[i] if i in active else 0) for i in range(19) ]

    cl_codec = DynamicHuffmanCodeLengthCode(cl_lengths); cl_codec.build()

    # 使うシンボルがゼロ長になっていないかの自衛チェック
    for sym,_,_ in rle_stream:
        if cl_codec.lengths[sym] == 0:
            raise AssertionError("internal: CL symbol used by RLE has zero length after HCLEN mask")

    return (litlen_eff, dist_eff, hlit, hdist, cl_codec, hclen, rle_stream)

# =========================================================
# DynamicHuffmanBlock
# =========================================================

@dataclass
class DynamicHuffmanBlock(HuffmanBlock):
    bfinal: int
    tokens: List[Token]
    header: DynamicHuffmanHeader
    cl_code: DynamicHuffmanCodeLengthCode
    litlen_code: DynamicHuffmanCode
    dist_code: DynamicHuffmanCode

    @staticmethod
    def load(br: BitReader) -> "DynamicHuffmanBlock":
        blk = Block.load(br)
        if not isinstance(blk, DynamicHuffmanBlock):
            raise ValueError("Expected DynamicHuffmanBlock")
        return blk

    @staticmethod
    def load_from_body(br: BitReader, bfinal: int) -> "DynamicHuffmanBlock":
        header, litlen, dist = DynamicHuffmanHeader.load(br)
        litlen.build()
        if not any(l > 0 for l in dist.lengths):
            raise ValueError("Distance tree has no codes")
        dist.build()

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

        cl_code = DynamicHuffmanCodeLengthCode(header.cl_lengths); cl_code.build()
        return DynamicHuffmanBlock(
            bfinal=bfinal, tokens=tokens,
            header=header, cl_code=cl_code,
            litlen_code=litlen, dist_code=dist
        )

    def dump(self, bw: BitWriter) -> None:
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b10, 2)

        (lit_eff, dist_eff,
         hlit, hdist,
         cl_codec, hclen,
         rle_stream) = build_cl_code_for_lengths(self.litlen_code.lengths, self.dist_code.lengths)

        # EOB(256) の健全性を念押し確認
        assert len(lit_eff) >= 257 and lit_eff[256] > 0

        # HLIT/HDIST/HCLEN
        bw.write_bits(hlit, 5)
        bw.write_bits(hdist, 5)
        bw.write_bits(hclen, 4)

        # CL 3bit 長さ（マスク済み配列に対応）
        cl_codec.dump_lengths(bw, hclen + 4)

        # RLE ストリームを CL ハフマンで符号化
        for sym, extra_val, extra_bits in rle_stream:
            cl_codec.write(bw, sym)
            if extra_bits:
                bw.write_bits(extra_val, extra_bits)

        # 本体
        lit_codec  = DynamicHuffmanCode(lit_eff);  lit_codec.build()
        dist_codec = DynamicHuffmanCode(dist_eff); dist_codec.build()

        for t in self.tokens:
            if isinstance(t, LitToken):
                lit_codec.write(bw, t.lit)
            else:
                lcode, lextra, lbits = _length_to_code_and_extra_for_dump(t.length)
                lit_codec.write(bw, lcode)
                if lbits: bw.write_bits(lextra, lbits)
                dcode, dextra, dbits = _distance_to_code_and_extra_for_dump(t.distance)
                dist_codec.write(bw, dcode)
                if dbits: bw.write_bits(dextra, dbits)

        lit_codec.write(bw, 256)  # EOB

        # ヘッダ情報を“実際に出力した値”で更新（cl_lengths はマスク済み）
        self.header = DynamicHuffmanHeader(
            hlit=hlit, hdist=hdist, hclen=hclen,
            cl_lengths=cl_codec.lengths,
            rle_code_lengths_stream=rle_stream
        )
        self.cl_code = cl_codec
        self.litlen_code = DynamicHuffmanCode(lit_eff);  self.litlen_code.build()
        self.dist_code   = DynamicHuffmanCode(dist_eff); self.dist_code.build()


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


# =========================================================
# Public builder and demo
# =========================================================

def build_block_from_lengths(tokens: Sequence[Token],
                            litlen_lengths: List[int],
                            dist_lengths: List[int],
                            bfinal: int = 1) -> DynamicHuffmanBlock:
    # まず CL を本計算（内部で EOB/距離/クラフト/切詰めを実施）
    lit_eff, dist_eff, hlit, hdist, cl_codec, hclen, rle_stream = \
        build_cl_code_for_lengths(litlen_lengths, dist_lengths)

    # コーデックを構築
    lit_code  = DynamicHuffmanCode(lit_eff);  lit_code.build()
    dist_code = DynamicHuffmanCode(dist_eff); dist_code.build()

    header = DynamicHuffmanHeader(
        hlit=hlit, hdist=hdist, hclen=hclen,
        cl_lengths=cl_codec.lengths,
        rle_code_lengths_stream=rle_stream
    )

    return DynamicHuffmanBlock(
        bfinal=bfinal, tokens=list(tokens),
        header=header, cl_code=cl_codec,
        litlen_code=lit_code, dist_code=dist_code
    )


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
    cl_table = _FastHuffman(cl_lengths, 7)  # 先読みテーブルで長さ n を得るためだけに使用
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
    base_bits = estimate_block_bits(base_block.tokens, base_block.litlen_code.lengths, base_block.dist_code.lengths)
    base_bytes = _encode_dynamic_block_bytes(base_block)
    base_score = score_func(base_bytes)

    best_bytes = base_bytes
    best_bits  = base_bits
    best_score = base_score
    best_lit   = list(base_block.litlen_code.lengths)
    best_dist  = list(base_block.dist_code.lengths)

    tried = 0
    accepted = 0
    for _ in range(num_iteration):
        tried += 1

        cand_l, cand_d = random_perturb_lengths(best_lit, best_dist, num_perturbation, rng)
        est_bits = estimate_block_bits(base_block.tokens, cand_l, cand_d)
        if est_bits - base_bits <= tolerance_bit:
            # 候補ブロック（bfinal は元を継承）
            cand_block = DynamicHuffmanBlock(
                bfinal=base_block.bfinal,
                tokens=base_block.tokens,
                header=base_block.header,      # dump 内で上書きされる
                cl_code=base_block.cl_code,    # dump 内で上書きされる
                litlen_code=DynamicHuffmanCode(cand_l),
                dist_code=DynamicHuffmanCode(cand_d),
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
                print(best_score)
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

if __name__ == "__main__":
    import zlib, os
    plain = open("base_arcdsl/task001.py~retire", "rb").read()
    # wbits=-15 で raw deflate
    deflate = zlib.compress(plain, level=6, wbits=-15)
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

    w = BitWriter()
    for b in blocks:
        print(b)
        b.dump(w)
    assert zlib.decompress(w.get_bytes(), wbits=-15) == plain

    print(f"{len(blocks)=}")

    res = b""
    for i, block in enumerate(blocks):
        writer = BitWriter()
        block.dump(writer)
        block_bytes = writer.get_bytes()

        if isinstance(block, DynamicHuffmanBlock):
            print(f"[block#{i}] initial_length={len(block_bytes)} initial_score={score(block_bytes)}")
            r = optimize_deflate_block(
                block,
                score_func=score,
                num_iteration=2000,
                num_perturbation=3,
                tolerance_bit=16,
                terminate_threshold=len(block_bytes),
                seed=1234,
            )
            res += r.best_bytes
            print(f"[block#{i}] tried={r.tried} accepted={r.accepted} best_score={r.best_score} bits~={r.best_bits}")
        else:
            print(f"[block#{i}] Skipped (not DynHuffman)")
            res += block_bytes

    decompressed = zlib.decompress(res, wbits=-15)
    print(decompressed == plain)
  

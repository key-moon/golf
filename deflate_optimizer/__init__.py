# -*- coding: utf-8 -*-
# Dynamic Huffman Deflate with proper CL (code-length alphabet) construction.
# Python 3.10+

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
import random
from typing import List, Tuple, Dict, Optional, Callable
import zlib

from .bitio import BitReader, BitWriter, dumps
from .huffman import fix_lengths_kraft, last_nonzero_index, FastHuffman

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

# ---- 追加: zlib と同等の left 判定（不完全 / 過剰） ----
def _build_bit_counts(lengths: List[int], maxbits: int) -> List[int]:
    cnt = [0]*(maxbits+1)
    for l in lengths:
        if 0 < l <= maxbits:
            cnt[l] += 1
    return cnt

def _left_after_counts(counts: List[int], maxbits: int) -> int:
    """
    zlib の inflate_table 相当:
      left < 0 -> oversubscribed（過剰）
      left = 0 -> complete（完全）
      left > 0 -> incomplete（不完全）
    """
    left = 1
    for bits in range(1, maxbits+1):
        left <<= 1
        left -= counts[bits] if bits < len(counts) else 0
    return left

def _make_tree_complete(lengths: List[int],
                        maxbits: int,
                        reserved: Optional[set] = None) -> List[int]:
    """
    lengths を「oversubscribe でない」かつ「complete（left==0）」に補正する。
    - oversubscribe（left<0）は既存の fix_lengths_kraft() で解消されている前提でもう一度チェック。
    - incomplete（left>0）は、長さ 0 のシンボルに maxbits を割り当てて left を 0 まで埋める。
      予約済み（reserved）シンボルは変更しない。
    """
    lens = list(lengths)
    # まず oversubscribe を排除（∑2^-L ≤ 1 まで延長）
    lens = fix_lengths_kraft(lens, maxbits)

    counts = _build_bit_counts(lens, maxbits)
    left = _left_after_counts(counts, maxbits)
    if left == 0:
        return lens
    if left < 0:
        # ここに来ない想定だが保険
        lens = fix_lengths_kraft(lens, maxbits)
        counts = _build_bit_counts(lens, maxbits)
        left = _left_after_counts(counts, maxbits)

    # left > 0 の場合、ゼロ長のシンボルに maxbits を付与して埋める
    if reserved is None:
        reserved = set()
    # 既存配列内のゼロ長から優先的に使う（HLIT/HDIST を無闇に伸ばさない）
    for idx in range(len(lens)):
        if left == 0:
            break
        if idx in reserved:
            continue
        if lens[idx] == 0:
            lens[idx] = maxbits
            left -= 1
    # まだ残れば、末尾を伸ばして付与
    while left > 0:
        idx = len(lens)
        if idx in reserved:
            # まずは次の index を探す
            lens.append(0);  # 1 つ空けて次へ
            continue
        lens.append(maxbits)
        left -= 1
    return lens

def _collect_used_litlen_syms(tokens: List["Token"]) -> set:
    used = {256}  # EOB は必須
    for t in tokens:
        if isinstance(t, LitToken):
            used.add(t.lit & 0x1FF)  # 0..255
        else:
            lcode, _, _ = _length_to_code_and_extra_for_dump(t.length)
            used.add(lcode)  # 257..285
    return used

def _collect_used_dist_syms(tokens: List["Token"]) -> set:
    used = set()
    for t in tokens:
        if isinstance(t, MatchToken):
            dcode, _, _ = _distance_to_code_and_extra_for_dump(t.distance)
            used.add(dcode)  # 0..29
    # 距離が 1 件も無い場合は空集合でよい（後段の ensure が最低 1 記号非 0 を担保）
    return used


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
        if _left_after_counts(_build_bit_counts(self.litlen_code.lengths, 15), 15) != 0:
            raise ValueError("Litlen code lengths do not satisfy the complete tree condition (left != 0).")
        if _left_after_counts(_build_bit_counts(self.dist_code.lengths, 15), 15) != 0:
            raise ValueError("Distance code lengths do not satisfy the complete tree condition (left != 0).")

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
):
    # --- 既存の安全化 ---
    litlen, dist = _ensure_eob_and_dist(litlen_lengths, dist_lengths)

    # ★ ここで reserved を用意：実際に使うシンボルはなるべく弄らない
    #   （length 値そのものは触れても良いが、ゼロ化したり極端に短くすると
    #     実データの符号長が激変するため）
    used_lit = _collect_used_litlen_syms(tokens=[])  # ← 呼び出しサイトで正しく渡せない場合の保険
    used_dist = set()

    # ここは後述の DynamicHuffmanBlock.dump()/builder から呼ぶときに
    # 正しく tokens を渡して上書きします。既存の呼び出しが tokens を知らない
    # 場合は EOB だけでも reserved になっていれば最低限は安全です。

    # 一旦 Kraft を満たす（oversubscribe 回避）
    litlen = fix_lengths_kraft(litlen, 15)
    dist   = fix_lengths_kraft(dist, 15)

    # --- complete 化（left==0 になるよう穴を埋める）---
    litlen = _make_tree_complete(litlen, 15, reserved=used_lit)
    dist   = _make_tree_complete(dist,   15, reserved=used_dist)

    # 後端ゼロ切詰め → HLIT/HDIST
    litlen_eff, dist_eff, num_litlen, num_dist = _cut_and_indices(litlen, dist)
    hlit  = num_litlen - 257
    hdist = num_dist   - 1

    # RLE 生成
    rle_stream = rle_code_lengths_stream(litlen_eff, dist_eff)

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

    # ★ CL も complete 化（保険：zlib は CL 不完全にも比較的寛容だが、揃えておく）
    cl_lengths = _make_tree_complete(cl_lengths, 7, reserved=None)

    cl_codec = DynamicHuffmanCodeLengthCode(cl_lengths)

    return litlen_eff, dist_eff, hlit, hdist, cl_codec, hclen, rle_stream

# =========================================================
# DynamicHuffmanBlock
# =========================================================

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
    base_bytes = dumps(base_block)
    base_score = score_func(base_bytes)

    orig = base_block.bfinal
    base_block.bfinal = 1
    orig_bytes = zlib.decompress(dumps(base_block), wbits=-15)
    base_block.bfinal = orig 

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
        cand_bytes = dumps(cand_block)

        cand_block.bfinal=1
        decompable_bytes = dumps(cand_block)
        assert zlib.decompress(decompable_bytes, wbits=-15) == orig_bytes
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

import heapq
from itertools import count
from io import StringIO
from dataclasses import dataclass
from typing import Optional

from deflate_optimizer.bitio import BitReader, BitWriter
from deflate_optimizer.blocks import Block, Token, LitToken, MatchToken
from deflate_optimizer.blocks.huffman import dump_tokens, load_tokens
from deflate_optimizer.huffman import FastHuffman

CL_ORDER = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]


def rle_code_lengths_stream(litlen: list[int], dist: list[int], allow_16=True, allow_17=True, allow_18=True) -> list[tuple[int,int,int]]:
    """
    litlen + dist のコード長列を RFC1951 の RLE で列挙。
    返値は (symbol, extra_value, extra_bits):
      - 0..15 : そのままコード長値
      - 16    : 直前の長さを 3..6 回繰り返す（2 ビットで回数-3 を表す）
      - 17    : 0 を 3..10 回
      - 18    : 0 を 11..138 回
    """
    seq = list(litlen) + list(dist)
    out: list[tuple[int,int,int]] = []
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


@dataclass
class DynamicHuffmanCodeLengthCode:
    lengths: list[int]
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
class DynamicHuffmanHeader:
    hlit: int
    hdist: int
    hclen: int
    cl_code: DynamicHuffmanCodeLengthCode
    litlen_code: FastHuffman
    dist_code: FastHuffman

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
        seq: list[int] = []
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
            cl_code=cl_code, litlen_code=FastHuffman(litlen_lengths), dist_code=FastHuffman(dist_lengths)
        )
        return header

    def dump(self, bw: "BitWriter") -> None:
        if len(self.litlen_code.lengths) < 257 or self.litlen_code.lengths[256] <= 0:
            raise ValueError("EOB (256) must have a non-zero code length and at least 257 litlen lengths are required.")

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

    def dump_string(self, tw):
        print(' '.join(str(l) for l in self.cl_code.lengths), file=tw)
        print(self.hlit + 257, file=tw)
        print(' '.join(str(l) for l in self.litlen_code.lengths), file=tw)
        print(self.hdist + 1, file=tw)
        print(' '.join(str(l) for l in self.dist_code.lengths), file=tw)
        assert len(self.litlen_code.lengths) == self.hlit + 257
        assert len(self.dist_code.lengths) == self.hdist + 1

@dataclass
class DynamicHuffmanBlock(Block):
    bfinal: int
    header: DynamicHuffmanHeader
    tokens: list[Token]

    @staticmethod
    def load(br: BitReader) -> "DynamicHuffmanBlock":
        blk = Block.load(br)
        if not isinstance(blk, DynamicHuffmanBlock):
            raise ValueError("Expected DynamicHuffmanBlock")
        return blk

    @staticmethod
    def load_from_body(br: BitReader, bfinal: int) -> "DynamicHuffmanBlock":
        header = DynamicHuffmanHeader.load(br)
        # dist = header.dist_code
        # if not any(l > 0 for l in dist.lengths):
        #     raise ValueError("Distance tree has no codes")
        toks = load_tokens(br, header.litlen_code, header.dist_code)
        return DynamicHuffmanBlock(bfinal=bfinal, header=header, tokens=toks)

    def dump(self, bw: BitWriter) -> None:
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b10, 2)

        # --- 以降は既存どおり ---
        self.header.dump(bw)
        dump_tokens(bw, self.tokens, self.header.litlen_code, self.header.dist_code)

    def dump_string(self, tw):
        print(self.bfinal, 0b10, file=tw)
        self.header.dump_string(tw)
        print(len(self.tokens), file=tw)
        def convert(tok):
            if isinstance(tok, LitToken):
                return f'L {tok.lit}'
            elif isinstance(tok, MatchToken):
                return f'M {tok.length} {tok.distance}'
            else:
                raise ValueError("Unknown token type")
        print(' '.join(convert(tok) for tok in self.tokens), file=tw)

    @staticmethod
    def load_from_text(tw: StringIO, bfinal: int) -> "DynamicHuffmanBlock":
        # 1) code-length アルファベットの長さ列 (length=19)
        line = tw.readline()
        if not line:
            raise ValueError("Unexpected EOF while reading CL lengths")
        cl_lengths = [int(x) for x in line.strip().split()]
        if len(cl_lengths) != 19:
            raise ValueError("CL lengths count mismatch")
        # 2) HLIT + 257 と litlen 長さ列
        line = tw.readline()
        if not line:
            raise ValueError("Unexpected EOF while reading HLIT")
        num_litlen = int(line.strip())
        if num_litlen < 257:
            raise ValueError("num_litlen must be >= 257")
        litlen_line = tw.readline()
        if not litlen_line:
            raise ValueError("Unexpected EOF while reading litlen lengths")
        litlen_lengths = [int(x) for x in litlen_line.strip().split()]
        if len(litlen_lengths) != num_litlen:
            raise ValueError("litlen lengths count mismatch")
        if litlen_lengths[256] == 0:
            raise ValueError("EOB(256) must have non-zero code length")

        # 3) HDIST + 1 と dist 長さ列
        line = tw.readline()
        if not line:
            raise ValueError("Unexpected EOF while reading HDIST")
        num_dist = int(line.strip())
        if num_dist < 1:
            raise ValueError("num_dist must be >= 1")
        dist_line = tw.readline()
        if not dist_line:
            raise ValueError("Unexpected EOF while reading dist lengths")
        dist_lengths = [int(x) for x in dist_line.strip().split()]
        if len(dist_lengths) != num_dist:
            raise ValueError("dist lengths count mismatch")

        # 4) トークン数とトークン列
        line = tw.readline()
        if not line:
            raise ValueError("Unexpected EOF while reading token count")
        tok_count = int(line.strip())
        toks_line = tw.readline()
        if tok_count == 0:
            tokens: list[Token] = []
        else:
            if not toks_line:
                raise ValueError("Unexpected EOF while reading tokens")
            words = toks_line.strip().split()
            tokens: list[Token] = []
            i = 0
            while i < len(words):
                tag = words[i]
                if tag == 'L':
                    if i + 1 >= len(words):
                        raise ValueError("Malformed literal token")
                    lit = int(words[i + 1])
                    tokens.append(LitToken(lit))
                    i += 2
                elif tag == 'M':
                    if i + 2 >= len(words):
                        raise ValueError("Malformed match token")
                    length = int(words[i + 1])
                    distance = int(words[i + 2])
                    tokens.append(MatchToken(length, distance))
                    i += 3
                else:
                    raise ValueError(f"Unknown token tag {tag!r}")
            if len(tokens) != tok_count:
                raise ValueError("Token count mismatch")

        # 5) ヘッダ構築
        hlit = num_litlen - 257
        hdist = num_dist - 1

        rle_codes = rle_code_lengths_stream(litlen_lengths, dist_lengths)
        cl_bins = [0]*19
        for sym, _, _ in rle_codes:
            cl_bins[sym] += 1

        # make Huffman tree for CL
        ctr = count()
        heap = [(freq, next(ctr), sym) for sym, freq in enumerate(cl_bins) if freq > 0]
        heapq.heapify(heap)
        while len(heap) > 1:
            f1, _, n1 = heapq.heappop(heap)
            f2, _, n2 = heapq.heappop(heap)
            merged = (n1, n2)
            heapq.heappush(heap, (f1 + f2, next(ctr), merged))
        root = heap[0][2] if heap else None
        cl_lengths = [0] * 19
        def assign_cl_lengths(node, depth):
            if isinstance(node, int):
                cl_lengths[node] = depth
            else:
                left, right = node
                assign_cl_lengths(left, depth + 1)
                assign_cl_lengths(right, depth + 1)
        if root is not None:
            if isinstance(root, int):
                cl_lengths[root] = 1
            else:
                assign_cl_lengths(root, 0)

        print(f'cl_lengths: {cl_lengths}')
        print(f'litlen_lengths: {litlen_lengths}')
        print(f'dist_lengths: {dist_lengths}')
        print(f'rle_codes: {rle_codes}')

        hclen = 15  # 19 個すべてを出力
        cl_code = DynamicHuffmanCodeLengthCode(cl_lengths)
        header = DynamicHuffmanHeader(
            hlit=hlit,
            hdist=hdist,
            hclen=hclen,
            cl_code=cl_code,
            litlen_code=FastHuffman(litlen_lengths),
            dist_code=FastHuffman(dist_lengths),
        )

        return DynamicHuffmanBlock(bfinal=bfinal, header=header, tokens=tokens)
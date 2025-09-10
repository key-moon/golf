from io import StringIO
from dataclasses import dataclass
from deflate_optimizer.bitio import BitReader, BitWriter
from deflate_optimizer.blocks import Block, Token, LitToken, MatchToken
from deflate_optimizer.blocks.huffman import dump_tokens, load_tokens

from deflate_optimizer.huffman import FastHuffman

def _fixed_litlen_lengths() -> list[int]:
    lens = [0]*288  # 0..287
    for s in range(0, 144):   lens[s] = 8
    for s in range(144, 256): lens[s] = 9
    for s in range(256, 280): lens[s] = 7
    for s in range(280, 288): lens[s] = 8
    return lens

def _fixed_dist_lengths() -> list[int]:
    lens = [5]*32  # 0..31
    return lens

STATIC_LITLEN_CODEC, STATIC_DIST_CODEC = FastHuffman(_fixed_litlen_lengths()), FastHuffman(_fixed_dist_lengths())

@dataclass
class FixedHuffmanBlock(Block):
    """固定ハフマン (BTYPE=01)"""
    tokens: list[Token]

    @staticmethod
    def load_from_body(br: BitReader, bfinal: int) -> "FixedHuffmanBlock":
        toks = load_tokens(br, STATIC_LITLEN_CODEC, STATIC_DIST_CODEC)
        return FixedHuffmanBlock(bfinal=bfinal, tokens=toks)

    def dump(self, bw: BitWriter) -> None:
        # ヘッダ
        bw.write_bits(self.bfinal & 1, 1)
        bw.write_bits(0b01, 2)
        dump_tokens(bw, self.tokens, STATIC_LITLEN_CODEC, STATIC_DIST_CODEC)

    def dump_string(self, tw):
        print(self.bfinal, 0b01, file=tw)
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
    def load_from_text(tw: StringIO, bfinal: int) -> "FixedHuffmanBlock":
        len_str = tw.readline().strip()
        length = int(len_str)
        tokens = []
        i = 0
        parts = tw.readline().strip().split()
        while i < length:
            if parts[i] == 'L':
                lit = int(parts[i+1])
                tokens.append(LitToken(lit=lit))
                i += 2
            elif parts[i] == 'M':
                length = int(parts[i+1])
                distance = int(parts[i+2])
                tokens.append(MatchToken(length=length, distance=distance))
                i += 3
            else:
                raise ValueError("Unknown token type in text")
        if len(tokens) != length:
            raise ValueError("FixedHuffman block token length mismatch")
        return FixedHuffmanBlock(bfinal=bfinal, tokens=tokens)

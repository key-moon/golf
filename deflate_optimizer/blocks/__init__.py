from io import StringIO
from abc import ABC, abstractmethod
from dataclasses import dataclass

from deflate_optimizer.bitio import BitReader, BitWriter

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
    def dump(self, bw: BitWriter) -> None:
        raise NotImplementedError
    
    @staticmethod
    def load_from_text(tw: StringIO) -> "Block":
        import deflate_optimizer.blocks.stored
        import deflate_optimizer.blocks.fixed_huffman
        import deflate_optimizer.blocks.dynamic_huffman
        bfinal_str, btype_str = tw.readline().strip().split()
        bfinal = int(bfinal_str)
        btype = int(btype_str)
        if btype == 0b10:
            return deflate_optimizer.blocks.dynamic_huffman.DynamicHuffmanBlock.load_from_text(tw, bfinal)
        elif btype == 0b01:
            return deflate_optimizer.blocks.fixed_huffman.FixedHuffmanBlock.load_from_text(tw, bfinal)
        elif btype == 0b00:
            return deflate_optimizer.blocks.stored.StoredBlock.load_from_text(tw, bfinal)
        else:
            raise ValueError("Invalid reserved BTYPE=0b11")


    @staticmethod
    def load(br: BitReader) -> "Block":
        import deflate_optimizer.blocks.stored
        import deflate_optimizer.blocks.fixed_huffman
        import deflate_optimizer.blocks.dynamic_huffman
        bfinal = br.read_bit()
        btype = br.read_bits(2)
        if btype == 0b10:
            return deflate_optimizer.blocks.dynamic_huffman.DynamicHuffmanBlock.load_from_body(br, bfinal)
        elif btype == 0b01:
            return deflate_optimizer.blocks.fixed_huffman.FixedHuffmanBlock.load_from_body(br, bfinal)
        elif btype == 0b00:
            return deflate_optimizer.blocks.stored.StoredBlock.load_from_body(br, bfinal)
        else:
            raise ValueError("Invalid reserved BTYPE=0b11")

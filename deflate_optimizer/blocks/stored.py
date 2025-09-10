from io import StringIO
from dataclasses import dataclass
from deflate_optimizer.blocks import Block
from deflate_optimizer.bitio import BitReader, BitWriter

@dataclass
class StoredBlock(Block):
    """非圧縮ブロック (BTYPE=00)。"""
    data: bytes  # 生データ

    @staticmethod
    def load_from_body(br: BitReader, bfinal: int) -> "StoredBlock":
        # 仕様：BTYPE=00 の直後にバイト境界に合わせる
        br.align_to_next_byte()
        # LEN / NLEN (16-bit, little-endian)
        length = br.read_bits(16)
        nlen   = br.read_bits(16)
        if (length ^ nlen) != 0xFFFF:
            raise ValueError("Stored block LEN/NLEN mismatch")
        payload = br.read_bytes(length)
        return StoredBlock(bfinal=bfinal, data=payload)

    def dump(self, bw: BitWriter) -> None:
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
    
    def dump_string(self, tw):
        print(self.bfinal, 0b00, file=tw)
        print(len(self.data), file=tw)
        print(' '.join(f'{int(b)}' for b in self.data), file=tw)
    
    @staticmethod
    def load_from_text(tw: StringIO, bfinal: int) -> "StoredBlock":
        len_str = tw.readline().strip()
        length = int(len_str)
        data_str = tw.readline().strip()
        byte_vals = list(map(int, data_str.split()))
        if len(byte_vals) != length:
            raise ValueError("Stored block length mismatch")
        data = bytes(byte_vals)
        return StoredBlock(bfinal=bfinal, data=data)

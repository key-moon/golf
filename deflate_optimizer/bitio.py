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

    def write_bytes(self, data: bytes) -> None:
        for byte in data:
            self.write_bits(byte, 8)

    def concatinate(self, other: "BitWriter") -> None:
        self.write_bytes(other._buf)
        self.write_bits(other._bitbuf, other._bitcnt)

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

def dumps(dumpable) -> bytes:
    bw = BitWriter()
    dumpable.dump(bw)
    return bw.get_bytes()

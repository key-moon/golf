from .bitio import BitReader, BitWriter

def reverse_bits(x: int, nbits: int) -> int:
    r = 0
    for _ in range(nbits):
        r = (r << 1) | (x & 1)
        x >>= 1
    return r

def last_nonzero_index(a: list[int]) -> int:
    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            return i
    return -1

def kraft_overflow(lengths: list[int]) -> bool:
    total = 0.0
    for l in lengths:
        if l > 0:
            total += 1.0 / (1 << l)
            if total > 1.0 + 1e-12:
                return True
    return False

def fix_lengths_kraft(lengths: list[int], maxbits: int):
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

def _check_huffman_lengths(lengths: list[int], maxbits: int):
    bit_counts = [0]*(maxbits+1)
    for l in lengths:
        if 0 < l <= maxbits:
            bit_counts[l] += 1
    
    left_after_counts = 1
    for bits in range(1, maxbits+1):
        left_after_counts <<= 1
        left_after_counts -= bit_counts[bits] if bits < len(bit_counts) else 0
    return left_after_counts == 0

def ensure_valid_huffman_lengths(lengths: list[int], maxbits: int):
    if not _check_huffman_lengths(lengths, maxbits):
        raise ValueError("Litlen code lengths do not satisfy the complete tree condition (left != 0).")

class FastHuffman:
    __slots__ = ("enc_map","dec_table","maxbits","mask")
    def __init__(self, lengths: list[int]):
        self.maxbits = maxbits = max(lengths)
        self.mask = (1 << maxbits) - 1
        pairs = [(l, s) for s, l in enumerate(lengths) if l > 0]
        if not pairs:
            raise ValueError("Huffman must have at least one non-zero length")
        pairs.sort()
        maxlen = max(l for l, _ in pairs)

        bl_count = [0]*(maxlen+1)
        for l, _ in pairs: bl_count[l] += 1
        next_code = [0]*(maxlen+1)
        code = 0
        for bits in range(1, maxlen+1):
            code = (code + bl_count[bits-1]) << 1
            next_code[bits] = code

        enc_map: dict[int, tuple[int,int]] = {}
        for length, sym in pairs:
            c = next_code[length]
            next_code[length] += 1
            enc_map[sym] = (reverse_bits(c, length), length)

        size = 1 << maxbits
        dec_table: list[tuple[int,int]] = [(-1, 0)] * size
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
        bits = br.peek_bits(self.maxbits, allow_zerofill=True)
        sym, n = self.dec_table[bits & self.mask]
        if n == 0 or sym < 0:
            raise ValueError("invalid Huffman prefix")
        br.drop_bits(n)  # drop は厳格（ここでは実在ビット数）
        return sym

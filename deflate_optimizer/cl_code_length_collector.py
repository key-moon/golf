
# /dist/task*.py のzlib payloadを読んでcl code lengthsを集計する
# #coding:L1 から始まるファイルを探し、
# coding:L1
# import zlib
# exec(zlib.decompress(bytes('}��0���#�kC,{�F[��f-��-D�߿�۩Th���C��S�u  ���!�!����VY?奰,X/@��˞��k2F�"�� ;B[i:���Y��I���R,)Hھ��1�/o�7�z�ӓ[V��-�J���ߐ����AD�6<�i��l�57}����dc�2��_','L1'),-9))


import ast
import re
from pathlib import Path

from deflate_optimizer.bitio import BitReader
from deflate_optimizer.blocks import Block
from deflate_optimizer.blocks.dynamic_huffman import DynamicHuffmanBlock
from deflate_optimizer.rle_dp_helper import RLE_DP_TABLE
from utils import viz_deflate_url

pat = re.compile(
    r"""
    exec\(\s*zlib\.decompress\(\s*          # exec(zlib.decompress(
        bytes\(\s*                          # bytes(
            (["'])                          # 1: 開始クオート
            (.*?)                           # 2: 文字列本体
            \1\s*,\s*                       # 同じクオートで閉じてからカンマ
            (?:L1|["']L1["'])               # L1 または "L1"
        \)\s*,\s*                           # ) , 
        ([-+]?\d+)                          # 3: wbits 値 例 -9
    \)\s*\)                                 # ))
    """,
    re.S | re.X
)

if __name__ == "__main__":
    cnt = 0
    for path in sorted(Path("dist").glob("task*.py")):
        with open(path, "r", encoding="l1", newline="") as f:
            src = f.read()
        if not src.startswith("#coding:L1"):
            continue

        m = pat.search(src)
        if not m:
            continue
        # 文字列リテラル部分を安全に評価して str を得る
        literal_with_quotes = m.group(1) + m.group(2) + m.group(1)
        s = ast.literal_eval(literal_with_quotes)       # str
        payload = s.encode("l1")                   # 実行時の bytes と同一

        wbits = int(m.group(3))
        if wbits >= 0:
            raise ValueError(f"Unsupported wbits={wbits} in {path}")

        reader = BitReader(payload)
        block_index = 0
        while True:
            block = Block.load(reader)
            if isinstance(block, DynamicHuffmanBlock):
                cl_lengths = block.header.cl_code.lengths
                litlen_lengths = block.header.litlen_code.lengths
                dist_lengths = block.header.dist_code.lengths

                # length/dist codeのRLE-encoded 表現を得る
                rle_stream = RLE_DP_TABLE.rle_code_lengths_stream(
                    litlen_lengths,
                    dist_lengths,
                    cl_lengths
                )
                # print(litlen_lengths + dist_lengths)
                rle_stream_freq = [0] * 19
                for sym, *_ in rle_stream:
                    rle_stream_freq[sym] += 1


                rle_bit_length = sum(cl_lengths[sym] + extra_bits for sym, _, extra_bits in rle_stream)
                print(path.name, end="  ")
                print(' '.join([f"{l:>2d}" for l in cl_lengths]))
                print(' ' * len(path.name), end="  ")
                print(' '.join([f"{l:>2d}" for l in rle_stream_freq]))
                # print(' '.join(map(str, rle_stream)))
                # print(' '.join(map(lambda x: str(x[0]), rle_stream)))
                print(rle_bit_length)
                print()
            if block.bfinal:
                break
            block_index += 1
        # print(viz_deflate_url(payload))
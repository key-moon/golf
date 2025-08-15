# 壊れた木を修正するやつ chatgptが吐いてきたけどなくても動く（validな摂動しかしないので）
# ---- 追加: zlib と同等の left 判定（不完全 / 過剰） ----
from typing import Optional

def _build_bit_counts(lengths: list[int], maxbits: int) -> list[int]:
    cnt = [0]*(maxbits+1)
    for l in lengths:
        if 0 < l <= maxbits:
            cnt[l] += 1
    return cnt

def _left_after_counts(counts: list[int], maxbits: int) -> int:
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

def _make_tree_complete(lengths: list[int],
                        maxbits: int,
                        reserved: Optional[set] = None) -> list[int]:
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

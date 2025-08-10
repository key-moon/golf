from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List, Tuple, Optional
import os
import math
import random

# =========================
# 64-bit SplitMix ハッシュ
# =========================

def splitmix64(x: int) -> int:
    """Deterministic 64-bit mixer (SplitMix64)."""
    x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    z = x
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & 0xFFFFFFFFFFFFFFFF
    z = (z ^ (z >> 27)) * 0x94D049BB133111EB & 0xFFFFFFFFFFFFFFFF
    z = z ^ (z >> 31)
    return z & 0xFFFFFFFFFFFFFFFF

def mix64_u128(x: int, seed: int) -> int:
    """Mix a 64-bit key x with a 64-bit seed → 64-bit hash."""
    return splitmix64(x ^ seed)

# ======================================
# 3インデックス生成（XORフィルタ用の位置）
# ======================================

def _idxs_from_hash(h: int, mask: int) -> Tuple[int, int, int]:
    """
    64-bit h から 3 つのインデックスを抽出。
    マスクは (table_size-1) を想定（テーブルサイズはパワーオブツー）。
    """
    # 3 つの 21-bit チャンクを切り出して mod 2^k に落とす
    # （小さめテーブルでも均一性は十分）
    i0 = (h        ) & mask
    i1 = (h >> 21) & mask
    i2 = (h >> 42) & mask
    return i0, i1, i2

# ===========================
# f-bit 指紋値の抽出（0..2^f-1）
# ===========================

def fingerprint_fbits(h: int, f: int) -> int:
    """下位 f ビットを指紋として用いる（f==0 は禁止）。"""
    if f <= 0 or f > 32:
        raise ValueError("f must be in [1..32]")
    return (h & ((1 << f) - 1))

# ===========================
# ビットパックされた配列
# ===========================

class BitPackedArray:
    """
    要素幅 bit_width ビットの固定長配列（要素数 length）をビットパックして格納。
    set/get と XOR フィルタ用に必要十分な機能を用意。
    """
    __slots__ = ("length", "bit_width", "_buf")

    def __init__(self, length: int, bit_width: int):
        if length < 0:
            raise ValueError("length must be non-negative")
        if bit_width <= 0:
            raise ValueError("bit_width must be positive")
        self.length = length
        self.bit_width = bit_width
        total_bits = length * bit_width
        buf_bytes = (total_bits + 7) // 8
        self._buf = bytearray(buf_bytes)

    def _bounds_check(self, idx: int):
        if not (0 <= idx < self.length):
            raise IndexError("index out of range")

    def get(self, idx: int) -> int:
        self._bounds_check(idx)
        bw = self.bit_width
        start_bit = idx * bw
        byte_pos = start_bit >> 3
        bit_off = start_bit & 7
        # 読み取りに必要なビット数を満たすだけバイトを読み、整形
        needed = (bit_off + bw + 7) >> 3
        val = 0
        for j in range(needed):
            val |= self._buf[byte_pos + j] << (8 * j)
        val >>= bit_off
        mask = (1 << bw) - 1
        return val & mask

    def set(self, idx: int, value: int):
        self._bounds_check(idx)
        bw = self.bit_width
        if value < 0 or value >= (1 << bw):
            raise ValueError("value out of range for bit_width")
        start_bit = idx * bw
        byte_pos = start_bit >> 3
        bit_off = start_bit & 7
        needed = (bit_off + bw + 7) >> 3
        # 現在値のある領域を読み込み→そのビット範囲のみ上書き
        cur = 0
        for j in range(needed):
            cur |= self._buf[byte_pos + j] << (8 * j)
        mask = ((1 << bw) - 1) << bit_off
        cur = (cur & ~mask) | ((value << bit_off) & mask)
        for j in range(needed):
            self._buf[byte_pos + j] = (cur >> (8 * j)) & 0xFF

    def xor_into(self, idx: int, value: int):
        """ arr[idx] ^= value """
        self.set(idx, self.get(idx) ^ value)

    def nbytes(self) -> int:
        return len(self._buf)

    def raw_bytes(self) -> bytes:
        return bytes(self._buf)

# ===========================
# XOR フィルタ本体
# ===========================

@dataclass
class XorFilter:
    """
    XOR フィルタ（3本ハッシュ）。静的集合の membership を近似判定。
    - 偽陰性 0（格納した要素は必ず "probably present" になる）
    - 偽陽性 あり（確率 ≈ 2^-f）
    """
    f_bits: int                 # 指紋のビット幅（false positive ≈ 2^-f）
    seed_pos: int               # 位置計算用シード
    seed_fp: int                # 指紋計算用シード（位置とは分離）
    size_mask: int              # テーブルサイズ-1（パワーオブツーサイズ用）
    table: BitPackedArray       # f_bits 幅のビットパック配列（サイズ = table_size）

    @property
    def table_size(self) -> int:
        return self.size_mask + 1

    @property
    def bytes_used(self) -> int:
        # bpk = (table_size * f_bits) / n が目標。ここでは総バイト数を返す。
        return self.table.nbytes()

    # ------------- 構築 -------------

    @staticmethod
    def _next_pow2(x: int) -> int:
        if x <= 1:
            return 1
        return 1 << (x - 1).bit_length()

    @classmethod
    def build(cls, keys: Iterable[int], f_bits: int = 20, load_factor: float = 1.23,
              max_attempts: int = 50, table_size=-1, seed: Optional[int] = None) -> "XorFilter":
        """
        keys: 64-bit 整数反復可能オブジェクト（重複は除去される）
        f_bits: 指紋ビット幅（false positive ≈ 2^-f_bits）
        load_factor: テーブルサイズ / |keys| の目安（~1.23 が定石）
        max_attempts: リトライ回数（サイクルが消えない場合にシード替え）
        seed: 省略時は OS 乱数から

        構築に成功すると XOR フィルタを返す。失敗時は RuntimeError。
        """
        key_list = sorted(set(int(k) & 0xFFFFFFFFFFFFFFFF for k in keys))
        n = len(key_list)
        if n == 0:
            raise ValueError("keys must be non-empty")
        if f_bits <= 0 or f_bits > 32:
            raise ValueError("f_bits must be in [1..32]")

        # テーブルサイズは 2 の冪に切り上げ（高速化のため）
        target_size = max(int(math.ceil(n * load_factor)), 1)
        table_size = table_size if table_size != -1 else cls._next_pow2(target_size)
        mask = table_size - 1

        # 構築ループ（ハイパーグラフのサイクルが消えるまでシードを振り直す）
        base_seed = seed if seed is not None else int.from_bytes(os.urandom(8), "little")

        for attempt in range(max_attempts):
            seed_pos = splitmix64(base_seed + attempt)   # 位置計算用シード
            seed_fp  = splitmix64(base_seed + attempt + 0x9E3779B97F4A7C15)  # 指紋用

            # 各 key の 3 位置を先に計算して保存
            positions: List[Tuple[int, int, int]] = []
            deg = [0] * table_size
            for x in key_list:
                h = mix64_u128(x, seed_pos)
                i0, i1, i2 = _idxs_from_hash(h, mask)
                positions.append((i0, i1, i2))
                deg[i0] += 1; deg[i1] += 1; deg[i2] += 1

            # 各頂点に接続するエッジ（key index）リスト
            # 小規模なので単純な構築で十分速い
            incident: List[List[int]] = [[] for _ in range(table_size)]
            for idx, (a, b, c) in enumerate(positions):
                incident[a].append(idx)
                incident[b].append(idx)
                incident[c].append(idx)

            # 取り除き順（peeling オーダ）を記録
            stack: List[Tuple[int, int]] = []  # (key_index, vertex_selected)
            from collections import deque
            q = deque(i for i, d in enumerate(deg) if d == 1)

            removed_edge = [False] * n
            left_edges = n

            while q:
                v = q.popleft()
                if deg[v] != 1:
                    continue
                # v に接続する、まだ残っているエッジ（key）を探す
                for e in incident[v]:
                    if removed_edge[e]:
                        continue
                    a, b, c = positions[e]
                    # e を取り除く
                    removed_edge[e] = True
                    left_edges -= 1
                    stack.append((e, v))
                    # 3 頂点の次数を減らし、1 になったらキューへ
                    for u in (a, b, c):
                        if u == v:
                            continue
                        deg[u] -= 1
                        if deg[u] == 1:
                            q.append(u)
                    deg[v] -= 1  # 最後に自分も 0 へ
                    break  # この頂点からは 1 エッジだけのはず

            if left_edges != 0:
                # サイクルが残った → 別シードでやり直し
                continue

            # ここに来れば peeling 成功。逆順で fingerprint を割り当てる
            table = BitPackedArray(table_size, f_bits)

            def get_fp(x: int) -> int:
                return fingerprint_fbits(mix64_u128(x, seed_fp), f_bits)

            # すでに埋まっている頂点の fingerprint を XOR して、残り1つを決定
            for e, chosen_v in reversed(stack):
                a, b, c = positions[e]
                x = key_list[e]
                fp = get_fp(x)
                # chosen_v 以外を特定
                if chosen_v == a:
                    o1, o2 = b, c
                elif chosen_v == b:
                    o1, o2 = a, c
                else:
                    o1, o2 = a, b
                val = fp ^ table.get(o1) ^ table.get(o2)
                table.set(chosen_v, val)

            # 成功
            return cls(
                f_bits=f_bits,
                seed_pos=seed_pos,
                seed_fp=seed_fp,
                size_mask=mask,
                table=table
            )

        raise RuntimeError("Failed to build XOR filter after max_attempts; try different seeds or load_factor.")

    # ------------- クエリ -------------

    def contains(self, x: int) -> bool:
        """Membership の近似判定：True=多分含む / False=含まない。偽陰性は原理的に 0。"""
        x &= 0xFFFFFFFFFFFFFFFF
        hpos = mix64_u128(x, self.seed_pos)
        i0, i1, i2 = _idxs_from_hash(hpos, self.size_mask)
        fp  = fingerprint_fbits(mix64_u128(x, self.seed_fp), self.f_bits)
        return (self.table.get(i0) ^ self.table.get(i1) ^ self.table.get(i2)) == fp

    # ------------- 補助 -------------

    def stats(self, n_keys: int) -> dict:
        """メモリや bpk の目安を返す。"""
        total_bits = self.table_size * self.f_bits
        return {
            "table_size": self.table_size,
            "f_bits": self.f_bits,
            "bytes": self.bytes_used,
            "bits": total_bits,
            "bpk": total_bits / float(n_keys),
            "approx_false_positive_rate": 2.0 ** (-self.f_bits)
        }


# ===========================
# 使い方デモ（簡単なテスト）
# ===========================

if __name__ == "__main__":
    random.seed(0xC0FFEE)
    # 小さな 64-bit 整数集合（例：300要素）
    keys = [random.getrandbits(64) for _ in range(90)]

    # 偽陽性 ≈ 2^-20 ≈ 1e-6 程度に設定（必要に応じて f_bits を変える）
    f_bits = 4
    filt = XorFilter.build(keys, f_bits=f_bits, load_factor=1.23, max_attempts=100)

    s = filt.stats(len(keys))
    print((1-s["approx_false_positive_rate"]) ** 180)
    print("XOR Filter stats:", s)

    # 既存要素は必ず True（偽陰性ゼロ）
    assert all(filt.contains(x) for x in keys)

    # ランダム非要素に対して偽陽性率をだいたい確認
    trials = 200000
    fp_cnt = 0
    for _ in range(trials):
        y = random.getrandbits(64)
        if y in keys:
            continue
        if filt.contains(y):
            fp_cnt += 1
    print(f"empirical FPR ~ {fp_cnt / trials:.6f} (target ~ {2**(-f_bits):.6f})")

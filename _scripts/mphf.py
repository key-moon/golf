#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal Perfect Hash Function (MPHF) for static sets of 64-bit integers
- CHD-style (bucket + displacement) construction
- Displacement array is compressed with unsigned LEB128 to minimize bits-per-key (bpk)
- Deterministic: fixed seeds unless specified
- For n ~ 300, typical bpk is around ~3-6 depending on distribution

Usage:
    python mphf_chd.py  # runs self-test

Public API:
    class MPHF:
        @staticmethod
        def build(keys: list[int], nbuckets: int | None = None, seed: int = 0) -> "MPHF"
        def lookup(self, x: int) -> int          # returns index in [0..n-1]
        def contains_exact(self, x: int) -> bool # only if you also pass the original set (optional)
        def serialize(self) -> bytes
        @staticmethod
        def deserialize(data: bytes) -> "MPHF"
        def bits_per_key(self) -> float

Notes:
- This is a minimal perfect hash (no collisions for the given static set). For x ∉ S, lookup(x) も [0..n-1] を返しますが、それは “membership” ではありません（必要なら別にAMQ指紋などを足してください）。
- bpk は displacement 配列の圧縮サイズが主。nbuckets を小さくすると 1 桶あたり要素数が増え、探索の displ が大きくなりがち。大きくしすぎると桶数が増えてメタデータが増えます。n/4 〜 n/8 付近が経験的にバランス良いです。
"""

from __future__ import annotations
from typing import List, Tuple
import struct
import math
import sys
import random

# ------------------------------
# 64-bit mix / splitmix64
# ------------------------------

def _mask64(x: int) -> int:
    return x & 0xFFFFFFFFFFFFFFFF

def splitmix64(x: int) -> int:
    z = _mask64(x + 0x9E3779B97F4A7C15)
    z = _mask64((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9)
    z = _mask64((z ^ (z >> 27)) * 0x94D049BB133111EB)
    return z ^ (z >> 31)

def mix64(x: int, seed: int) -> int:
    # Simple keyed mix: splitmix64(x ^ seed)
    return splitmix64(_mask64(x) ^ _mask64(seed))

# Derive two 64-bit hashes from one:
def hash2(x: int, seed: int) -> Tuple[int, int]:
    h1 = mix64(x, seed)
    h2 = mix64(x, _mask64(seed ^ 0xD6E8FEB86659FD93))
    return h1, h2

# ------------------------------
# Unsigned LEB128 (VarInt) for compact displacement storage
# ------------------------------

def uleb128_encode(u: int) -> bytes:
    if u < 0:
        raise ValueError("uleb128_encode expects non-negative integer")
    out = bytearray()
    while True:
        b = u & 0x7F
        u >>= 7
        if u:
            out.append(b | 0x80)
        else:
            out.append(b)
            break
    return bytes(out)

def uleb128_decode(bs: bytes, offset: int = 0) -> Tuple[int, int]:
    shift = 0
    result = 0
    i = offset
    while True:
        if i >= len(bs):
            raise ValueError("ULEB128 decode overflow")
        b = bs[i]
        i += 1
        result |= ((b & 0x7F) << shift)
        if (b & 0x80) == 0:
            break
        shift += 7
        if shift > 63:
            raise ValueError("ULEB128 too large")
    return result, i

# ------------------------------
# MPHF (CHD-style)
# ------------------------------

class MPHF:
    """
    CHD-style MPHF:
      - Partition keys into nbuckets by h1 % nbuckets
      - Process buckets in descending order of size
      - For a bucket, search smallest displacement d >= 0 such that
            pos_i = (h2_i + d) % n
        are all distinct and unoccupied in the global table.
      - Store d per bucket (compressed with ULEB128).
      - Lookup uses the same formula to get a unique position.

    This produces a perfect permutation of {0..n-1} for the given set.
    """
    # __slots__ = ("n", "nbuckets", "seed", "_disp_bytes", "_bucket_offsets")

    def __init__(self, n: int, nbuckets: int, seed: int,
                 disp_bytes: bytes, bucket_offsets: List[int]) -> None:
        self.n = n
        self.nbuckets = nbuckets
        self.seed = seed
        self._disp_bytes = disp_bytes
        self._bucket_offsets = bucket_offsets  # prefix sum into disp_bytes

    # ---------- Build ----------
    @staticmethod
    def build(keys: List[int], nbuckets: int | None = None, seed: int = 0) -> "MPHF":
        if len(keys) == 0:
            return MPHF(0, 0, seed, b"", [])

        # 1) 重複排除（MPHFの定義域は集合）
        uniq = list(dict.fromkeys(keys))
        if len(uniq) != len(keys):
            raise ValueError("Duplicate keys detected in input set")

        n = len(uniq)
        if nbuckets is None:
            nbuckets = max(1, min(n, n // 6 if n >= 6 else 1))
        nbuckets = max(1, min(nbuckets, n))

        # あとで複数回使うので事前に h1/h2 を引いておく（h2 は mod n は後でやる）
        def _hash2_map(seed_local: int) -> dict[int, int]:
            return {x: (hash2(x, seed_local)[1] % n) for x in uniq}

        # リトライ制御
        MAX_GLOBAL_RETRIES = 128 # シードを変えて全体再構築する最大回数
        # 各バケット内で d を試す上限。n が小さいので 4n 程度で十分現実的
        MAX_D_TRIES_FACTOR = 10

        rng = random.Random(seed ^ 0xC0FFEE1234ABCD)

        for global_try in range(MAX_GLOBAL_RETRIES):
            seed_local = (seed + global_try) & 0xFFFFFFFFFFFFFFFF

            # 2) バケット分割（h1 % nbuckets）
            buckets: List[List[int]] = [[] for _ in range(nbuckets)]
            for x in uniq:
                h1, _ = hash2(x, seed_local)
                b = h1 % nbuckets
                buckets[b].append(x)

            # 3) 大きい順に処理（タイは乱択で崩すとハマりにくい）
            order = list(range(nbuckets))
            order.sort(key=lambda b: (len(buckets[b]), rng.random()), reverse=True)

            used = [False] * n
            slot_of_key: dict[int, int] = {}
            disp_values = [0] * nbuckets
            h2_map = _hash2_map(seed_local)

            fail = False
            max_d_tries = max(1, n * MAX_D_TRIES_FACTOR)

            for bi in order:
                bucket = buckets[bi]
                if not bucket:
                    disp_values[bi] = 0
                    continue

                # 4) このバケットの d 探索を乱択スタートで有界探索
                start_d = rng.randrange(0, n)  # 乱択開始点
                placed = False

                for t in range(max_d_tries):
                    d = (start_d + t) % n
                    positions = []
                    seen_local = set()
                    collision = False
                    for x in bucket:
                        p = (h2_map[x] + d) % n
                        if used[p] or p in seen_local:
                            collision = True
                            break
                        seen_local.add(p)
                        positions.append(p)
                    if not collision:
                        for x, p in zip(bucket, positions):
                            used[p] = True
                            slot_of_key[x] = p
                        disp_values[bi] = d
                        placed = True
                        break

                if not placed:
                    # このシードではこのバケットが置けない → 全体やり直し
                    fail = True
                    break

            if fail:
                # 別シードで再試行
                continue

            # 5) 完了検査
            if len(slot_of_key) != n:
                # 理屈上ここは来ないはずだが、安全のため再試行
                continue

            # 6) ULEB128 で displacement を圧縮・オフセット配列作成
            print(disp_values)
            disp_bytes_parts: List[bytes] = []
            bucket_offsets: List[int] = [0] * (nbuckets + 1)
            offset = 0
            for i in range(nbuckets):
                enc = uleb128_encode(disp_values[i])
                disp_bytes_parts.append(enc)
                bucket_offsets[i] = offset
                offset += len(enc)
            bucket_offsets[nbuckets] = offset
            disp_bytes = b"".join(disp_bytes_parts)

            mph = MPHF(n=n, nbuckets=nbuckets, seed=seed_local,
                    disp_bytes=disp_bytes, bucket_offsets=bucket_offsets)

            # 7) サニティチェック
            for x in uniq:
                if mph.lookup(x) != slot_of_key[x]:
                    # 何か壊れているのでリトライ
                    fail = True
                    break
            if fail:
                continue

            return mph

        # ここまで来たら全リトライ失敗 → パラメータ調整を促す
        raise RuntimeError(
            f"MPHF.build failed after {MAX_GLOBAL_RETRIES} retries. "
            f"Try increasing nbuckets or changing the seed."
        )


    # ---------- Lookup ----------

    def _disp_of_bucket(self, b: int) -> int:
        start = self._bucket_offsets[b]
        end = self._bucket_offsets[b + 1]
        # decode a single ULEB128 at [start:end]
        val, nxt = uleb128_decode(self._disp_bytes, start)
        if nxt != end:
            # Should not happen: we store exactly one varint per bucket
            raise ValueError("Corrupt displacement encoding")
        return val

    def lookup(self, x: int) -> int:
        if self.n == 0:
            raise KeyError("Empty MPHF")
        h1, h2 = hash2(x, self.seed)
        b = h1 % self.nbuckets
        d = self._disp_of_bucket(b)
        return ( (h2 % self.n) + d ) % self.n

    # ---------- (Optional) exact membership check ----------
    # ※ MPHF 単体では membership は判定できない（集合外も 0..n-1 に写る）ので、
    #   厳密な包含判定を行いたい場合は “元のキー列を同じ順序で並べた配列” を持つか、
    #   あるいは別途 fingerprint（AMQ）を併設してください。
    #   ここではオプションとして “順序付きキー配列” を別に持つ例を示します。

    def attach_ordered_keys(self, keys: List[int]) -> None:
        """Optionally attach an array `ordered_keys` so that contains_exact() works in O(1).
        The array must satisfy ordered_keys[lookup(x)] == x for all x in the original set.
        """
        if len(keys) != self.n:
            raise ValueError("ordered_keys length must be n")
        self._ordered_keys = list(keys)  # store a copy

    def contains_exact(self, x: int) -> bool:
        if not hasattr(self, "_ordered_keys"):
            raise RuntimeError("No ordered_keys attached; cannot do exact membership")
        idx = self.lookup(x)
        return self._ordered_keys[idx] == x

    # ---------- Serialization ----------

    def serialize(self) -> bytes:
        """
        Binary format:
          magic (4B) = b'MPHF'
          version (1B) = 1
          n (u32), nbuckets (u32)
          seed (u64)
          disp_len (u32)
          bucket_offsets_len (u32)  # number of entries (nbuckets+1)
          bucket_offsets (u32 * (nbuckets+1))
          disp_bytes (disp_len)
        """
        magic = b"MPHF"
        ver = 1
        header = bytearray()
        header.extend(magic)
        header.extend(struct.pack("<B", ver))
        header.extend(struct.pack("<IIQ", self.n, self.nbuckets, self.seed))
        disp_len = len(self._disp_bytes)
        header.extend(struct.pack("<II", disp_len, len(self._bucket_offsets)))
        # bucket_offsets as u32
        bo_bytes = b"".join(struct.pack("<I", x) for x in self._bucket_offsets)
        return bytes(header) + bo_bytes + self._disp_bytes

    @staticmethod
    def deserialize(data: bytes) -> "MPHF":
        i = 0
        if data[i:i+4] != b"MPHF":
            raise ValueError("Bad magic")
        i += 4
        ver = data[i]
        i += 1
        if ver != 1:
            raise ValueError(f"Unsupported version: {ver}")
        n, nb, seed = struct.unpack_from("<IIQ", data, i)
        i += struct.calcsize("<IIQ")
        disp_len, bo_len = struct.unpack_from("<II", data, i)
        i += struct.calcsize("<II")
        # read bucket offsets
        bucket_offsets = list(struct.unpack_from("<" + "I"*bo_len, data, i))
        i += struct.calcsize("<" + "I"*bo_len)
        disp_bytes = data[i:i+disp_len]
        if len(disp_bytes) != disp_len:
            raise ValueError("Truncated disp_bytes")
        return MPHF(n=n, nbuckets=nb, seed=seed,
                    disp_bytes=disp_bytes, bucket_offsets=bucket_offsets)

    # ---------- Size metrics ----------

    def bits_per_key(self) -> float:
        """
        Counts only the MPHF metadata (displacements + offsets + small header equivalent).
        For fair bpk, you may exclude the small constant header; here we include:
        - disp_bytes
        - bucket_offsets (u32 each)
        and divide by n.
        """
        disp_bits = len(self._disp_bytes) * 8
        offsets_bits = len(self._bucket_offsets) * 4 * 8
        # Note: small header/seeds are negligible for large n; for n~300 they are minor. Exclude them by default.
        return (disp_bits + offsets_bits) / max(1, self.n)

# ------------------------------
# Helpers to build ordered key array
# ------------------------------

def build_ordered_keys(keys: List[int], mph: MPHF) -> List[int]:
    """Given the original key set and an MPHF, produce ordered_keys so that
    ordered_keys[mph.lookup(x)] == x. This enables exact membership checks without extra AMQ.
    """
    arr = [None] * mph.n
    for x in keys:
        arr[mph.lookup(x)] = x
    # Safety
    for i, v in enumerate(arr):
        if v is None:
            raise AssertionError(f"hole at {i}")
    return arr  # type: ignore

# ------------------------------
# Self-test / Example
# ------------------------------

def _demo():
    # Example: random 64-bit keys
    rng = random.Random(42)
    n = 300
    keys = []
    used = set()
    while len(keys) < n:
        x = rng.getrandbits(64)
        if x not in used:
            used.add(x)
            keys.append(x)

    # # Try a couple of nbuckets settings and pick the best (lower bpk)
    # cand_nb = []
    # for div in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    #     nb = max(1, n // div)
    #     cand_nb.append(nb)
    # cand_nb = sorted(set(cand_nb))

    best = None
    best_mph = None
    for nb in range(80, 300):
        try:
            mph = MPHF.build(keys, nbuckets=nb, seed=0)
        except:
            print(f"err: {nb=}")
            continue
        print(f"{nb=}")
        bpk = mph.bits_per_key()
        if (best is None) or (bpk < best):
            best = bpk
            best_mph = mph
        break

    assert best_mph is not None
    mph = best_mph
    print(f"Built MPHF: n={mph.n} nbuckets={mph.nbuckets} bpk={mph.bits_per_key():.3f}")

    # Attach ordered keys for exact membership checks (optional)
    ordered = build_ordered_keys(keys, mph)
    mph.attach_ordered_keys(ordered)

    # Verify minimal perfectness and exact membership
    ok = True
    seen = set()
    for x in keys:
        idx = mph.lookup(x)
        if idx in seen:
            print("collision at", idx)
            ok = False
            break
        seen.add(idx)
        if not mph.contains_exact(x):
            print("membership failed for", x)
            ok = False
            break
    print("Perfect:", ok)

    # Serialize / deserialize round-trip
    print(mph._disp_bytes)
    blob = mph.serialize()
    mph2 = MPHF.deserialize(blob)
    # Note: ordered_keys は別途保存したい場合はアプリ側で扱う（MPHF自体は不要）
    same = True
    for x in keys:
        if mph.lookup(x) != mph2.lookup(x):
            same = False
            break
    print("Serialize round-trip OK:", same)

if __name__ == "__main__":
    _demo()

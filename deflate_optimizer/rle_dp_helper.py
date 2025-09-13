import itertools
from collections import deque
import sys


def _length_rle(vec: list[int]) -> list[tuple[int, int]]:
    if not vec:
        return []
    res = []
    cur = vec[0]
    run = 1
    for x in vec[1:]:
        if x == cur:
            run += 1
        else:
            res.append((cur, run))
            cur = x
            run = 1
    res.append((cur, run))
    return res

class RLETable:
    """
    変更点
    - コンストラクタでは前計算を実行しない
    - 必要に応じて on-demand に DP テーブルを計算しキャッシュする
    - 旧実装と同一のアルゴリズムを compute_* 関数に分割して維持する
    """

    N = 300
    VALID_WIDTHS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    INF = 1 << 60

    def __init__(self):
        # 前計算はしない
        self.table: dict[tuple[int, int], tuple[list[int], list[int]]] = {}
        self.table2: dict[tuple[int, int, int, int], tuple[list[int], list[int]]] = {}

    # --- 個別計算: 非ゼロ値用 ---
    def compute_nonzero_symbol_cost(self, _single_symbol_cost: int, _code_16_cost: int) -> tuple[list[int], list[int]]:
        N = self.N
        INF = self.INF

        single_symbol_cost = _single_symbol_cost if _single_symbol_cost != 0 else INF
        code_16_cost = _code_16_cost if _code_16_cost != 0 else INF
        add_16 = code_16_cost + 2

        dp = [INF] * N
        prev = [INF] * N
        dp[0] = 0

        deq16 = deque()

        def push_monotone(dq, idx, val, arr):
            while dq and arr[dq[-1]] >= val:
                if arr[dq[-1]] > val:
                    dq.pop()
                else:
                    break
            dq.append(idx)

        for j in range(1, N):
            best = INF
            choice = INF

            # literal
            c_lit = dp[j - 1] + single_symbol_cost
            if c_lit < best:
                best = c_lit
                choice = 1

            # PREV_RUN
            if add_16 < INF:
                k_new = j - 3
                if k_new >= 1:
                    push_monotone(deq16, k_new, dp[k_new], dp)
                k_min = j - 6
                while deq16 and deq16[0] < max(1, k_min):
                    deq16.popleft()
                if deq16:
                    k = deq16[0]
                    c16 = dp[k] + add_16
                    if c16 < best:
                        best = c16
                        choice = j - k
            dp[j] = best
            prev[j] = choice

        return dp, prev

    # --- 個別計算: 値0用 ---
    def compute_zero_symbol_cost(
        self,
        _single_symbol_cost: int,
        _code_16_cost: int,
        _code_17_cost: int,
        _code_18_cost: int,
    ) -> tuple[list[int], list[int]]:
        N = self.N
        INF = self.INF

        single_symbol_cost = _single_symbol_cost if _single_symbol_cost != 0 else INF
        code_16_cost = _code_16_cost if _code_16_cost != 0 else INF
        code_17_cost = _code_17_cost if _code_17_cost != 0 else INF
        code_18_cost = _code_18_cost if _code_18_cost != 0 else INF
        add_16 = code_16_cost + 2
        add_17 = code_17_cost + 3
        add_18 = code_18_cost + 7

        dp = [INF] * N
        prev = [INF] * N
        dp[0] = 0

        deq17 = deque()
        deq18 = deque()
        deq16 = deque()

        def push_monotone(dq, idx, val, arr):
            while dq and arr[dq[-1]] >= val:
                if arr[dq[-1]] > val:
                    dq.pop()
                else:
                    break
            dq.append(idx)

        for j in range(1, N):
            best = INF
            choice = INF

            # literal
            c_lit = dp[j - 1] + single_symbol_cost
            if c_lit < best:
                best = c_lit
                choice = 1

            # ZERO_RUN 3..10
            if add_17 < INF:
                k_new = j - 3
                if k_new >= 0:
                    push_monotone(deq17, k_new, dp[k_new], dp)
                k_min = j - 10
                while deq17 and deq17[0] < max(0, k_min):
                    deq17.popleft()
                if deq17:
                    k = deq17[0]
                    c17 = dp[k] + add_17
                    if c17 < best:
                        best = c17
                        choice = j - k

            # ZERO_RUN 11..138
            if add_18 < INF:
                k_new = j - 11
                if k_new >= 0:
                    push_monotone(deq18, k_new, dp[k_new], dp)
                k_min = j - 138
                while deq18 and deq18[0] < max(0, k_min):
                    deq18.popleft()
                if deq18:
                    k = deq18[0]
                    c18 = dp[k] + add_18
                    if c18 < best:
                        best = c18
                        choice = j - k

            # PREV_RUN 3..6
            if add_16 < INF:
                k_new = j - 3
                if k_new >= 1:
                    push_monotone(deq16, k_new, dp[k_new], dp)
                k_min = j - 6
                while deq16 and deq16[0] < max(1, k_min):
                    deq16.popleft()
                if deq16:
                    k = deq16[0]
                    c16 = dp[k] + add_16
                    if c16 < best:
                        best = c16
                        choice = -(j - k)

            dp[j] = best
            prev[j] = choice

        return dp, prev

    # --- 必要なら全候補を前計算するメンバ関数 ---
    def precompute_all_tables(self):
        VALID = self.VALID_WIDTHS
        for a, b in itertools.product(VALID, VALID):
            key = (a, b)
            if key not in self.table:
                self.table[key] = self.compute_nonzero_symbol_cost(a, b)
        for a, b, c, d in itertools.product(VALID, VALID, VALID, VALID):
            key2 = (a, b, c, d)
            if key2 not in self.table2:
                self.table2[key2] = self.compute_zero_symbol_cost(a, b, c, d)

    # --- 旧インターフェース互換 ---
    def optimal_parse(self, value: int, count: int, cl_lengths: list[int]) -> list[tuple[int, int, int]]:
        INF_CHECK = 1 << 30  # 旧実装のしきい値と合わせる

        if value != 0:
            key = (cl_lengths[value], cl_lengths[16])
            if key not in self.table:
                self.table[key] = self.compute_nonzero_symbol_cost(*key)
            dp, prev = self.table[key]
            if dp[count] >= INF_CHECK:
                raise ValueError(f"DP failed: value={value} count={count} cl_lengths={cl_lengths}")
            i = count
            tmp = []
            while i > 0:
                choice = prev[i]
                if choice == 1:
                    tmp.append((value, 0, 0))
                    i -= 1
                else:
                    run = choice
                    tmp.append((16, run - 3, 2))
                    i -= run
            tmp.reverse()
            return tmp
        else:
            key2 = (cl_lengths[0], cl_lengths[16], cl_lengths[17], cl_lengths[18])
            if key2 not in self.table2:
                self.table2[key2] = self.compute_zero_symbol_cost(*key2)
            dp, prev = self.table2[key2]
            if dp[count] >= INF_CHECK:
                raise ValueError(f"DP failed: value=0 count={count} cl_lengths={cl_lengths}")
            i = count
            tmp = []
            while i > 0:
                choice = prev[i]
                if choice == 1:
                    tmp.append((0, 0, 0))
                    i -= 1
                elif choice > 0:
                    run = choice
                    if run <= 10:
                        tmp.append((17, run - 3, 3))
                    else:
                        tmp.append((18, run - 11, 7))
                    i -= run
                else:
                    run = -choice
                    tmp.append((16, run - 3, 2))
                    i -= run
            tmp.reverse()
            return tmp

    def rle_code_lengths_stream(
        self,
        litlen: list[int],
        dist: list[int],
        cl_lengths: list[int]
    ) -> list[tuple[int, int, int]]:
        concat = list(litlen) + list(dist)
        entries = _length_rle(concat)
        out = []
        for value, count in entries:
            out.extend(self.optimal_parse(value, count, cl_lengths))
        return out


RLE_DP_TABLE = RLETable()

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

def _compute_table():
    """
    imos 法の考え方を用い、各遷移をスライディング最小値で O(N) に削減する
    ただし N は 300 固定とする
    """
    N = 300
    VALID_WIDTHS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    INF = 1 << 60

    def push_monotone(dq, idx, val, arr):
        # arr は dp 参照配列
        while dq and arr[dq[-1]] >= val:
            # 等号で後着を捨てずに前着を優先することで
            # 元のループ順に合わせたタイブレークを再現する
            if arr[dq[-1]] > val:
                dq.pop()
            else:
                break
        dq.append(idx)

    table = {}
    for _single_symbol_cost, _code_16_cost in itertools.product(VALID_WIDTHS, VALID_WIDTHS):
        single_symbol_cost = _single_symbol_cost if _single_symbol_cost != 0 else INF
        code_16_cost = _code_16_cost if _code_16_cost != 0 else INF
        add_16 = code_16_cost + 2

        dp = [INF] * N
        prev = [INF] * N
        dp[0] = 0

        # PREV_RUN 用の窓 k in [j-6, j-3] かつ k>=1
        deq16 = deque()

        for j in range(1, N):
            best = INF
            choice = INF

            # まず literal
            c_lit = dp[j - 1] + single_symbol_cost
            if c_lit < best:
                best = c_lit
                choice = 1

            # PREV_RUN
            if add_16 < INF:
                # 窓に新規に入る k=j-3 を条件付きで追加
                k_new = j - 3
                if k_new >= 1:
                    push_monotone(deq16, k_new, dp[k_new], dp)
                # 古い要素を追い出す
                k_min = j - 6
                while deq16 and deq16[0] < max(1, k_min):
                    deq16.popleft()
                if deq16:
                    k = deq16[0]
                    c16 = dp[k] + add_16
                    # ループ順との整合性のため等号では更新しない
                    if c16 < best:
                        best = c16
                        choice = j - k  # run 長
            dp[j] = best
            prev[j] = choice

        table[(_single_symbol_cost, _code_16_cost)] = (dp, prev)

    table2 = {}
    for _single_symbol_cost, _code_16_cost, _code_17_cost, _code_18_cost in itertools.product(VALID_WIDTHS, VALID_WIDTHS, VALID_WIDTHS, VALID_WIDTHS):
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

        # 各レンジ用のスライディング最小値
        # ZERO_RUN 3..10: k in [j-10, j-3] かつ k>=0
        deq17 = deque()
        # ZERO_RUN 11..138: k in [j-138, j-11] かつ k>=0
        deq18 = deque()
        # PREV_RUN 3..6: k in [j-6, j-3] かつ k>=1
        deq16 = deque()

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
                        choice = j - k  # 正の run

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
                        choice = j - k  # 正の run

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
                        choice = -(j - k)  # 負の run で PREV_RUN を表現

            dp[j] = best
            prev[j] = choice

        table2[(_single_symbol_cost, _code_16_cost, _code_17_cost, _code_18_cost)] = (dp, prev)

    return table, table2

def _compute_table_slow():
    N = 300
    VALID_WIDTHS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    INF = 1 << 30
    # table[i][j]: DP table for single_symbol_cost=i, code_16_cost=j
    # memo: 累積和をすると早くなる（面倒なのでやってない）
    table = {}
    for _single_symbol_cost, _code_16_cost in itertools.product(VALID_WIDTHS, VALID_WIDTHS):
        single_symbol_cost = _single_symbol_cost if _single_symbol_cost != 0 else INF
        code_16_cost = _code_16_cost if _code_16_cost != 0 else INF
        dp = [INF] * N
        prev = [INF] * N
        dp[0] = 0
        for i in range(N):
            if dp[i] == INF:
                continue
            # literal
            if i + 1 < N and (dp[i] + single_symbol_cost < dp[i + 1]):
                dp[i + 1] = dp[i] + single_symbol_cost
                prev[i + 1] = 1
            # PREV_RUN 3..6
            if i > 0:
                add = code_16_cost + 2
                for run in range(3, min(6, N - i - 1) + 1):
                    j = i + run
                    if dp[i] + add < dp[j]:
                        dp[j] = dp[i] + add
                        prev[j] = run
        table[(_single_symbol_cost, _code_16_cost)] = (dp, prev)
    
    # table2[i][j][k][l]: DP table for single_symbol_cost=i, code_16_cost=j, code_17_cost=k, code_18_cost=l
    table2 = {}
    for _single_symbol_cost, _code_16_cost, _code_17_cost, _code_18_cost in itertools.product(VALID_WIDTHS, VALID_WIDTHS, VALID_WIDTHS, VALID_WIDTHS):
        single_symbol_cost = _single_symbol_cost if _single_symbol_cost != 0 else INF
        code_16_cost = _code_16_cost if _code_16_cost != 0 else INF
        code_17_cost = _code_17_cost if _code_17_cost != 0 else INF
        code_18_cost = _code_18_cost if _code_18_cost != 0 else INF
        dp = [INF] * N
        prev = [INF] * N
        dp[0] = 0
        for i in range(N):
            if dp[i] == INF:
                continue
            # literal
            if i + 1 < N and (dp[i] + single_symbol_cost < dp[i + 1]):
                dp[i + 1] = dp[i] + single_symbol_cost
                prev[i + 1] = 1
            # ZERO_RUN 3..10 は 17 3bits  11..138 は 18 7bits
            add_17 = code_17_cost + 3
            for run in range(3, min(10, N - i - 1) + 1):
                j = i + run
                if dp[i] + add_17 < dp[j]:
                    dp[j] = dp[i] + add_17
                    prev[j] = run
            add_18 = code_18_cost + 7
            for run in range(11, min(138, N - i - 1) + 1):
                j = i + run
                if dp[i] + add_18 < dp[j]:
                    dp[j] = dp[i] + add_18
                    prev[j] = run
            # PREV_RUN 3..6
            if i > 0:
                add_16 = code_16_cost + 2
                for run in range(3, min(6, N - i - 1) + 1):
                    j = i + run
                    if dp[i] + add_16 < dp[j]:
                        dp[j] = dp[i] + add_16
                        prev[j] = -run
        table2[(_single_symbol_cost, _code_16_cost, _code_17_cost, _code_18_cost)] = (dp, prev)
    return table, table2

class RLETable:
    def __init__(self):
        print('Computing RLE DP table...', file=sys.stderr)
        self.table, self.table2 = _compute_table()
    
    def optimal_parse(self, value: int, count: int, cl_lengths: list[int]) -> list[tuple[int, int, int]]:
        if value != 0:
            dp, prev = self.table[(cl_lengths[value], cl_lengths[16])]
            if dp[count] >= (1 << 30):
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
            dp, prev = self.table2[(cl_lengths[0], cl_lengths[16], cl_lengths[17], cl_lengths[18])]
            if dp[count] >= (1 << 30):
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

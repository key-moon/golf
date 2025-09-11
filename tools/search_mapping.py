from __future__ import annotations
import ast
from dataclasses import dataclass
import os
import pickle
import re
import string
import time
from typing import Tuple, Dict, List, Optional, Set
from functools import lru_cache

from tqdm import tqdm

# ============================================================
# 演算子メタ（優先・結合・可換・表示トークン）
# precedence:  ** > (unary -/~) > * // % > + - > << >> > & > ^ > |
# ============================================================
OPS = {
    '**': {'prec': 80, 'assoc': 'right', 'comm': False, 'token': '**'},
    '*':  {'prec': 60, 'assoc': 'left',  'comm': True,  'token': '*'},
    '//': {'prec': 60, 'assoc': 'left',  'comm': False, 'token': '//'},
    '%':  {'prec': 60, 'assoc': 'left',  'comm': False, 'token': '%'},
    '<<': {'prec': 40, 'assoc': 'left',  'comm': False, 'token': '<<'},
    '>>': {'prec': 40, 'assoc': 'left',  'comm': False, 'token': '>>'},
    '&':  {'prec': 30, 'assoc': 'left',  'comm': True,  'token': '&'},
    '^':  {'prec': 20, 'assoc': 'left',  'comm': True,  'token': '^'},
    '|':  {'prec': 10, 'assoc': 'left',  'comm': True,  'token': '|'},
    # + / - は Add ノードで扱うので OPS には置かない
}
# Add（+/-連鎖）の見かけ優先度（* // % より低い / << >> より高い）
ADD_PREC = 50
# unary の見かけ優先度（** より低い / * // % より高い）
UNARY_PREC = 70

# 定数どうしはテンプレートとして無意味
CONST_CONST_BAN = {'+','-','*','//','%','&','^','|','>>'}

# ============================================================
# 64-bit tree-hash（衝突は同バケットで文字列照合）
# ============================================================
MASK64 = (1 << 64) - 1
def mix64(x: int) -> int:
    x &= MASK64
    x ^= x >> 30; x = (x * 0xbf58476d1ce4e5b9) & MASK64
    x ^= x >> 27; x = (x * 0x94d049bb133111eb) & MASK64
    x ^= x >> 31
    return x & MASK64

SALT_NUM  = 0xbb67ae8584caa73b
SALT_VAR  = 0x6a09e667f3bcc909
SALT_ADD  = 0x3c6ef372fe94f82b
SALT_OP   = {
    '*':  0xa54ff53a5f1d36f1,
    '//': 0x510e527fade682d1,
    '%':  0x9b05688c2b3e6c1f,
    '<<': 0x1f83d9abfb41bd6b,
    '>>': 0x5be0cd19137e2179,
    '&':  0xcbbb9d5dc1059ed8,
    '^':  0x629a292a367cd507,
    '|':  0x9159015a3070dd17,
    '**': 0x152fecd8f70e5939,
}
KEY1 = 0x9e3779b97f4a7c15
KEY2 = 0xc2b2ae3d27d4eb4f
COMM_M1 = 0xff51afd7ed558ccd
COMM_M2 = 0xc4ceb9fe1a85ec53

PREF_SALT = {
    '':   0x243f6a8885a308d3,
    '-':  0x13198a2e03707344,
    '~':  0xa4093822299f31d0,
    '-~': 0x082efa98ec4e6c89,
    '~-': 0x452821e638d01377,
}

# ============================================================
# AST
# ============================================================
@dataclass(frozen=True)
class Node:
    def has_x(self) -> bool: raise NotImplementedError
    def prec(self) -> int:   return 100  # 原子既定
    def to_string(self) -> str: raise NotImplementedError

@dataclass(frozen=True)
class Var(Node):
    """prefix: '', '-', '~', '-~', '~-'. 例: '-~x'"""
    prefix: str = ''
    def has_x(self) -> bool: return True
    def prec(self) -> int:
        return UNARY_PREC if self.prefix else 100
    def to_string(self) -> str:
        return f'{self.prefix}x' if self.prefix else 'x'

@dataclass(frozen=True)
class Num(Node):
    k: int  # 'd' の繰り返し数（桁長）
    def has_x(self) -> bool: return False
    def to_string(self) -> str: return 'd' * self.k

@dataclass(frozen=True)
class Op(Node):
    op: str
    args: Tuple[Node, ...]  # 可換は可変長、非可換は 2 項
    def has_x(self) -> bool: return any(has_x_cached(a) for a in self.args)
    def prec(self) -> int: return OPS[self.op]['prec']
    def to_string(self) -> str: return _op_to_string(self)

@dataclass(frozen=True)
class Add(Node):
    """加減連鎖：terms は (Node, sign) の列。sign は +1 / -1。"""
    terms: Tuple[Tuple[Node, int], ...]
    def has_x(self) -> bool: return any(has_x_cached(n) for n, s in self.terms)
    def prec(self) -> int: return ADD_PREC
    def to_string(self) -> str: return _add_to_string(self)

# ========================= キャッシュ ========================
@lru_cache(maxsize=None)
def has_x_cached(n: Node) -> bool:
    return n.has_x()

@lru_cache(maxsize=None)
def hash64(n: Node) -> int:
    if isinstance(n, Var):
        return mix64(SALT_VAR ^ PREF_SALT[n.prefix])
    if isinstance(n, Num):
        return mix64(SALT_NUM ^ mix64(n.k * 0x9e3779b97f4a7c15))
    if isinstance(n, Add):
        h = SALT_ADD
        for node, sign in n.terms:
            hs = hash64(node)
            h = mix64(h ^ (KEY1 * hs + KEY2 * (1 if sign < 0 else 0)))
        return h
    if isinstance(n, Op):
        h = SALT_OP[n.op]
        if OPS[n.op]['comm']:
            s = 0; x = 0; m = COMM_M1; l = 0
            for ch in n.args:
                hc = hash64(ch)
                s = (s + hc) & MASK64
                x ^= hc
                m = ((m ^ hc) * COMM_M2) & MASK64
                l += 1
            return mix64(h ^ mix64(s) ^ mix64(x) ^ mix64(m) ^ mix64(l))
        else:
            return mix64(h ^ (KEY1 * hash64(n.args[0]) + KEY2 * hash64(n.args[1])))
    raise TypeError

@lru_cache(maxsize=None)
def str_len(n: Node) -> int:
    return len(n.to_string())

# --------- to_string 実装（必要最小括弧） --------
@lru_cache(maxsize=None)
def _op_to_string(node: Op) -> str:
    op = node.op
    token = OPS[op]['token']
    if OPS[op]['comm']:
        children = sorted(node.args, key=hash64)  # 正規順
        parts: List[str] = []
        for ch in children:
            s = ch.to_string()
            need = isinstance(ch, (Op, Add)) and (
                ch.prec() < node.prec() or
                (isinstance(ch, Op) and ch.prec() == node.prec() and ch.op != op)
            )
            parts.append(f'({s})' if need else s)
        return token.join(parts)
    else:
        left, right = node.args
        ls = left.to_string()
        rs = right.to_string()
        left_need = isinstance(left, (Op, Add)) and (
            left.prec() < node.prec() or (op == '**' and isinstance(left, Op) and left.op == '**')
        )
        right_need = False
        if isinstance(right, (Op, Add)):
            if right.prec() < node.prec():
                right_need = True
            elif OPS[op]['assoc'] == 'left' and right.prec() == node.prec():
                right_need = True
        if left_need:  ls = f'({ls})'
        if right_need: rs = f'({rs})'
        return f'{ls}{token}{rs}'

@lru_cache(maxsize=None)
def _add_to_string(node: Add) -> str:
    parts: List[str] = []
    for i, (term, sign) in enumerate(node.terms):
        s = term.to_string()
        need = isinstance(term, (Op, Add)) and term.prec() < node.prec()
        if i == 0:
            parts.append(f'({s})' if need else s)
        else:
            if sign >= 0:
                parts.append('+' + (f'({s})' if need else s))
            else:
                parts.append('-' + (f'({s})' if need else s))
    return ''.join(parts)

# ====================== 正規化（簡略化なし） ===================
def make_op(op: str, args: Tuple[Node, ...]) -> Node:
    """+/- は Add に畳む。他の可換はフラット化＋ソートのみ。"""
    if op == '+' or op == '-':
        terms: List[Tuple[Node, int]] = []

        def append_term(node: Node, sign: int) -> None:
            if isinstance(node, Add):
                for t, s in node.terms:
                    terms.append((t, sign * s))
            else:
                terms.append((node, sign))

        if op == '+':
            assert len(args) == 2
            append_term(args[0], +1)
            append_term(args[1], +1)
        else:  # '-'
            assert len(args) == 2
            append_term(args[0], +1)
            append_term(args[1], -1)

        assert terms and terms[0][1] == 1, (args, terms)
        terms.sort(key=lambda x: (-x[1], hash64(x[0])))
        return Add(tuple(terms))

    # それ以外
    if OPS[op]['comm']:
        flat: List[Node] = []
        for a in args:
            if isinstance(a, Op) and a.op == op:
                flat.extend(a.args)  # 結合のみ
            else:
                flat.append(a)
        flat.sort(key=hash64)
        return Op(op, tuple(flat))
    else:
        assert len(args) == 2
        return Op(op, args)

# ============================================================
# “前段パターン拒否”：加減列（Add）の中身で判定
# ============================================================
def nodes_equal(a: Node, b: Node) -> bool:
    return hash64(a) == hash64(b) and a.to_string() == b.to_string()

def collect_add_terms_preview(op: str, left: Node, right: Optional[Node]=None) -> Optional[List[Tuple[Node,int]]]:
    """生成前プレビュー：+/- なら Add と同じルールで項と符号を取り出す。"""
    if op not in ('+','-'):
        return None
    terms: List[Tuple[Node,int]] = []

    def push(n: Node, sign: int) -> None:
        if isinstance(n, Add):
            for t, s in n.terms:
                terms.append((t, sign * s))
        else:
            terms.append((n, sign))

    push(left, +1)
    if right is not None:
        push(right, -1 if op == '-' else +1)
    return terms

def is_bad_pattern_pre(op: str, left: Node, right: Node) -> bool:
    """
    生成直前の局所パターンで「採択しない」と判断する。
    - 簡略化は一切しない。ここでは不採択のみ。
    - +/- は Add で扱う想定（ただし -x は Add に畳まれない Var(prefix='-')）。
    """
    # -------- 基本NG：定数どうし --------
    if isinstance(left, Num) and isinstance(right, Num) and op not in CONST_CONST_BAN:
        return True

    # -------- 同一オペランドNG（置換可能な重複）--------
    if nodes_equal(left, right) and op in {'&', '|', '^', '-', '//', '+', '*'}:
        return True

    # -------- x と -x の組み合わせの除外（floor-div）--------
    # -x//x, x//-x は冗長（一般化：Var 同士で「符号だけ違う」）
    if op == '//' and isinstance(left, Var) and isinstance(right, Var):
        lp, rp = left.prefix, right.prefix
        return (lp.strip("-") == rp.strip("-") and (lp.startswith('-') ^ rp.startswith('-')))

    # -------- ({term}(+, -, *) dddd)  (% & ) ddd を除外 --------
    # 左が Add（加減列）で数を含む、または '*' で数を含む ＆ 右が数 → 冗長
    if op in {'%', '&'} and isinstance(right, Num):
        # Add 中に 1 個でも Num があればアウト（-x は Add に畳まれないので安全）
        if isinstance(left, Add):
            if any(isinstance(t, Num) and t.k > right.k for (t, s) in left.terms):
                return True
        # 乗算のどちらかが数でもアウト（順序は問わない）
        if isinstance(left, Op) and left.op == '*':
            if any(isinstance(ch, Num) and ch.k > right.k for ch in left.args):
                return True

    # -------- 多重 % の除外： (term % dd) % ddd --------
    if op == '%' and isinstance(right, Num):
        if isinstance(left, Op) and left.op == '%' and isinstance(left.args[1], Num) and left.args[1].k < right.k:
            return True

    # 多重 // の除外： (term // dd) // dd
    if op == '//' and isinstance(right, Num):
        if isinstance(left, Op) and left.op == '//' and isinstance(left.args[1], Num):
            return True

    # 加減連鎖の既存チェック（x-d-dd-d / x-d-dd-x 等）
    # ここでは Add へのプレビューだけ行い、-x は Var(prefix='-') のまま扱う
    def _preview_add_terms(op_: str, L: Node, R: Node) -> Optional[List[Tuple[Node, int]]]:
        if op_ not in {'+', '-'}:
            return None
        terms: List[Tuple[Node, int]] = []
        def push(n: Node, sign: int) -> None:
            if isinstance(n, Add):
                for t, s in n.terms:
                    terms.append((t, sign * s))
            else:
                terms.append((n, sign))
        push(L, +1)
        push(R, -1 if op_ == '-' else +1)
        return terms

    terms = _preview_add_terms(op, left, right)
    if terms is not None:
        # 数（Num）が 2 個以上 → 無意味
        if sum(1 for t, _ in terms if isinstance(t, Num)) >= 2:
            return True
        # 同一「非数」項が正負で両方登場 → 無意味（x-d-dd-x, x-(x+d) 等）
        pos: Dict[int, int] = {}
        neg: Dict[int, int] = {}
        for t, s in terms:
            if isinstance(t, Num):
                continue
            h = hash64(t)
            if s >= 0:
                pos[h] = pos.get(h, 0) + 1
            else:
                neg[h] = neg.get(h, 0) + 1
        for h in pos:
            if h in neg:
                return True

    return False


def is_bad_pattern_post(node: Node) -> bool:
    """
    生成直後（正規化後）に、全体形を見て不採択にする。
    - 可換演算はフラット化済み前提。
    """
    # 単項では何もしない
    if not isinstance(node, Op):
        return False

    op = node.op

    # -------- 可換演算での重複オペランド（|,&,^,*）--------
    # 同じオペランドが複数あれば冗長（x|x|dd, x&x&K, x^x^y, x*x*dd 等）
    if op in {'|', '&', '^', '*'}:
        seen: Set[int] = set()
        for a in node.args:
            sig = hash64(a)
            if sig in seen:
                return True
            seen.add(sig)

    # -------- 可換演算に「数が2個以上」混在 --------
    # & / | / ^ / * に Num が2つ以上含まれる → 冗長（数どうしは別表現で置換可能）
    if op in {'&', '|', '^', '*'}:
        if sum(1 for a in node.args if isinstance(a, Num)) >= 2:
            return True

    return False

# ===================== 高速・安全な下界見積 ====================
def fast_lower_bound_len(op: str, a: Node, b: Node, len_a: int, len_b: int) -> int:
    if op in ('+','-'):
        # Add はトークン 1 文字を下界として仮置き（実際は複数項で増えるが過小評価でOK）
        tok = 1
        p = ADD_PREC
    else:
        p = OPS[op]['prec']
        tok = len(OPS[op]['token'])
    pa = a.prec() if isinstance(a, (Op, Add, Var)) else 100
    pb = b.prec() if isinstance(b, (Op, Add, Var)) else 100
    need_a = 2 if pa < p else 0
    need_b = 2 if pb < p else 0
    return len_a + len_b + tok + need_a + need_b

# ========================= 列挙 ========================
def enumerate_templates(
    N: int,
    allow_ops: list[str] = ['+','-','*','//','%','<<','>>','&','^','|','**'],
    require_x: bool = True,
    max_digit_run: Optional[int] = None,
) -> List[Node]:
    # 入力検証（+/- は Add で扱うが allow_ops には入っていて良い）
    for op in allow_ops:
        if op not in OPS and op not in ('+','-'):
            raise ValueError(f'Unknown op: {op}')
    if max_digit_run is None: max_digit_run = N

    # dp_by_len[L] = { h64 : { string : Node } }
    dp_by_len: Dict[int, Dict[int, Node]] = { i+1: {} for i in range(N) }

    # 原子（Var prefix 5 種）
    for pref in ('', '-', '~', '-~', '~-'):
        v = Var(pref)
        dp_by_len[len(v.to_string())][hash64(v)] = v

    # 数（d-run）
    for k in range(1, min(max_digit_run, N) + 1):
        n = Num(k)
        dp_by_len[k][hash64(n)] = n

    # ---- 合成→フィルタ→採択（共通処理） ----
    def _try_emit(N: int, op: str, a: Node, b: Node) -> None:
        # require_x 早期
        if require_x and not (has_x_cached(a) or has_x_cached(b)):
            return

        # 生成直前パターン拒否
        if is_bad_pattern_pre(op, a, b):
            return

        # 粗い下界
        if fast_lower_bound_len(op, a, b, str_len(a), str_len(b)) > N:
            return

        # 正規化（+/- は Add。他は可換のみフラット化）
        node = make_op(op, (a, b))

        # 生成直後パターン拒否
        if is_bad_pattern_post(node):
            return

        s = node.to_string()
        L = len(s)
        if L > N:
            return
        if require_x and 'x' not in s:
            return
        h = hash64(node)
        if h in dp_by_len[L]:
            assert dp_by_len[L][h].to_string() == node.to_string(), (dp_by_len[L][h], node)
            return 
        dp_by_len[L][h] = node

    # sum_len = len(lhs)+len(rhs) を対角走査（op トークン長も考慮）
    min_tok = min([1] + [len(OPS[o]['token']) for o in allow_ops if o not in ('+','-')])
    for sum_len in range(2, N - min_tok + 1):
        for l1 in range(1, sum_len):
            l2 = sum_len - l1
            if l1 not in dp_by_len or l2 not in dp_by_len:
                continue

            left_nodes  = list(dp_by_len[l1].values())
            right_nodes = list(dp_by_len[l2].values())

            for op in allow_ops:
                tok_len = 1 if op in ('+','-') else len(OPS[op]['token'])
                if sum_len + tok_len > N:
                    continue

                comm = (op not in ('+','-')) and OPS[op]['comm']
                if comm and l1 > l2:
                    continue  # 可換は順序重複を抑止

                # ペア生成
                if comm and l1 == l2:
                    sorted_right = sorted(right_nodes, key=hash64)
                    for i, a in enumerate(sorted_right):
                        ha = hash64(a)
                        for b in sorted_right[i:]:
                            if ha <= hash64(b):
                                _try_emit(N, op, a, b)
                else:
                    for a in left_nodes:
                        for b in right_nodes:
                            _try_emit(N, op, a, b)

    # 出力
    nodes: List[Node] = []
    for L in range(1, N + 1):
        for node in dp_by_len.get(L, {}).values():
            if node.has_x():
                nodes.append(node)
    nodes.sort(key=lambda z: (len(z.to_string()), z.to_string()))
    return nodes

def hook(f):
    def func(*args, **kwargs):
        res = f(*args, **kwargs)
        print(f"{f.__name__}({args[0], args[1], args[2]}, {kwargs=}) = {res}")
        return res
    return func

# ---- 範囲評価（安全過大評価）。失敗/オーバーは (False, None) ----
@lru_cache(maxsize=None)
def eval_bounds(node: Node, x_min: int, x_max: int, cap: int) -> Tuple[bool, Optional[Tuple[int,int]]]:
    """
    |x| ∈ [x_min, x_max]（通常 x_min = -x_abs, x_max = x_abs）
    cap: 許容絶対値しきい値
    戻り値:
      (True, (lo,hi)) : すべての代入で lo..hi に収まる（かつ |lo|,|hi| ≤ cap）
      (False, None)   : しきい値を超えうる／評価不能（0 除算・負剰余・指数爆発など）
    """
    # 便利関数
    def max_abs(a: int, b: int) -> int: return a if abs(a) >= abs(b) else b
    def within_cap(lo: int, hi: int) -> bool: return -cap <= lo <= hi <= cap
    def bail() -> Tuple[bool, Optional[Tuple[int,int]]]: return (False, None)

    # --- Var ---
    if isinstance(node, Var):
        L, U = x_min, x_max
        if node.prefix == '':
            lo, hi = L, U
        elif node.prefix == '-':
            lo, hi = -U, -L
        elif node.prefix == '~':
            # ~x = -x - 1
            lo, hi = -U - 1, -L - 1
        elif node.prefix == '-~':
            # -~x = x + 1
            lo, hi = L + 1, U + 1
        elif node.prefix == '~-':
            # ~(-x) = x - 1
            lo, hi = L - 1, U - 1
        else:
            return bail()
        return (True, (lo, hi)) if within_cap(lo, hi) else bail()

    # --- Num ---
    if isinstance(node, Num):
        # [0, 10^k - 1] だが巨大化回避のため桁比較で早期判定
        if node.k <= 0:
            return (True, (0, 0))
        # cap の桁数
        import math
        cap_digits = 1 if cap == 0 else int(math.log10(cap)) + 1
        if node.k > cap_digits:
            return bail()
        else:
            lo = -10 ** (node.k - 1)
            hi = 10 ** node.k - 1
            assert isinstance(lo, int)
            assert isinstance(hi, int)
            return (True, (lo, hi))

    # --- Add ---
    if isinstance(node, Add):
        total_lo = 0
        total_hi = 0
        for term, sign in node.terms:
            ok, rng = eval_bounds(term, x_min, x_max, cap)
            if not ok or rng is None:
                return bail()
            lo, hi = rng
            if sign >= 0:
                total_lo += lo
                total_hi += hi
            else:
                total_lo -= hi
                total_hi -= lo
            if not (-cap <= total_lo <= cap and -cap <= total_hi <= cap):
                return bail()
        return (True, (total_lo, total_hi)) if total_lo <= total_hi else (True, (total_hi, total_lo))

    # --- Op ---
    if isinstance(node, Op):
        op = node.op
        # 便利: 2 項/可変長の区間取得
        def get_bounds_list(args: Tuple[Node, ...]) -> Optional[List[Tuple[int,int]]]:
            res: List[Tuple[int,int]] = []
            for a in args:
                ok, rng = eval_bounds(a, x_min, x_max, cap)
                if not ok or rng is None:
                    return None
                res.append(rng)
            return res

        # 乗算（可換・可変長）
        if op == '*':
            ranges = get_bounds_list(node.args)
            if ranges is None:
                return bail()
            # 逐次的に区間を掛け合わせる
            cur_lo, cur_hi = 1, 1
            first = True
            for lo, hi in ranges:
                if first:
                    cur_lo, cur_hi = lo, hi
                    first = False
                    if not (-cap <= cur_lo <= cap and -cap <= cur_hi <= cap):
                        return bail()
                    continue
                # 候補 4 つ
                cand = [cur_lo*lo, cur_lo*hi, cur_hi*lo, cur_hi*hi]
                nlo, nhi = min(cand), max(cand)
                if not (-cap <= nlo <= cap and -cap <= nhi <= cap):
                    return bail()
                cur_lo, cur_hi = nlo, nhi
            return (True, (cur_lo, cur_hi))

        # 冪乗（右結合・2 項）
        if op == '**':
            if len(node.args) != 2:
                return bail()
            okA, rA = eval_bounds(node.args[0], x_min, x_max, cap)
            okB, rB = eval_bounds(node.args[1], x_min, x_max, cap)
            if not okA or not okB or rA is None or rB is None:
                return bail()
            aL, aU = rA; bL, bU = rB
            # 指数に負を許さない（整数域外 or 爆発）
            if bL < 0:
                bL = 0
            # 上界チェック（bit_length で安全に比較）
            import math
            A = max(abs(aL), abs(aU))
            if bU == 0:
                lo = hi = 1
                return (True, (lo, hi))
            if A == 0:
                lo = hi = 0
                return (True, (lo, hi))
            if A == 1:
                # 1^b または (-1)^b
                if aL <= -1 <= aU:
                    # 奇偶不明 → [-1,1]
                    lo, hi = -1, 1
                elif aU == 1 and aL == 1:
                    lo, hi = 1, 1
                elif aL == -1 and aU == -1:
                    # (-1)^b の範囲 [-1,1]
                    lo, hi = -1, 1
                else:
                    lo, hi = -1, 1
                return (True, (lo, hi)) if within_cap(lo, hi) else bail()
            # A >= 2
            # bit_length を使って A**bU <= cap 判定
            # log2(A**bU) = bU * log2(A) < =? log2(cap)
            # 近似ではなく安全側にするため、少しきつめに：
            if (A.bit_length() - 1) * bU > (cap.bit_length()):
                return bail()
            # なおかつ実計算で確認（cap 超えたら即 bail）
            try:
                val = int(A ** bU)
            except OverflowError:
                return bail()
            if val > cap:
                return bail()
            lo, hi = (-val, val) if aL < 0 < aU or aL < 0 and (bU % 2 == 1) else (0 if aL >= 0 else -val, val)
            return (True, (lo, hi))

        # 整数除算（2 項）
        if op == '//':
            if len(node.args) != 2:
                return bail()
            okA, rA = eval_bounds(node.args[0], x_min, x_max, cap)
            okB, rB = eval_bounds(node.args[1], x_min, x_max, cap)
            if not okA or not okB or rA is None or rB is None:
                return bail()
            aL, aU = rA; bL, bU = rB
            # |denom| の最小値を見積（区間端と ±1 を考慮）
            cand = [abs(bL), abs(bU)]
            if bL <= 1 <= bU: cand.append(1)
            if bL <= -1 <= bU: cand.append(1)
            dmin = max(1, min(cand))
            A = max(abs(aL), abs(aU))
            up = A // dmin
            if up > cap:
                return bail()
            return (True, (-up, up))

        # 剰余（2 項）
        if op == '%':
            if len(node.args) != 2:
                return bail()
            return eval_bounds(node.args[1], x_min, x_max, cap)

        # ビットシフト（2 項）
        if op in ('<<', '>>'):
            if len(node.args) != 2:
                return bail()
            okA, rA = eval_bounds(node.args[0], x_min, x_max, cap)
            okK, rK = eval_bounds(node.args[1], x_min, x_max, cap)
            if not okA or not okK or rA is None or rK is None:
                return bail()
            aL, aU = rA; kL, kU = rK
            if kU < 0:
                return bail()
            A = max(abs(aL), abs(aU))
            if op == '<<':
                # a << k の上界：bit_length で安全判定
                # bitlen(A<<k) = bitlen(A) + k
                if A == 0:
                    return (True, (0, 0))
                if (A.bit_length() - 1) + kU > cap.bit_length():
                    return bail()
                up = A << kU
                if up > cap:
                    return bail()
                lo, hi = (-up, up)
                return (True, (lo, hi))
            else:
                # >> は最小シフトで最大絶対値
                shift = max(0, kL)
                up = A >> shift
                if up > cap:
                    return bail()
                lo, hi = (-up, up)
                return (True, (lo, hi))

        # ビット演算（可換）
        if op in ('&', '^', '|'):
            ranges = get_bounds_list(node.args)
            if ranges is None:
                return bail()
            # 2 項以上の可換に対応するため逐次畳み込み
            def combine_bit(opc: str, r1: Tuple[int,int], r2: Tuple[int,int]) -> Optional[Tuple[int,int]]:
                l1, u1 = r1; l2, u2 = r2
                has_neg = False
                if l1 < 0:
                    has_neg = True
                    l1, u1 = 0, max(~l1, u1)
                if l2 < 0:
                    has_neg = True
                    l2, u2 = 0, max(~l2, u2)
                # 非負×非負は上界を強くとれる
                if opc == '&':
                    lo, hi = 0, min(u1, u2)
                else:  # '|' '^'
                    lo, hi = 0, (1 << max(u1.bit_length(), u2.bit_length())) - 1
                if has_neg:
                    lo = -hi
                return (lo, hi) if -cap <= lo <= hi <= cap else None

            cur = ranges[0]
            for i in range(1, len(ranges)):
                comb = combine_bit(op, cur, ranges[i])
                if comb is None:
                    return bail()
                cur = comb
            return (True, cur)

        # ここまでに無い演算子は未対応
        return bail()

    # 型不明
    return (False, None)

def check_template(template: str, mapping: dict[int, int]):
    mapping_kvs = list(mapping.items())
    placeholders = re.findall("(d+)", template)

    func = template
    sym_candidates = string.ascii_uppercase
    source_tmpl = "def f():\n"
    indentation = " "
    syms = []
    for placeholder in placeholders:
        sym, sym_candidates = sym_candidates[0], sym_candidates[1:]
        syms.append(sym)

        func = func.replace(placeholder, sym, 1)
        source_tmpl += f"{indentation}for {sym} in range_{sym}:\n"
        indentation += " "

    source_tmpl += f"{indentation}try:\n"
    source_tmpl += f"{indentation} for x, v in mapping_kvs:\n"
    source_tmpl += f"{indentation}  if ({func})!=v:break\n"
    source_tmpl += f"{indentation} else: return [{','.join(syms)}]\n"
    # source_tmpl += f"{indentation} if x == {len(mapping_kvs)-3}: print({repr(func)}, {','.join(syms)})\n"
    source_tmpl += f"{indentation}except: pass\n"

    for b in range(1 << len(placeholders)):
        source = source_tmpl
        valid = True
        for tmpl_len, (placeholder, sym) in enumerate(zip(placeholders, syms)):
            if b >> tmpl_len & 1:
                sym_min = 10**(len(placeholder)-1)
                sym_max = 10**len(placeholder)
            else:
                if len(placeholder) == 1:
                    valid = False
                # ~999 -> -100
                sym_min = -10**(len(placeholder)-1)
                sym_max = -10**(len(placeholder)-2)+1
            source = source.replace(f"range_{sym}", f"range({sym_min}, {sym_max})")
        if not valid:
            continue
        env = {"mapping_kvs": mapping_kvs}
        exec(source, env)
        res = env["f"]()
        if res is not None:
            res_func = func
            for sym, binded in zip(syms, res):
                res_func = res_func.replace(sym, str(binded))
            yield res_func

# TODO: DoSを防ぐためeval_boundsが安全側に倒しすぎてしまっている expやshlのみ別途hookする?
#       式のキャッシュ?
if __name__ == "__main__":
    # mapping = { 20:1, 25:4, 30:2 }
    mapping = {0: 0, 1: 3, 2: 3, 3: 0}
    max_length = 9
    mod_tolerance = 3
    DO_CLAMP = False

    end_terms = []
    if DO_CLAMP:
        last_mod_min = max(mapping.values())+1
        for tmpl_len in range(mod_tolerance+1):
            end_terms.append(f"%{last_mod_min+tmpl_len}")
            for j in range(1, tmpl_len+1):
                end_terms.append(f"%{last_mod_min+tmpl_len}-{j}")

        for affine_add in range(1, min(mapping.values())+1):
            last_mod_min = max(mapping.values()) - affine_add + 1
            for tmpl_len in range(mod_tolerance+1):
                end_terms.append(f"%{last_mod_min+tmpl_len}+{affine_add}")
        n = max_length - 3
    else:
        end_terms = [""]
        n = max_length
  
    print("[+] enumerating...")
    templates = enumerate_templates(n, allow_ops=['+','-','*','//','%','<<','>>','&','^','|','**'], max_digit_run=n-5)
    print("[+] enumeration done")
    os.makedirs(".cache/mapping", exist_ok=True)
    with open(f".cache/mapping/{n}.txt", "w") as o:
        for template in templates:
            o.write(template.to_string())
            o.write("\n")

    x_lo, x_hi=min(mapping.keys()), max(mapping.keys())
    cap = 10**10000

    clamped_templates = []
    for template in tqdm(templates):
        if template.to_string().endswith("%d"):
            continue
        if "x" not in template.to_string():
            continue
        ok, rng = eval_bounds(template, x_lo, x_hi, cap)
        if not ok:
            continue

        for clamp in end_terms:
            clamped = ast.unparse(ast.parse(f"({template.to_string()}){clamp}")).replace(" ", "")
            if len(clamped) <= max_length:
                clamped_templates.append(clamped)
    
    pickle.dump(clamped_templates, open(f".cache/mapping/{n}", "wb"))
    for template in tqdm(sorted(clamped_templates, key=lambda x: x.count("d"))):
        t = time.time()
        results = [*check_template(template, mapping)]
        end = time.time()
        if 1 < end - t:
            print(template)
        for res in results:
            print(f"{len(res)=} {res=}")

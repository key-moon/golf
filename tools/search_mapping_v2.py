from collections import defaultdict
import math

# ===== Precedence / associativity =====
# Larger number = tighter binding (for our comparison logic)
PREC = {
    "|": 1,
    "^": 2,
    "&": 3,
    "<<": 4, ">>": 4,
    "+": 5, "-": 5,
    "*": 6, "//": 6, "%": 6,
    "**": 8,  # power binds tighter than unary +,-,~
}
UNARY_PREC = 7  # unary +,-,~ are below power but above multiplicative
ATOM_PREC = 99
MAX_PREC = ATOM_PREC

# When parent and child share the same precedence:
# For each parent_op, booleans telling whether we can drop parens safely for (left, right) child
ASSOC_SAFE = {
    "+": (True, True),
    "*": (True, True),
    "&": (True, True),
    "|": (True, True),
    "^": (True, True),

    "-": (True, False), "/": (True, False), "//": (True, False), "%": (True, False),
    "<<": (True, False), ">>": (True, False),

    # Power is right-associative: left child at same prec must be parenthesized
    "**": (False, True),
}

BIN_OPS = ["+", "-", "*", "//", "%", "**", "&", "|", "^", "<<", ">>"]
UN_OPS = ["-", "~"]  # unary ops supported

# Precompute operator byte lengths
OP_LEN = {op: len(op.encode("utf-8")) for op in set(BIN_OPS) | set(UN_OPS)}

# ===== Literal length cap =====
MAX_LITERAL_BYTES = 3  # do not generate integer literals of length >= 5

# ===== Global growth caps (safe, user-tunable) =====
# - VALUE_CAP: absolute-value cap for intermediate results
# - BIT_CAP:   bit-length cap for intermediate results (prevents huge bigints)
DEFAULT_VALUE_CAP = 10**5
DEFAULT_BIT_CAP = 18  # very small cap to prune huge powers/shifts quickly

# ===== Helpers =====
def byte_len(s):
    return len(s.encode("utf-8"))


def needs_paren_binary(parent_op, child_prec, child_side, child_is_atom, child_expr, child_last_op):
    """
    Decide if parentheses are required around a child expression when used under parent_op.
    child_side in {"L","R"}.
    """
    if child_is_atom:
        # Special-case for negative numeric literal as left child of ** (e.g., "(-3)**2" is required)
        if parent_op == "**" and child_side == "L" and child_expr.startswith("-"):
            return True
        return False
    pprec = PREC[parent_op]
    if child_prec > pprec:
        return False
    if child_prec < pprec:
        return True
    # Equal precedence: consult safety table
    safeL, safeR = ASSOC_SAFE.get(parent_op, (False, False))
    return (child_side == "L" and not safeL) or (child_side == "R" and not safeR)


def needs_paren_unary(child_prec, child_is_atom, child_last_op):
    # Python: power binds tighter than unary; if child is "**" tree, we need parens
    if child_is_atom:
        return False
    if child_last_op == "**":
        return True
    return child_prec < UNARY_PREC


def eval_bin_raw(op, a, b):
    if op in ("//", "%") and b == 0:
        return None
    if op == ">>" and b < 0:
        return None
    if op == "+":  return a + b
    if op == "-":  return a - b
    if op == "*":  return a * b
    if op == "//": return a // b
    if op == "%":  return a % b
    if op == "**": return a ** b
    if op == "&":  return a & b
    if op == "|":  return a | b
    if op == "^":  return a ^ b
    if op == "<<": return a << b
    if op == ">>": return a >> b
    return None


def eval_un(op, a):
    try:
        if op == "-": return -a
        if op == "~": return ~a
    except Exception:
        return None
    return None


def bitlen_abs(x: int) -> int:
    return abs(int(x)).bit_length()


def pow_bits_estimate(base_abs: int, exp: int) -> float:
    if exp <= 0:
        return 1.0
    if base_abs <= 1:
        return 1.0
    return exp * math.log2(base_abs)


# ===== Numeric literal enumeration (fast, exact-length, no leading zeros) =====
# We generate each exact byte-length only once and cache signatures per mapping size.
_POS_CACHE = {}  # (L, N) -> {str_literal: (val,)*N}
_NEG_CACHE = {}  # (L, N) -> {str_literal: (val,)*N}


def _gen_pos_literals_len(L):
    """Yield all non-negative base-10 integer literal strings of exact length L.
    No leading zeros except "0" when L==1.
    """
    if L <= 0 or L > MAX_LITERAL_BYTES:
        return
    if L == 1:
        yield "0"
    # generate by range (fast)
    for i in range(10**(L-1), 10**L):
        yield str(i)


def _gen_neg_literals_len(L):
    """Yield all negative base-10 integer literal strings of exact length L (including leading '-').
    Equivalent to '-' + positive literal of length L-1 (no '-0').
    """
    if L <= 1 or L > MAX_LITERAL_BYTES:
        return
    for i in range(10**(L-2), 10**(L-1)):
        yield str(-i)


def get_const_sig_map(length_bytes, N_examples, kind):
    """
    kind in {"pos","neg"}
    Returns dict {literal_str: signature_tuple} for all integer literals of exact byte length.
    Cached by (L,N,kind). Uses tuple multiplication for speed.
    Enforces MAX_LITERAL_BYTES.
    """
    if length_bytes > MAX_LITERAL_BYTES:
        return {}

    if kind == "pos":
        cache = _POS_CACHE
        gen = _gen_pos_literals_len
    else:
        cache = _NEG_CACHE
        gen = _gen_neg_literals_len

    key = (length_bytes, N_examples)
    if key in cache:
        return cache[key]

    m = {}
    for s in gen(length_bytes):
        try:
            v = int(s)
        except Exception:
            continue
        m[s] = (v,) * N_examples
    cache[key] = m
    return m


# ===== Signature-level caches for op application =====
# Avoid recomputing op over same (sigL, sigR) or (sigC).
# These respect the growth caps via closures in search_mapping.
_BIN_CACHE = {}  # (capV, capB, op, sigL, sigR) -> sig
_UN_CACHE = {}   # (op, sig) -> sig  (unary ops unaffected by caps)


# ===== Utilities for outer `% const` check =====
def _gcd_list(vals):
    g = 0
    for x in vals:
        g = math.gcd(g, abs(int(x)))
    return g


def _divisors_ascending(n):
    n = abs(int(n))
    if n == 0:
        return []
    small, large = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i * i != n:
                large.append(n // i)
        i += 1
    return small + large[::-1]


# ===== Synthesis core (DP over last precedence × byte-length) =====
def search_mapping(mapping, max_bytes=10, value_cap=DEFAULT_VALUE_CAP, bit_cap=DEFAULT_BIT_CAP, require_outer_mod_const=False):
    """
    mapping: dict
      - single-var: {int -> int}
      - multi-var: {(v0, v1, ...)-> int}
    max_bytes: maximum expression byte length to explore
    value_cap: absolute-value cap for intermediate results (branch pruning)
    bit_cap: bit-length cap for intermediate results (branch pruning)
    require_outer_mod_const: if True, only return solutions of the form `EXPR % CONST`.

    Returns: shortest Python expression string over variables a,b,c,... that matches mapping on given inputs.

    Integer literals are NOT stored in DP explicitly; they are considered only when composing left/right children.
    Heavy computations (e.g., huge exponentiation, massive shifts) are avoided when they provably exceed caps.
    Additionally, we track the **total number of characters across all integer literals** in an expression and prune
    any expression whose total literal characters >= 5. (e.g., "12+345" counts as 2+3=5 and is pruned.)

    New: for every candidate inner expression we also try to finish with an outer "% CONST" using a GCD test:
      Let d_i = inner[i] - target[i]. For k > max(target) with k | gcd(d_i), `inner % k` matches target.
      We scan divisors of that gcd that fit literal-length / byte-length budgets and return the shortest one.
    """
    # Build examples and outputs
    keys = list(mapping.keys())
    if not keys:
        raise ValueError("mapping must be non-empty")

    if isinstance(keys[0], int):
        num_vars = 1
        var_names = ["a"]
        examples = [{"a": k} for k in keys]
    elif isinstance(keys[0], tuple):
        num_vars = len(keys[0])
        letters = "abcdefghijklmnopqrstuvwxyz"
        var_names = [letters[i] for i in range(num_vars)]
        examples = [{var_names[i]: k[i] for i in range(num_vars)} for k in keys]
    else:
        raise TypeError("Unsupported input type")

    outputs = [mapping[k] for k in keys]
    target_sig = tuple(outputs)
    if any(t < 0 for t in outputs):
        # Python's a % k with k>0 cannot yield negative results; outer modulo impossible
        outer_mod_possible = False
    else:
        outer_mod_possible = True
    N = len(examples)

    # Precompute signatures for variables
    var_seeds = {v: tuple(ex[v] for ex in examples) for v in var_names}

    # dp[prec][len] = dict: sig -> (expr, last_op, is_atom, lit_total_chars)
    # reps[sig] = list of (n, prec, expr, last_op, is_atom, lit_total_chars)
    reps = defaultdict(list)
    # Also keep a flat bucket per length to avoid re-walking dp for every op
    # cands_by_len[n] = list of (prec, sig, expr, last_op, is_atom, lit_total_chars)
    cands_by_len = defaultdict(list)

    SUM_LITERAL_LIMIT = 5  # prune if the sum of characters of all integer literals >= 5

    def dominated(sig, n, p):
        for n0, p0, *_rest in reps.get(sig, []):
            if (p0 >= p and n0 <= n) or (p0 < p and n0 <= n - 2):
                return True
        return False

    def insert(sig, n, p, expr, last_op, is_atom, lit_total_chars):
        # prune by total-literal-chars rule
        if lit_total_chars >= SUM_LITERAL_LIMIT:
            return False
        # Do not store max-length expressions; they cannot be extended further
        if n == max_bytes:
            return True
        # Normal memoization path with dominance filtering
        if dominated(sig, n, p):
            return False
        new_list = []
        for n0, p0, e0, o0, a0, lc0 in reps.get(sig, []):
            if (p >= p0 and n <= n0) or (p < p0 and n <= n0 - 2):
                continue
            new_list.append((n0, p0, e0, o0, a0, lc0))
        new_list.append((n, p, expr, last_op, is_atom, lit_total_chars))
        reps[sig] = new_list
        cands_by_len[n].append((p, sig, expr, last_op, is_atom, lit_total_chars))
        return True
    # Attempt outer "% CONST" finish for a given inner candidate
    def try_outer_mod_finish(p_inner, expr_inner, is_atom_inner, last_op_inner, sig_inner, n_inner, lit_total_inner):
        if not outer_mod_possible:
            return None
        diffs = [si - ti for si, ti in zip(sig_inner, target_sig)]
        g = _gcd_list(diffs)
        if g == 0:
            # inner already equals target (would have been returned elsewhere)
            return None
        maxT = max(outputs)
        if g <= maxT:
            return None
        # compute left length with parentheses if needed
        need_par = needs_paren_binary("%", p_inner, "L", is_atom_inner, expr_inner, last_op_inner)
        left_len_after = n_inner + (2 if need_par else 0)
        # enumerate divisors > maxT, shortest literal length first
        divs = [d for d in _divisors_ascending(g) if d > maxT]
        divs.sort(key=lambda x: (len(str(x)), x))
        for k in divs:
            k_str = str(k)
            k_len = byte_len(k_str)
            if k_len > MAX_LITERAL_BYTES:
                continue
            # literal-char budget
            if lit_total_inner + k_len >= SUM_LITERAL_LIMIT:
                continue
            total_len = left_len_after + 1 + k_len  # '%' is one byte
            if total_len > max_bytes:
                continue
            # Build once and return
            left_s = ("(" + expr_inner + ")") if need_par else expr_inner
            expr = left_s + "%" + k_str
            return expr
        return None

    # Seed variables (atoms)
    for v, sig in var_seeds.items():
        n = byte_len(v)
        if insert(sig, n, ATOM_PREC, v, None, True, 0):
            # try immediate outer % const
            got = try_outer_mod_finish(ATOM_PREC, v, True, None, sig, n, 0)
            if got is not None:
                return got

    # Local, cap-aware application with pruning
    def apply_bin_sig(op, sigL, sigR):
        key = (value_cap, bit_cap, op, sigL, sigR)
        got = _BIN_CACHE.get(key)
        if got is not None:
            return got
        out = []
        for a, b in zip(sigL, sigR):
            # Quick, cap-aware short-circuits
            if op == "**":
                # Reject negative exponents for integer semantics (would become float)
                if isinstance(b, int) and b < 0:
                    _BIN_CACHE[key] = None
                    return None
                ba = abs(int(a))
                be = int(b) if isinstance(b, int) else b
                if not isinstance(be, int):
                    _BIN_CACHE[key] = None
                    return None
                if ba == 0 and be == 0:
                    _BIN_CACHE[key] = None
                    return None
                # Estimation: bits ≈ be * log2(ba)
                est_bits = pow_bits_estimate(ba, be)
                if est_bits > bit_cap:
                    _BIN_CACHE[key] = None
                    return None
            elif op == "<<":
                if not isinstance(b, int) or b < 0:
                    _BIN_CACHE[key] = None
                    return None
                if bitlen_abs(a) + b > bit_cap:
                    _BIN_CACHE[key] = None
                    return None
            elif op == "*":
                if bitlen_abs(a) + bitlen_abs(b) > bit_cap + 1:
                    _BIN_CACHE[key] = None
                    return None

            v = eval_bin_raw(op, a, b)
            if v is None:
                _BIN_CACHE[key] = None
                return None
            if abs(int(v)) > value_cap or bitlen_abs(v) > bit_cap:
                _BIN_CACHE[key] = None
                return None
            out.append(v)
        res = tuple(out)
        _BIN_CACHE[key] = res
        return res

    def apply_un_sig_local(op, sigC):
        key = (op, sigC)
        got = _UN_CACHE.get(key)
        if got is not None:
            return got
        out = []
        for x in sigC:
            v = eval_un(op, x)
            if v is None:
                _UN_CACHE[key] = None
                return None
            if abs(int(v)) > value_cap or bitlen_abs(v) > bit_cap:
                _UN_CACHE[key] = None
                return None
            out.append(v)
        res = tuple(out)
        _UN_CACHE[key] = res
        return res

    # Helpers for constant pruning per-op
    TEN_POW = [1]
    for _ in range(32):
        TEN_POW.append(TEN_POW[-1] * 10)

    def min_abs_for_len(L, kind):
        if kind == "pos":
            return 0 if L == 1 else TEN_POW[L - 1]
        else:
            return TEN_POW[L - 1]

    def max_abs_for_len(L, kind):
        if L == 1:
            return 9
        return TEN_POW[L] - 1

    # Main DP by total bytes
    for n in range(1, max_bytes + 1):
        print(n)
        # ===== Unary ops =====
        for uop in UN_OPS:
            ulen = OP_LEN[uop]
            # child length = n - ulen - paren(0 or 2)
            for clen in (n-ulen-2, n-ulen):  # child raw length (without added parens)
                for p_child, sigC, eC, lastC, is_atomC, litTotC in cands_by_len.get(clen, () ):
                    need_par = needs_paren_unary(p_child, is_atomC, lastC)
                    total_len = ulen + clen + (2 if need_par else 0)
                    if total_len != n:
                        continue
                    sig = apply_un_sig_local(uop, sigC)
                    if sig is None:
                        continue
                    expr = uop + (("(" + eC + ")") if need_par else eC)
                    if insert(sig, n, UNARY_PREC, expr, uop, False, litTotC):
                        if sig == target_sig and not require_outer_mod_const:
                            return expr
                        # Try finishing by outer % const
                        got = try_outer_mod_finish(UNARY_PREC, expr, False, uop, sig, n, litTotC)
                        if got is not None:
                            return got

        # ===== Binary ops =====
        for op in BIN_OPS:
            op_len = OP_LEN[op]
            p = PREC[op]

            # -------- expr op expr --------
            for lenL in range(1, n):  # raw left length
                left_bucket = cands_by_len.get(lenL, ())
                if not left_bucket:
                    continue
                for pL, sigL, eL, lastL, atomL, litTotL in left_bucket:
                    parL = needs_paren_binary(op, pL, "L", atomL, eL, lastL)
                    left_len_after = lenL + (2 if parL else 0)
                    need_right_total = n - op_len - left_len_after
                    if need_right_total <= 0:
                        continue

                    for lenR in (need_right_total-2, need_right_total):
                        right_bucket = cands_by_len.get(lenR, ())
                        if not right_bucket:
                            continue
                        for pR, sigR, eR, lastR, atomR, litTotR in right_bucket:
                            parR = needs_paren_binary(op, pR, "R", atomR, eR, lastR)
                            right_len_after = lenR + (2 if parR else 0)
                            if right_len_after != need_right_total:
                                continue
                            sig = apply_bin_sig(op, sigL, sigR)
                            if sig is None:
                                continue
                            left_s = ("(" + eL + ")") if parL else eL
                            right_s = ("(" + eR + ")") if parR else eR
                            expr = left_s + op + right_s
                            lit_total = litTotL + litTotR
                            if insert(sig, n, p, expr, op, False, lit_total):
                                if sig == target_sig and (not require_outer_mod_const):
                                    return expr
                                got = try_outer_mod_finish(p, expr, False, op, sig, n, lit_total)
                                if got is not None:
                                    return got

            # For const-bound pruning we need max abs of operand signatures
            def sig_abs_max(sig):
                return max(abs(int(v)) for v in sig)

            # -------- expr op CONST (right const) --------
            for lenL in range(1, n):
                left_bucket = cands_by_len.get(lenL, ())
                if not left_bucket:
                    continue
                for pL, sigL, eL, lastL, atomL, litTotL in left_bucket:
                    parL = needs_paren_binary(op, pL, "L", atomL, eL, lastL)
                    left_len_after = lenL + (2 if parL else 0)
                    need_const_len = n - left_len_after - op_len
                    if need_const_len <= 0:
                        continue

                    # Compute a safe absolute bound for the constant for monotone-growing ops
                    const_abs_bound = None
                    if op == "*":
                        amax = sig_abs_max(sigL)
                        if amax > 0:
                            const_abs_bound = max(0, value_cap // amax)
                    elif op == "<<":
                        const_abs_bound = min(max(bit_cap - bitlen_abs(a), 0) for a in sigL)
                    elif op == "**":
                        caps = []
                        for a in sigL:
                            aa = abs(int(a))
                            if aa >= 2:
                                caps.append(int(bit_cap // max(1.0, math.log2(aa))))
                        const_abs_bound = min(caps) if caps else bit_cap

                    for kind in ("pos", "neg"):
                        if op in ("<<", "**") and kind == "neg":
                            continue
                        if const_abs_bound is not None:
                            lo = min_abs_for_len(need_const_len, kind)
                            if const_abs_bound < lo:
                                continue
                        cmap = get_const_sig_map(need_const_len, N, kind)
                        if not cmap:
                            continue
                        for k_str, sigK in cmap.items():
                            kv = abs(int(sigK[0]))
                            if const_abs_bound is not None and kv > const_abs_bound:
                                continue
                            if op == "<<" and int(sigK[0]) < 0:
                                continue
                            if op == "**" and int(sigK[0]) < 0:
                                continue
                            sig = apply_bin_sig(op, sigL, sigK)
                            if sig is None:
                                continue
                            left_s = ("(" + eL + ")") if parL else eL
                            expr = left_s + op + k_str
                            lit_total = litTotL + byte_len(k_str)
                            if insert(sig, n, p, expr, op, False, lit_total):
                                if sig == target_sig and (not require_outer_mod_const or op == "%"):
                                    return expr
                                got = try_outer_mod_finish(p, expr, False, op, sig, n, lit_total)
                                if got is not None:
                                    return got

            # -------- CONST op expr (left const) --------
            for lenR in range(1, n):
                right_bucket = cands_by_len.get(lenR, ())
                if not right_bucket:
                    continue
                for pR, sigR, eR, lastR, atomR, litTotR in right_bucket:
                    parR = needs_paren_binary(op, pR, "R", atomR, eR, lastR)
                    right_len_after = lenR + (2 if parR else 0)

                    const_abs_bound = None
                    if op == "*":
                        bmax = sig_abs_max(sigR)
                        if bmax > 0:
                            const_abs_bound = max(0, value_cap // bmax)

                    if op != "**":
                        need_const_len = n - right_len_after - op_len
                        if need_const_len <= 0:
                            continue
                        for kind in ("pos", "neg"):
                            if op in ("<<",) and kind == "neg":
                                continue
                            if const_abs_bound is not None:
                                lo = min_abs_for_len(need_const_len, kind)
                                if const_abs_bound < lo:
                                    continue
                            cmap = get_const_sig_map(need_const_len, N, kind)
                            if not cmap:
                                continue
                            for k_str, sigK in cmap.items():
                                kv = abs(int(sigK[0]))
                                if const_abs_bound is not None and kv > const_abs_bound:
                                    continue
                                if op == "<<" and int(sigK[0]) < 0:
                                    continue
                                sig = apply_bin_sig(op, sigK, sigR)
                                if sig is None:
                                    continue
                                right_s = ("(" + eR + ")") if parR else eR
                                expr = k_str + op + right_s
                                lit_total = litTotR + byte_len(k_str)
                                if insert(sig, n, p, expr, op, False, lit_total):
                                    if sig == target_sig and (not require_outer_mod_const):
                                        return expr
                                    got = try_outer_mod_finish(p, expr, False, op, sig, n, lit_total)
                                    if got is not None:
                                        return got
                    else:
                        need_len_nonneg = n - right_len_after - op_len
                        if need_len_nonneg > 0:
                            cmap = get_const_sig_map(need_len_nonneg, N, "pos")
                            for k_str, sigK in cmap.items():
                                sig = apply_bin_sig(op, sigK, sigR)
                                if sig is None:
                                    continue
                                right_s = ("(" + eR + ")") if parR else eR
                                expr = k_str + op + right_s
                                lit_total = litTotR + byte_len(k_str)
                                if insert(sig, n, p, expr, op, False, lit_total):
                                    if sig == target_sig and (not require_outer_mod_const):
                                        return expr
                                    got = try_outer_mod_finish(p, expr, False, op, sig, n, lit_total)
                                    if got is not None:
                                        return got
                        need_len_neg_raw = n - right_len_after - op_len - 2
                        if need_len_neg_raw > 0:
                            cmap = get_const_sig_map(need_len_neg_raw, N, "neg")
                            for k_str, sigK in cmap.items():
                                sig = apply_bin_sig(op, sigK, sigR)
                                if sig is None:
                                    continue
                                right_s = ("(" + eR + ")") if parR else eR
                                expr = "(" + k_str + ")" + op + right_s
                                lit_total = litTotR + byte_len(k_str)
                                if insert(sig, n, p, expr, op, False, lit_total):
                                    if sig == target_sig and (not require_outer_mod_const):
                                        return expr
                                    got = try_outer_mod_finish(p, expr, False, op, sig, n, lit_total)
                                    if got is not None:
                                        return got

    return None

# Example
print(search_mapping({ 
    (0,0):0,
    (0,8):2,
    (0,16):0,
    (1,0):4,
    (1,8):6,
    (1,16):3,
    (2,0):0,
    (2,8):1,
    (2,16):0,
 }, 9))

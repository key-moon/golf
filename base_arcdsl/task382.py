def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_connect(a, b):
    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()

def val_func_shoot(start, direction):
    return val_func_connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = val_func_ulcorner(piece)[1] + val_func_lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def val_func_hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = val_func_ulcorner(piece)[0] + val_func_lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_portrait(piece):
    return val_func_height(piece) > val_func_width(piece)

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

def pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_astuple(a, b):
    return (a, b)

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_tojvec(j):
    return (0, j)

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_both(a, b):
    return a and b

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_size(container):
    return len(container)

def val_func_greater(a, b):
    return a > b

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_equality(a, b):
    return a == b

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_ofcolor(I, 2)
    x2 = val_func_portrait(x1)
    x3 = val_func_branch(x2, val_func_identity, val_func_dmirror)
    x4 = x3(I)
    x5 = val_func_leftmost(x1)
    x6 = val_func_equality(x5, 0)
    x7 = val_func_branch(x6, val_func_identity, val_func_vmirror)
    x8 = x7(x4)
    x9 = val_func_ofcolor(x8, 8)
    x10 = val_func_uppermost(x9)
    x11 = val_func_equality(x10, 0)
    x12 = val_func_branch(x11, val_func_identity, val_func_hmirror)
    x13 = x12(x8)
    x14 = val_func_ofcolor(x13, 8)
    x15 = val_func_ofcolor(x13, 2)
    x16 = val_func_rbind(val_func_shoot, (1, 0))
    x17 = mval_func_apply(x16, x14)
    x18 = val_func_height(x13)
    x19 = val_func_apply(val_func_first, x15)
    x20 = val_func_insert(0, x19)
    x21 = val_func_insert(x18, x19)
    x22 = val_func_apply(val_func_decrement, x21)
    x23 = val_func_order(x20, val_func_identity)
    x24 = val_func_order(x22, val_func_identity)
    x25 = val_func_size(x15)
    x26 = val_func_increment(x25)
    x27 = val_func_interval(0, x26, 1)
    x28 = val_func_apply(val_func_tojvec, x27)
    x29 = val_func_pair(x23, x24)
    x30 = val_func_lbind(val_func_sfilter, x17)
    x31 = val_func_compose(val_func_first, val_func_last)
    x32 = val_func_chain(val_func_decrement, val_func_first, val_func_first)
    x33 = val_func_fork(val_func_greater, x31, x32)
    x34 = val_func_chain(val_func_increment, val_func_last, val_func_first)
    x35 = val_func_fork(val_func_greater, x34, x31)
    x36 = val_func_fork(val_func_both, x33, x35)
    x37 = val_func_lbind(val_func_lbind, val_func_astuple)
    x38 = val_func_lbind(val_func_compose, x36)
    x39 = val_func_chain(x30, x38, x37)
    x40 = val_func_apply(x39, x29)
    x41 = pval_func_apply(val_func_shift, x40, x28)
    x42 = val_func_merge(x41)
    x43 = val_func_fill(x13, 8, x42)
    x44 = val_func_chain(x3, x7, x12)
    O = x44(x43)
    return [*map(list,O)]

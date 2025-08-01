def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

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

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

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

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

def underval_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = val_func_mostcolor(grid)
    g = list(list(r) for r in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_vline(patch):
    return val_func_height(patch) == len(patch) and val_func_width(patch) == 1

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_objects(grid, univalued, diagonal, without_bg):
    bg = val_func_mostcolor(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = val_func_asindices(grid)
    diagfun = val_func_neighbors if diagonal else val_func_dval_func_neighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

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

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_astuple(a, b):
    return (a, b)

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_tojvec(j):
    return (0, j)

def val_func_toivec(i):
    return (i, 0)

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_minimum(container):
    return min(container, default=0)

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_equality(a, b):
    return a == b

def val_func_invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def val_func_add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, False, False, True)
    x2 = val_func_matcher(val_func_first, 2)
    x3 = val_func_rbind(val_func_sfilter, x2)
    x4 = val_func_compose(val_func_lowermost, x3)
    x5 = val_func_compose(val_func_rightmost, x3)
    x6 = val_func_compose(val_func_uppermost, x3)
    x7 = val_func_compose(val_func_leftmost, x3)
    x8 = val_func_fork(val_func_equality, x4, val_func_lowermost)
    x9 = val_func_fork(val_func_equality, x5, val_func_rightmost)
    x10 = val_func_fork(val_func_equality, x6, val_func_uppermost)
    x11 = val_func_fork(val_func_equality, x7, val_func_leftmost)
    x12 = val_func_compose(val_func_invert, x10)
    x13 = val_func_compose(val_func_invert, x11)
    x14 = val_func_fork(val_func_add, x12, x8)
    x15 = val_func_fork(val_func_add, x13, x9)
    x16 = val_func_fork(val_func_astuple, x14, x15)
    x17 = val_func_compose(val_func_center, x3)
    x18 = val_func_fork(val_func_shoot, x17, x16)
    x19 = mval_func_apply(x18, x1)
    x20 = val_func_fill(I, 2, x19)
    x21 = val_func_compose(val_func_vline, x18)
    x22 = val_func_sfilter(x1, x21)
    x23 = val_func_difference(x1, x22)
    x24 = val_func_chain(val_func_decrement, val_func_minimum, val_func_shape)
    x25 = val_func_compose(val_func_increment, x24)
    x26 = val_func_compose(val_func_invert, x24)
    x27 = val_func_rbind(val_func_interval, 1)
    x28 = val_func_fork(x27, x26, x25)
    x29 = val_func_lbind(val_func_apply, val_func_toivec)
    x30 = val_func_lbind(val_func_apply, val_func_tojvec)
    x31 = val_func_lbind(val_func_lbind, val_func_shift)
    x32 = val_func_compose(x31, x18)
    x33 = val_func_compose(x29, x28)
    x34 = val_func_compose(x30, x28)
    x35 = val_func_fork(mval_func_apply, x32, x33)
    x36 = val_func_fork(mval_func_apply, x32, x34)
    x37 = mval_func_apply(x35, x23)
    x38 = mval_func_apply(x36, x22)
    x39 = val_func_combine(x37, x38)
    O = underval_func_fill(x20, 3, x39)
    return [*map(list,O)]

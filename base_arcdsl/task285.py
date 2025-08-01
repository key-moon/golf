def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

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

def val_func_manhattan(a, b):
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in val_func_toindices(a) for bi, bj in val_func_toindices(b))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_backdrop(patch):
    if len(patch) == 0:
        return frozenset({})
    indices = val_func_toindices(patch)
    si, sj = val_func_ulcorner(indices)
    ei, ej = val_func_lrcorner(patch)
    return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))

def val_func_delta(patch):
    if len(patch) == 0:
        return frozenset({})
    return val_func_backdrop(patch) - val_func_toindices(patch)

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def val_func_position(a, b):
    ia, ja = val_func_center(val_func_toindices(a))
    ib, jb = val_func_center(val_func_toindices(b))
    if ia == ib:
        return (0, 1 if ja < jb else -1)
    elif ja == jb:
        return (1 if ia < ib else -1, 0)
    elif ia < ib:
        return (1, 1 if ja < jb else -1)
    elif ia > ib:
        return (-1, 1 if ja < jb else -1)

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

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

def val_func_adjacent(a, b):
    return val_func_manhattan(a, b) == 1

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

def val_func_recolor(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

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

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_extract(container, condition):
    return next(e for e in container if condition(e))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_tojvec(j):
    return (0, j)

def val_func_toivec(i):
    return (i, 0)

def val_func_crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1))

def val_func_initset(value):
    return frozenset({value})

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_intersection(a, b):
    return a & b

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_equality(a, b):
    return a == b

def val_func_invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def val_func_multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, False, True, True)
    x2 = val_func_lbind(val_func_rbind, val_func_equality)
    x3 = val_func_rbind(val_func_compose, val_func_first)
    x4 = val_func_chain(x3, x2, val_func_mostcolor)
    x5 = val_func_fork(val_func_sfilter, val_func_identity, x4)
    x6 = val_func_fork(val_func_difference, val_func_identity, x5)
    x7 = val_func_lbind(val_func_rbind, val_func_adjacent)
    x8 = val_func_rbind(val_func_compose, val_func_initset)
    x9 = val_func_chain(x8, x7, x6)
    x10 = val_func_fork(val_func_extract, x5, x9)
    x11 = val_func_fork(val_func_insert, x10, x6)
    x12 = val_func_lbind(val_func_recolor, 0)
    x13 = val_func_chain(x12, val_func_delta, x11)
    x14 = val_func_fork(val_func_combine, x11, x13)
    x15 = val_func_fork(val_func_position, x5, x6)
    x16 = val_func_chain(val_func_toivec, val_func_first, x15)
    x17 = val_func_chain(val_func_tojvec, val_func_last, x15)
    x18 = val_func_fork(val_func_multiply, val_func_shape, x16)
    x19 = val_func_fork(val_func_multiply, val_func_shape, x17)
    x20 = val_func_fork(val_func_multiply, val_func_shape, x15)
    x21 = val_func_fork(val_func_shift, val_func_hmirror, x18)
    x22 = val_func_fork(val_func_shift, val_func_vmirror, x19)
    x23 = val_func_compose(val_func_hmirror, val_func_vmirror)
    x24 = val_func_fork(val_func_shift, x23, x20)
    x25 = val_func_lbind(val_func_compose, x5)
    x26 = x25(x21)
    x27 = x25(x22)
    x28 = x25(x24)
    x29 = val_func_compose(val_func_crement, val_func_invert)
    x30 = val_func_lbind(val_func_compose, x29)
    x31 = x30(x16)
    x32 = x30(x17)
    x33 = x30(x15)
    x34 = val_func_fork(val_func_shift, x26, x31)
    x35 = val_func_fork(val_func_shift, x27, x32)
    x36 = val_func_fork(val_func_shift, x28, x33)
    x37 = val_func_lbind(val_func_index, I)
    x38 = val_func_lbind(val_func_compose, val_func_toindices)
    x39 = x38(x14)
    x40 = x38(x34)
    x41 = x38(x35)
    x42 = x38(x36)
    x43 = val_func_fork(val_func_intersection, x39, x40)
    x44 = val_func_fork(val_func_intersection, x39, x41)
    x45 = val_func_fork(val_func_intersection, x39, x42)
    x46 = val_func_chain(x37, val_func_first, x43)
    x47 = val_func_chain(x37, val_func_first, x44)
    x48 = val_func_chain(x37, val_func_first, x45)
    x49 = val_func_fork(val_func_recolor, x46, x34)
    x50 = val_func_fork(val_func_recolor, x47, x35)
    x51 = val_func_fork(val_func_recolor, x48, x36)
    x52 = mval_func_apply(x49, x1)
    x53 = mval_func_apply(x50, x1)
    x54 = mval_func_apply(x51, x1)
    x55 = val_func_paint(I, x52)
    x56 = val_func_paint(x55, x53)
    O = val_func_paint(x56, x54)
    return [*map(list,O)]

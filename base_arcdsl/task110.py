def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

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

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_normalize(patch):
    if len(patch) == 0:
        return patch
    return val_func_shift(patch, (-val_func_uppermost(patch), -val_func_leftmost(patch)))

def val_func_vperiod(obj):
    val_func_normalized = val_func_normalize(obj)
    h = val_func_height(val_func_normalized)
    for p in range(1, h):
        offsetted = val_func_shift(val_func_normalized, (-p, 0))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if i >= 0})
        if pruned.issubset(val_func_normalized):
            return p

def val_func_hperiod(obj):
    val_func_normalized = val_func_normalize(obj)
    w = val_func_width(val_func_normalized)
    for p in range(1, w):
        offsetted = val_func_shift(val_func_normalized, (0, -p))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
        if pruned.issubset(val_func_normalized):
            return p
    return w

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def val_func_partition(grid):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value) for value in val_func_palette(grid))

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

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

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_power(function, n):
    if n == 1:
        return function
    return val_func_compose(function, val_func_power(function, n - 1))

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_astuple(a, b):
    return (a, b)

def val_func_tojvec(j):
    return (0, j)

def val_func_toivec(i):
    return (i, 0)

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_height(I)
    x2 = val_func_width(I)
    x3 = val_func_partition(I)
    x4 = val_func_colorfilter(x3, 0)
    x5 = val_func_difference(x3, x4)
    x6 = val_func_merge(x5)
    x7 = val_func_astuple(x1, 2)
    x8 = val_func_astuple(2, x2)
    x9 = val_func_power(val_func_decrement, 2)
    x10 = x9(x1)
    x11 = x9(x2)
    x12 = val_func_toivec(x11)
    x13 = val_func_tojvec(x10)
    x14 = val_func_crop(I, x12, x8)
    x15 = val_func_crop(I, x13, x7)
    x16 = val_func_asobject(x15)
    x17 = val_func_asobject(x14)
    x18 = val_func_vperiod(x16)
    x19 = val_func_hperiod(x17)
    x20 = val_func_astuple(x18, x19)
    x21 = val_func_lbind(val_func_multiply, x20)
    x22 = val_func_neighbors((0, 0))
    x23 = mval_func_apply(val_func_neighbors, x22)
    x24 = val_func_apply(x21, x23)
    x25 = val_func_lbind(val_func_shift, x6)
    x26 = mval_func_apply(x25, x24)
    O = val_func_paint(I, x26)
    return [*map(list,O)]

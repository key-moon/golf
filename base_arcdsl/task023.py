def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

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

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

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

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_occurrences(grid, obj):
    occs = set()
    normed = val_func_normalize(obj)
    h, w = len(grid), len(grid[0])
    oh, ow = val_func_shape(obj)
    h2, w2 = h - oh + 1, w - ow + 1
    for i in range(h2):
        for j in range(w2):
            occurs = True
            for v, (a, b) in val_func_shift(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and grid[a][b] == v):
                    occurs = False
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_vconcat(a, b):
    return a + b

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

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

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

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_canvas(5, (2, 2))
    x2 = val_func_asobject(x1)
    x3 = val_func_occurrences(I, x2)
    x4 = val_func_lbind(val_func_shift, x2)
    x5 = mval_func_apply(x4, x3)
    x6 = val_func_fill(I, 8, x5)
    x7 = val_func_canvas(5, (1, 1))
    x8 = val_func_astuple(2, 1)
    x9 = val_func_canvas(8, x8)
    x10 = val_func_vconcat(x9, x7)
    x11 = val_func_asobject(x10)
    x12 = val_func_occurrences(x6, x11)
    x13 = val_func_lbind(val_func_shift, x11)
    x14 = mval_func_apply(x13, x12)
    x15 = val_func_fill(x6, 2, x14)
    x16 = val_func_astuple(1, 3)
    x17 = val_func_canvas(5, x16)
    x18 = val_func_asobject(x17)
    x19 = val_func_occurrences(x15, x18)
    x20 = val_func_lbind(val_func_shift, x18)
    x21 = mval_func_apply(x20, x19)
    x22 = val_func_fill(x15, 2, x21)
    x23 = val_func_hmirror(x10)
    x24 = val_func_asobject(x23)
    x25 = val_func_occurrences(x22, x24)
    x26 = val_func_lbind(val_func_shift, x24)
    x27 = mval_func_apply(x26, x25)
    x28 = val_func_fill(x22, 2, x27)
    x29 = val_func_dmirror(x10)
    x30 = val_func_asobject(x29)
    x31 = val_func_occurrences(x28, x30)
    x32 = val_func_lbind(val_func_shift, x30)
    x33 = mval_func_apply(x32, x31)
    x34 = val_func_fill(x28, 2, x33)
    x35 = val_func_vmirror(x29)
    x36 = val_func_asobject(x35)
    x37 = val_func_occurrences(x34, x36)
    x38 = val_func_lbind(val_func_shift, x36)
    x39 = mval_func_apply(x38, x37)
    O = val_func_fill(x34, 2, x39)
    return [*map(list,O)]

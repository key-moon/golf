def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in val_func_toindices(patch) if 0 <= i < h and 0 <= j < w)

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_maximum(container):
    return max(container, default=0)

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_asindices(I)
    x2 = val_func_dmirror(I)
    x3 = val_func_invert(9)
    x4 = val_func_pval_func_apply(val_func_pair, I, x2)
    x5 = val_func_lbind(val_func_apply, val_func_maximum)
    x6 = val_func_apply(x5, x4)
    x7 = val_func_ofcolor(x6, 0)
    x8 = val_func_difference(x1, x7)
    x9 = val_func_toobject(x8, x6)
    x10 = val_func_interval(x3, 9, 1)
    x11 = val_func_interval(9, x3, -1)
    x12 = val_func_pair(x10, x11)
    x13 = val_func_lbind(val_func_shift, x9)
    x14 = mval_func_apply(x13, x12)
    O = val_func_paint(x6, x14)
    return [*map(list,O)]

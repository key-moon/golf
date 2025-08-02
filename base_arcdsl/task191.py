def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_normalize(patch):
    if len(patch) == 0:
        return patch
    return val_func_shift(patch, (-val_func_uppermost(patch), -val_func_leftmost(patch)))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

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

def mpval_func_apply(function, a, b):
    return val_func_merge(pval_func_apply(function, a, b))

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

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_product(a, b):
    return frozenset((i, j) for j in b for i in a)

def val_func_astuple(a, b):
    return (a, b)

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_size(container):
    return len(container)

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_height(I)
    x2 = val_func_width(I)
    x3 = val_func_ofcolor(I, 1)
    x4 = val_func_ofcolor(I, 4)
    x5 = val_func_ulcorner(x3)
    x6 = val_func_subgrid(x3, I)
    x7 = val_func_rot90(x6)
    x8 = val_func_rot180(x6)
    x9 = val_func_rot270(x6)
    x10 = val_func_matcher(val_func_size, 0)
    x11 = val_func_rbind(val_func_ofcolor, 1)
    x12 = val_func_compose(val_func_normalize, x11)
    x13 = val_func_rbind(val_func_ofcolor, 4)
    x14 = val_func_rbind(val_func_shift, x5)
    x15 = val_func_compose(x14, x13)
    x16 = val_func_lbind(val_func_subtract, x1)
    x17 = val_func_chain(val_func_increment, x16, val_func_height)
    x18 = val_func_lbind(val_func_subtract, x2)
    x19 = val_func_chain(val_func_increment, x18, val_func_width)
    x20 = val_func_rbind(val_func_interval, 1)
    x21 = val_func_lbind(x20, 0)
    x22 = val_func_compose(x21, x17)
    x23 = val_func_compose(x21, x19)
    x24 = val_func_fork(val_func_product, x22, x23)
    x25 = val_func_rbind(val_func_shift, (-1, -1))
    x26 = val_func_lbind(val_func_lbind, val_func_shift)
    x27 = val_func_chain(x26, x25, x12)
    x28 = val_func_astuple(x6, x7)
    x29 = val_func_astuple(x8, x9)
    x30 = val_func_combine(x28, x29)
    x31 = val_func_apply(x15, x30)
    x32 = val_func_lbind(val_func_difference, x4)
    x33 = val_func_apply(x32, x31)
    x34 = val_func_apply(val_func_normalize, x31)
    x35 = val_func_apply(x24, x34)
    x36 = val_func_lbind(val_func_rbind, val_func_difference)
    x37 = val_func_apply(x26, x34)
    x38 = val_func_apply(x36, x33)
    x39 = pval_func_apply(val_func_compose, x38, x37)
    x40 = val_func_lbind(val_func_compose, x10)
    x41 = val_func_apply(x40, x39)
    x42 = pval_func_apply(val_func_sfilter, x35, x41)
    x43 = val_func_apply(x27, x30)
    x44 = mpval_func_apply(mval_func_apply, x43, x42)
    O = val_func_fill(I, 1, x44)
    return [*map(list,O)]

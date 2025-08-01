def val_func_pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def mval_func_pval_func_apply(function, a, b):
    return val_func_merge(val_func_pval_func_apply(function, a, b))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_astuple(a, b):
    return (a, b)

def val_func_tojvec(j):
    return (0, j)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_crop(I, (0, 0), (3, 3))
    x2 = val_func_rot90(x1)
    x3 = val_func_rot180(x1)
    x4 = val_func_astuple(x2, x3)
    x5 = val_func_astuple(4, 8)
    x6 = val_func_apply(val_func_tojvec, x5)
    x7 = val_func_apply(val_func_asobject, x4)
    x8 = mval_func_pval_func_apply(val_func_shift, x7, x6)
    O = val_func_paint(I, x8)
    return [*map(list,O)]

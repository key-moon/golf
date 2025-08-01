def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

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

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_vconcat(a, b):
    return a + b

def val_func_hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_astuple(a, b):
    return (a, b)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_repeat(item, num):
    return tuple(item for i in range(num))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_width(I)
    x2 = val_func_astuple(2, x1)
    x3 = val_func_crop(I, (0, 0), x2)
    x4 = val_func_tophalf(x3)
    x5 = val_func_dmirror(x4)
    x6 = val_func_hupscale(x5, x1)
    x7 = val_func_repeat(x6, 2)
    x8 = val_func_merge(x7)
    O = val_func_vconcat(x3, x8)
    return [*map(list,O)]

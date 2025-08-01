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

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_downscale(grid, factor):
    h, w = len(grid), len(grid[0])
    g = tuple()
    for i in range(h):
        r = tuple()
        for j in range(w):
            if j % factor == 0:
                r = r + (grid[i][j],)
        g = g + (r, )
    h = len(g)
    dsg = tuple()
    for i in range(h):
        if i % factor == 0:
            dsg = dsg + (g[i],)
    return dsg

def val_func_upscale(element, factor):
    if isinstance(element, tuple):
        g = tuple()
        for row in element:
            val_func_upscaled_row = tuple()
            for value in row:
                val_func_upscaled_row = val_func_upscaled_row + tuple(value for num in range(factor))
            g = g + tuple(val_func_upscaled_row for num in range(factor))
        return g
    else:
        if len(element) == 0:
            return frozenset()
        di_inv, dj_inv = val_func_ulcorner(element)
        di, dj = (-di_inv, -dj_inv)
        normed_obj = val_func_shift(element, (di, dj))
        o = set()
        for value, (i, j) in normed_obj:
            for io in range(factor):
                for jo in range(factor):
                    o.add((value, (i * factor + io, j * factor + jo)))
        return val_func_shift(frozenset(o), (di_inv, dj_inv))

def val_func_rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_rot180(I)
    x2 = val_func_downscale(x1, 2)
    x3 = val_func_rot180(x2)
    O = val_func_upscale(x3, 4)
    return [*map(list,O)]

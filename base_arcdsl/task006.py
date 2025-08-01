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

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_righthalf(grid):
    return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))

def val_func_lefthalf(grid):
    return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_cellwise(a, b, fallback):
    h, w = len(a), len(a[0])
    resulting_grid = tuple()
    for i in range(h):
        row = tuple()
        for j in range(w):
            a_value = a[i][j]
            value = a_value if a_value == b[i][j] else fallback
            row = row + (value,)
        resulting_grid = resulting_grid + (row, )
    return resulting_grid

def val_func_vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = val_func_ulcorner(piece)[1] + val_func_lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_vmirror(I)
    x2 = val_func_lefthalf(x1)
    x3 = val_func_righthalf(x1)
    x4 = val_func_vmirror(x3)
    x5 = val_func_cellwise(x2, x4, 0)
    O = val_func_replace(x5, 1, 2)
    return [*map(list,O)]

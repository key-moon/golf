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

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_righthalf(grid):
    return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))

def val_func_lefthalf(grid):
    return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))

def val_func_bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_tophalf(I)
    x2 = val_func_bottomhalf(I)
    x3 = val_func_lefthalf(x1)
    x4 = val_func_righthalf(x1)
    x5 = val_func_lefthalf(x2)
    x6 = val_func_righthalf(x2)
    x7 = val_func_ofcolor(x4, 4)
    x8 = val_func_ofcolor(x3, 7)
    x9 = val_func_ofcolor(x5, 8)
    x10 = val_func_fill(x6, 8, x9)
    x11 = val_func_fill(x10, 4, x7)
    O = val_func_fill(x11, 7, x8)
    return [*map(list,O)]

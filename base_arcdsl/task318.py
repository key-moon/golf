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

def val_func_bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_astuple(a, b):
    return (a, b)

def val_func_intersection(a, b):
    return a & b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_tophalf(I)
    x2 = val_func_bottomhalf(I)
    x3 = val_func_ofcolor(x1, 0)
    x4 = val_func_ofcolor(x2, 0)
    x5 = val_func_intersection(x3, x4)
    x6 = val_func_astuple(4, 4)
    x7 = val_func_canvas(3, x6)
    O = val_func_fill(x7, 0, x5)
    return [*map(list,O)]

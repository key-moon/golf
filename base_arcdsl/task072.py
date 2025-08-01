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

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_intersection(a, b):
    return a & b

def val_func_combine(a, b):
    return type(a)((*a, *b))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_tophalf(I)
    x2 = val_func_bottomhalf(I)
    x3 = val_func_astuple(6, 5)
    x4 = val_func_ofcolor(x1, 2)
    x5 = val_func_ofcolor(x2, 2)
    x6 = val_func_combine(x4, x5)
    x7 = val_func_intersection(x4, x5)
    x8 = val_func_difference(x6, x7)
    x9 = val_func_canvas(0, x3)
    O = val_func_fill(x9, 3, x8)
    return [*map(list,O)]

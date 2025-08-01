def val_func_vconcat(a, b):
    return a + b

def val_func_hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_rot90(I)
    x2 = val_func_rot180(I)
    x3 = val_func_rot270(I)
    x4 = val_func_hconcat(I, x1)
    x5 = val_func_hconcat(x3, x2)
    O = val_func_vconcat(x4, x5)
    return [*map(list,O)]

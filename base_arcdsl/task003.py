def val_func_bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_vconcat(a, b):
    return a + b

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_equality(a, b):
    return a == b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_tophalf(I)
    x2 = val_func_bottomhalf(I)
    x3 = val_func_equality(x1, x2)
    x4 = val_func_crop(I, (2, 0), (3, 3))
    x5 = val_func_branch(x3, x2, x4)
    x6 = val_func_vconcat(I, x5)
    O = val_func_replace(x6, 1, 2)
    return [*map(list,O)]

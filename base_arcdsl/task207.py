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

def val_func_astuple(a, b):
    return (a, b)

def val_func_leastcommon(container):
    return min(set(container), key=container.count)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_lefthalf(I)
    x2 = val_func_righthalf(I)
    x3 = val_func_tophalf(x1)
    x4 = val_func_tophalf(x2)
    x5 = val_func_bottomhalf(x1)
    x6 = val_func_bottomhalf(x2)
    x7 = val_func_astuple(x3, x4)
    x8 = val_func_astuple(x5, x6)
    x9 = val_func_combine(x7, x8)
    O = val_func_leastcommon(x9)
    return [*map(list,O)]

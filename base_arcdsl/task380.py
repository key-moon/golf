def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def p(I):
    I=tuple(map(tuple,I))
    O = val_func_rot270(I)
    return [*map(list,O)]

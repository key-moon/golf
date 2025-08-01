def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def p(I):
    I=tuple(map(tuple,I))
    O = val_func_replace(I, 7, 5)
    return [*map(list,O)]

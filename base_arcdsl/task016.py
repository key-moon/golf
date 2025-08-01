def val_func_switch(grid, a, b):
    return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_switch(I, 3, 4)
    x2 = val_func_switch(x1, 8, 9)
    x3 = val_func_switch(x2, 2, 6)
    O = val_func_switch(x3, 1, 5)
    return [*map(list,O)]

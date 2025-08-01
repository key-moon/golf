def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_leastcolor(I)
    x2 = val_func_replace(I, x1, 0)
    x3 = val_func_leastcolor(x2)
    O = val_func_replace(x2, x3, x1)
    return [*map(list,O)]

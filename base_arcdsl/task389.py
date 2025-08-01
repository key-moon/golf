def val_func_switch(grid, a, b):
    return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_palette(I)
    x2 = val_func_first(x1)
    x3 = val_func_last(x1)
    x4 = val_func_switch(I, x2, x3)
    O = val_func_replace(x4, 5, 0)
    return [*map(list,O)]

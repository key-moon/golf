def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_first(container):
    return next(iter(container))

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_astuple(a, b):
    return (a, b)

def val_func_other(container, value):
    return val_func_first(val_func_remove(value, container))

def val_func_size(container):
    return len(container)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_palette(I)
    x2 = val_func_other(x1, 0)
    x3 = val_func_ofcolor(I, x2)
    x4 = val_func_size(x3)
    x5 = val_func_astuple(1, x4)
    O = val_func_canvas(x2, x5)
    return [*map(list,O)]

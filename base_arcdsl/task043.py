def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

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

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_underfill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = val_func_mostcolor(grid)
    g = list(list(r) for r in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def val_func_urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_power(function, n):
    if n == 1:
        return function
    return val_func_compose(function, val_func_power(function, n - 1))

def val_func_product(a, b):
    return frozenset((i, j) for j in b for i in a)

def val_func_astuple(a, b):
    return (a, b)

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_ofcolor(I, 5)
    x2 = val_func_product(x1, x1)
    x3 = val_func_power(val_func_first, 2)
    x4 = val_func_power(val_func_last, 2)
    x5 = val_func_fork(val_func_astuple, x3, x4)
    x6 = val_func_apply(x5, x2)
    x7 = val_func_urcorner(x1)
    x8 = val_func_remove(x7, x6)
    O = val_func_underfill(I, 2, x8)
    return [*map(list,O)]

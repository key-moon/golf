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

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_size(container):
    return len(container)

def val_func_greater(a, b):
    return a > b

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_leastcolor(I)
    x2 = val_func_ofcolor(I, x1)
    x3 = val_func_rbind(val_func_difference, x2)
    x4 = val_func_rbind(val_func_greater, 2)
    x5 = val_func_chain(x4, val_func_size, x3)
    x6 = val_func_compose(x5, val_func_dneighbors)
    x7 = val_func_sfilter(x2, x6)
    O = val_func_fill(I, 0, x7)
    return [*map(list,O)]

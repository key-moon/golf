def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_first(container):
    return next(iter(container))

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

def val_func_hfrontier(location):
    return frozenset((location[0], j) for j in range(30))

def val_func_vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_other(container, value):
    return val_func_first(val_func_remove(value, container))

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_equality(a, b):
    return a == b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_palette(I)
    x2 = val_func_other(x1, 0)
    x3 = val_func_equality(x2, 1)
    x4 = val_func_equality(x2, 2)
    x5 = val_func_branch(x3, (1, 1), (2, 2))
    x6 = val_func_branch(x4, (0, 1), x5)
    x7 = val_func_fork(val_func_combine, val_func_vfrontier, val_func_hfrontier)
    x8 = x7(x6)
    x9 = val_func_canvas(0, (3, 3))
    O = val_func_fill(x9, 5, x8)
    return [*map(list,O)]

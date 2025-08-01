def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_astuple(a, b):
    return (a, b)

def val_func_tojvec(j):
    return (0, j)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_leastcolor(I)
    x2 = val_func_crop(I, (0, 0), (3, 3))
    x3 = val_func_crop(I, (2, 0), (3, 3))
    x4 = val_func_tojvec(4)
    x5 = val_func_crop(I, x4, (3, 3))
    x6 = val_func_astuple(2, 4)
    x7 = val_func_crop(I, x6, (3, 3))
    x8 = val_func_canvas(0, (3, 3))
    x9 = val_func_rbind(val_func_ofcolor, x1)
    x10 = val_func_astuple(x2, x3)
    x11 = val_func_astuple(x5, x7)
    x12 = val_func_combine(x10, x11)
    x13 = mval_func_apply(x9, x12)
    O = val_func_fill(x8, x1, x13)
    return [*map(list,O)]

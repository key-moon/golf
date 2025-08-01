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

def val_func_hfrontier(location):
    return frozenset((location[0], j) for j in range(30))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_ofcolor(I, 5)
    x2 = val_func_lbind(val_func_matcher, val_func_last)
    x3 = val_func_lbind(val_func_sfilter, x1)
    x4 = val_func_lbind(val_func_mval_func_apply, val_func_hfrontier)
    x5 = val_func_chain(x4, x3, x2)
    x6 = x5(0)
    x7 = x5(2)
    x8 = x5(1)
    x9 = val_func_fill(I, 2, x6)
    x10 = val_func_fill(x9, 3, x7)
    O = val_func_fill(x10, 4, x8)
    return [*map(list,O)]

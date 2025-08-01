def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_bordering(patch, grid):
    return val_func_uppermost(patch) == 0 or val_func_leftmost(patch) == 0 or val_func_lowermost(patch) == len(grid) - 1 or val_func_rightmost(patch) == len(grid[0]) - 1

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_mfilter(container, function):
    return val_func_merge(val_func_sfilter(container, function))

def val_func_initset(value):
    return frozenset({value})

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_asindices(I)
    x2 = val_func_apply(val_func_initset, x1)
    x3 = val_func_rbind(val_func_bordering, I)
    x4 = val_func_mfilter(x2, x3)
    O = val_func_fill(I, 8, x4)
    return [*map(list,O)]

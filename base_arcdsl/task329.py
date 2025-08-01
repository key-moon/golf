def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

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

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_flip(b):
    return not b

def val_func_halve(n):
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_asindices(I)
    x2 = val_func_width(I)
    x3 = val_func_halve(x2)
    x4 = val_func_matcher(val_func_last, x3)
    x5 = val_func_compose(val_func_flip, x4)
    x6 = val_func_sfilter(x1, x5)
    O = val_func_fill(I, 0, x6)
    return [*map(list,O)]

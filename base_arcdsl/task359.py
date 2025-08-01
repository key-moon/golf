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

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_vupscale(grid, factor):
    g = tuple()
    for row in grid:
        g = g + tuple(row for num in range(factor))
    return g

def val_func_hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_mostcommon(container):
    return max(set(container), key=container.count)

def val_func_size(container):
    return len(container)

def val_func_greater(a, b):
    return a > b

def val_func_repeat(item, num):
    return tuple(item for i in range(num))

def val_func_dedupe(tup):
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_rot90(I)
    x2 = val_func_apply(val_func_mostcommon, I)
    x3 = val_func_apply(val_func_mostcommon, x1)
    x4 = val_func_repeat(x2, 1)
    x5 = val_func_repeat(x3, 1)
    x6 = val_func_compose(val_func_size, val_func_dedupe)
    x7 = x6(x2)
    x8 = x6(x3)
    x9 = val_func_greater(x8, x7)
    x10 = val_func_branch(x9, val_func_height, val_func_width)
    x11 = x10(I)
    x12 = val_func_rot90(x4)
    x13 = val_func_branch(x9, x5, x12)
    x14 = val_func_branch(x9, val_func_vupscale, val_func_hupscale)
    O = x14(x13, x11)
    return [*map(list,O)]

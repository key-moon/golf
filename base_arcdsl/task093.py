def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

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

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_righthalf(grid):
    return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))

def val_func_lefthalf(grid):
    return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_portrait(piece):
    return val_func_height(piece) > val_func_width(piece)

def val_func_leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

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

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_leastcolor(I)
    x2 = val_func_replace(I, x1, 5)
    x3 = val_func_ofcolor(I, 5)
    x4 = val_func_portrait(x3)
    x5 = val_func_branch(x4, val_func_identity, val_func_dmirror)
    x6 = x5(x2)
    x7 = val_func_lefthalf(x6)
    x8 = val_func_righthalf(x6)
    x9 = val_func_rbind(val_func_order, val_func_identity)
    x10 = val_func_rbind(val_func_order, val_func_invert)
    x11 = val_func_apply(x9, x7)
    x12 = val_func_apply(x10, x8)
    x13 = val_func_hconcat(x11, x12)
    O = x5(x13)
    return [*map(list,O)]

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

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = val_func_ulcorner(piece)[1] + val_func_lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_cmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*(r[::-1] for r in piece[::-1])))
    return val_func_vmirror(val_func_dmirror(val_func_vmirror(piece)))

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_maximum(container):
    return max(container, default=0)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_replace(I, 4, 0)
    x2 = val_func_dmirror(x1)
    x3 = pval_func_apply(val_func_pair, x1, x2)
    x4 = val_func_lbind(val_func_apply, val_func_maximum)
    x5 = val_func_apply(x4, x3)
    x6 = val_func_cmirror(x5)
    x7 = pval_func_apply(val_func_pair, x5, x6)
    x8 = val_func_apply(x4, x7)
    O = val_func_cmirror(x8)
    return [*map(list,O)]

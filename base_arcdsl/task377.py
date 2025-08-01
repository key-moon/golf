def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

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

def val_func_vconcat(a, b):
    return a + b

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = val_func_ulcorner(piece)[0] + val_func_lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_dedupe(tup):
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_compose(val_func_dmirror, val_func_dedupe)
    x2 = x1(I)
    x3 = x1(x2)
    x4 = val_func_fork(val_func_remove, val_func_last, val_func_identity)
    x5 = val_func_compose(val_func_hmirror, x4)
    x6 = val_func_fork(val_func_vconcat, val_func_identity, x5)
    x7 = x6(x3)
    x8 = val_func_dmirror(x7)
    O = x6(x8)
    return [*map(list,O)]

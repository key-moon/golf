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

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_vsplit(grid, n):
    h, w = len(grid) // n, len(grid[0])
    offset = len(grid) % n != 0
    return tuple(val_func_crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_extract(container, condition):
    return next(e for e in container if condition(e))

def val_func_equality(a, b):
    return a == b

def val_func_flip(b):
    return not b

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_vsplit(I, 3)
    x2 = val_func_fork(val_func_equality, val_func_dmirror, val_func_identity)
    x3 = val_func_compose(val_func_flip, x2)
    O = val_func_extract(x1, x3)
    return [*map(list,O)]

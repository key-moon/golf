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

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_recolor(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def val_func_prval_func_apply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

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

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

def val_func_invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def val_func_multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_ofcolor(I, 2)
    x2 = val_func_replace(I, 2, 0)
    x3 = val_func_leastcolor(x2)
    x4 = val_func_ofcolor(x2, x3)
    x5 = val_func_combine(x1, x4)
    x6 = val_func_recolor(x3, x5)
    x7 = val_func_compose(val_func_decrement, val_func_double)
    x8 = val_func_ulcorner(x5)
    x9 = val_func_invert(x8)
    x10 = val_func_shift(x1, x9)
    x11 = val_func_apply(x7, x10)
    x12 = val_func_interval(0, 9, 1)
    x13 = val_func_prval_func_apply(val_func_multiply, x11, x12)
    x14 = val_func_lbind(val_func_shift, x6)
    x15 = mval_func_apply(x14, x13)
    O = val_func_paint(I, x15)
    return [*map(list,O)]

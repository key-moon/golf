def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def val_func_underfill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = val_func_mostval_func_color(grid)
    g = list(list(r) for r in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_partition(grid):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value) for value in val_func_palette(grid))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

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

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_product(a, b):
    return frozenset((i, j) for j in b for i in a)

def val_func_astuple(a, b):
    return (a, b)

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_totuple(container):
    return tuple(container)

def val_func_extract(container, condition):
    return next(e for e in container if condition(e))

def val_func_initset(value):
    return frozenset({value})

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_flip(b):
    return not b

def val_func_divide(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)

def val_func_multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def val_func_subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def val_func_add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_height(I)
    x2 = val_func_mostval_func_color(I)
    x3 = val_func_asobject(I)
    x4 = val_func_subtract(x1, 2)
    x5 = val_func_divide(x4, 3)
    x6 = val_func_astuple(x5, x5)
    x7 = val_func_crop(I, (0, 0), x6)
    x8 = val_func_partition(x7)
    x9 = val_func_matcher(val_func_color, 0)
    x10 = val_func_compose(val_func_flip, x9)
    x11 = val_func_extract(x8, x10)
    x12 = val_func_initset(x2)
    x13 = val_func_palette(x3)
    x14 = val_func_palette(x11)
    x15 = val_func_difference(x13, x14)
    x16 = val_func_difference(x15, x12)
    x17 = val_func_first(x16)
    x18 = val_func_interval(0, 3, 1)
    x19 = val_func_product(x18, x18)
    x20 = val_func_totuple(x19)
    x21 = val_func_apply(val_func_first, x20)
    x22 = val_func_apply(val_func_last, x20)
    x23 = val_func_lbind(val_func_multiply, x5)
    x24 = val_func_apply(x23, x21)
    x25 = val_func_apply(x23, x22)
    x26 = val_func_pval_func_apply(val_func_add, x24, x21)
    x27 = val_func_pval_func_apply(val_func_add, x25, x22)
    x28 = val_func_pval_func_apply(val_func_astuple, x26, x27)
    x29 = val_func_lbind(val_func_shift, x11)
    x30 = mval_func_apply(x29, x28)
    O = val_func_underfill(I, x17, x30)
    return [*map(list,O)]

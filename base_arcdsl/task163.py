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

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in val_func_toindices(patch) if 0 <= i < h and 0 <= j < w)

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_recolor(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_product(a, b):
    return frozenset((i, j) for j in b for i in a)

def val_func_astuple(a, b):
    return (a, b)

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_initset(value):
    return frozenset({value})

def val_func_greater(a, b):
    return a > b

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
    x1 = val_func_ofcolor(I, 4)
    x2 = val_func_first(x1)
    x3 = val_func_first(x2)
    x4 = val_func_last(x2)
    x5 = val_func_greater(x3, 3)
    x6 = val_func_greater(x3, 7)
    x7 = val_func_greater(x4, 3)
    x8 = val_func_greater(x4, 7)
    x9 = val_func_branch(x5, 4, 0)
    x10 = val_func_branch(x6, 8, x9)
    x11 = val_func_branch(x7, 4, 0)
    x12 = val_func_branch(x8, 8, x11)
    x13 = val_func_astuple(x10, x12)
    x14 = val_func_initset(0)
    x15 = val_func_insert(4, x14)
    x16 = val_func_insert(8, x15)
    x17 = val_func_product(x16, x16)
    x18 = val_func_crop(I, (0, 0), (3, 3))
    x19 = val_func_asindices(x18)
    x20 = val_func_recolor(0, x19)
    x21 = val_func_lbind(val_func_shift, x20)
    x22 = mval_func_apply(x21, x17)
    x23 = val_func_paint(I, x22)
    x24 = val_func_crop(I, x13, (3, 3))
    x25 = val_func_replace(x24, 5, 0)
    x26 = val_func_ofcolor(x25, 4)
    x27 = val_func_first(x26)
    x28 = val_func_asindices(x25)
    x29 = val_func_toobject(x28, x25)
    x30 = val_func_multiply(x27, 4)
    x31 = val_func_shift(x29, x30)
    O = val_func_paint(x23, x31)
    return [*map(list,O)]

def pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

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

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_partition(grid):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value) for value in val_func_palette(grid))

def reval_func_color(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def mpval_func_apply(function, a, b):
    return val_func_merge(pval_func_apply(function, a, b))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_size(container):
    return len(container)

def val_func_repeat(item, num):
    return tuple(item for i in range(num))

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_combine(a, b):
    return type(a)((*a, *b))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_partition(I)
    x2 = val_func_order(x1, val_func_size)
    x3 = val_func_apply(val_func_color, x2)
    x4 = val_func_last(x2)
    x5 = val_func_remove(x4, x2)
    x6 = val_func_repeat(x4, 1)
    x7 = val_func_combine(x6, x5)
    x8 = mpval_func_apply(reval_func_color, x3, x7)
    O = val_func_paint(I, x8)
    return [*map(list,O)]

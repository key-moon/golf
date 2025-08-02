def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

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

def val_func_connect(a, b):
    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_hline(patch):
    return val_func_width(patch) == len(patch) and val_func_height(patch) == 1

def val_func_vline(patch):
    return val_func_height(patch) == len(patch) and val_func_width(patch) == 1

def val_func_partition(grid):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value) for value in val_func_palette(grid))

def reval_func_color(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_ofval_func_color(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_power(function, n):
    if n == 1:
        return function
    return val_func_compose(function, val_func_power(function, n - 1))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_product(a, b):
    return frozenset((i, j) for j in b for i in a)

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_mfilter(container, function):
    return val_func_merge(val_func_sfilter(container, function))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_either(a, b):
    return a or b

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_size(container):
    return len(container)

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_equality(a, b):
    return a == b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_partition(I)
    x2 = val_func_mostval_func_color(I)
    x3 = val_func_ofval_func_color(I, x2)
    x4 = val_func_val_func_colorfilter(x1, 0)
    x5 = val_func_argmax(x1, val_func_size)
    x6 = val_func_difference(x1, x4)
    x7 = val_func_remove(x5, x6)
    x8 = val_func_merge(x7)
    x9 = val_func_product(x8, x8)
    x10 = val_func_power(val_func_first, 2)
    x11 = val_func_compose(val_func_first, val_func_last)
    x12 = val_func_fork(val_func_equality, x10, x11)
    x13 = val_func_sfilter(x9, x12)
    x14 = val_func_compose(val_func_last, val_func_first)
    x15 = val_func_power(val_func_last, 2)
    x16 = val_func_fork(val_func_connect, x14, x15)
    x17 = val_func_fork(reval_func_color, val_func_color, x16)
    x18 = val_func_apply(x17, x13)
    x19 = val_func_fork(val_func_either, val_func_vline, val_func_hline)
    x20 = val_func_mfilter(x18, x19)
    x21 = val_func_paint(I, x20)
    O = val_func_fill(x21, x2, x3)
    return [*map(list,O)]

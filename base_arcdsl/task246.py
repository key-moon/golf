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

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def val_func_underfill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = val_func_mostcolor(grid)
    g = list(list(r) for r in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_astuple(a, b):
    return (a, b)

def val_func_minimum(container):
    return min(container, default=0)

def val_func_maximum(container):
    return max(container, default=0)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_ofcolor(I, 2)
    x2 = val_func_ofcolor(I, 3)
    x3 = val_func_uppermost(x1)
    x4 = val_func_leftmost(x1)
    x5 = val_func_uppermost(x2)
    x6 = val_func_leftmost(x2)
    x7 = val_func_astuple(x3, x5)
    x8 = val_func_minimum(x7)
    x9 = val_func_maximum(x7)
    x10 = val_func_astuple(x8, x6)
    x11 = val_func_astuple(x9, x6)
    x12 = val_func_connect(x10, x11)
    x13 = val_func_astuple(x4, x6)
    x14 = val_func_minimum(x13)
    x15 = val_func_maximum(x13)
    x16 = val_func_astuple(x3, x14)
    x17 = val_func_astuple(x3, x15)
    x18 = val_func_connect(x16, x17)
    x19 = val_func_combine(x12, x18)
    O = val_func_underfill(I, 8, x19)
    return [*map(list,O)]

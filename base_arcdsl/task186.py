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

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_tojvec(j):
    return (0, j)

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_size(container):
    return len(container)

def val_func_equality(a, b):
    return a == b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_ofcolor(I, 1)
    x2 = val_func_size(x1)
    x3 = val_func_decrement(x2)
    x4 = val_func_canvas(0, (3, 3))
    x5 = val_func_tojvec(x3)
    x6 = val_func_connect((0, 0), x5)
    x7 = val_func_equality(x2, 4)
    x8 = val_func_insert((1, 1), x6)
    x9 = val_func_branch(x7, x8, x6)
    O = val_func_fill(x4, 2, x9)
    return [*map(list,O)]

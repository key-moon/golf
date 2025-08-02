def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_objects(grid, univalued, diagonal, without_bg):
    bg = val_func_mostcolor(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = val_func_asindices(grid)
    diagfun = val_func_neighbors if diagonal else val_func_dval_func_neighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_power(function, n):
    if n == 1:
        return function
    return val_func_compose(function, val_func_power(function, n - 1))

def val_func_lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_astuple(a, b):
    return (a, b)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_totuple(container):
    return tuple(container)

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_even(n):
    return n % 2 == 0

def val_func_subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, True, False, True)
    x2 = val_func_totuple(x1)
    x3 = val_func_compose(val_func_increment, val_func_ulcorner)
    x4 = val_func_compose(val_func_decrement, val_func_lrcorner)
    x5 = val_func_apply(x3, x2)
    x6 = val_func_apply(x4, x2)
    x7 = pval_func_apply(val_func_connect, x5, x6)
    x8 = val_func_apply(val_func_last, x5)
    x9 = val_func_compose(val_func_last, val_func_first)
    x10 = val_func_power(val_func_last, 2)
    x11 = val_func_fork(val_func_subtract, x9, x10)
    x12 = val_func_compose(val_func_even, x11)
    x13 = val_func_lbind(val_func_rbind, val_func_astuple)
    x14 = val_func_lbind(val_func_compose, x12)
    x15 = val_func_compose(x14, x13)
    x16 = val_func_fork(val_func_sfilter, val_func_first, x15)
    x17 = val_func_pair(x7, x8)
    x18 = mval_func_apply(x16, x17)
    O = val_func_fill(I, 0, x18)
    return [*map(list,O)]

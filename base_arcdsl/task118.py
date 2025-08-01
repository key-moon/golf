def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | ival_func_neighbors(loc)

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

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

def val_func_toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in val_func_toindices(patch) if 0 <= i < h and 0 <= j < w)

def val_func_hline(patch):
    return val_func_width(patch) == len(patch) and val_func_height(patch) == 1

def val_func_vline(patch):
    return val_func_height(patch) == len(patch) and val_func_width(patch) == 1

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

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_prval_func_apply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

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

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_mfilter(container, function):
    return val_func_merge(val_func_sfilter(container, function))

def val_func_tojvec(j):
    return (0, j)

def val_func_toivec(i):
    return (i, 0)

def val_func_either(a, b):
    return a or b

def val_func_both(a, b):
    return a and b

def val_func_initset(value):
    return frozenset({value})

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_valmax(container, compfunc):
    return compfunc(max(container, key=compfunc, default=0))

def val_func_size(container):
    return len(container)

def val_func_greater(a, b):
    return a > b

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_halve(n):
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)

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
    x1 = val_func_ofcolor(I, 2)
    x2 = val_func_prval_func_apply(val_func_connect, x1, x1)
    x3 = val_func_lbind(val_func_greater, 6)
    x4 = val_func_compose(x3, val_func_size)
    x5 = val_func_fork(val_func_either, val_func_vline, val_func_hline)
    x6 = val_func_fork(val_func_both, x4, x5)
    x7 = val_func_mfilter(x2, x6)
    x8 = val_func_fill(I, 2, x7)
    x9 = val_func_objects(x8, True, False, False)
    x10 = val_func_colorfilter(x9, 2)
    x11 = val_func_valmax(x10, val_func_width)
    x12 = val_func_halve(x11)
    x13 = val_func_toivec(x12)
    x14 = val_func_tojvec(x12)
    x15 = val_func_rbind(val_func_add, (0, 2))
    x16 = val_func_rbind(val_func_add, (2, 0))
    x17 = val_func_rbind(val_func_subtract, (0, 2))
    x18 = val_func_rbind(val_func_subtract, (2, 0))
    x19 = val_func_rbind(val_func_colorcount, 2)
    x20 = val_func_rbind(val_func_toobject, x8)
    x21 = val_func_compose(val_func_initset, x15)
    x22 = val_func_fork(val_func_insert, x16, x21)
    x23 = val_func_fork(val_func_insert, x17, x22)
    x24 = val_func_fork(val_func_insert, x18, x23)
    x25 = val_func_fork(val_func_combine, val_func_dval_func_neighbors, x24)
    x26 = val_func_chain(x19, x20, x25)
    x27 = val_func_rbind(val_func_argmax, x26)
    x28 = val_func_compose(x27, val_func_toindices)
    x29 = val_func_apply(x28, x10)
    x30 = val_func_rbind(val_func_add, x13)
    x31 = val_func_rbind(val_func_subtract, x13)
    x32 = val_func_rbind(val_func_add, x14)
    x33 = val_func_rbind(val_func_subtract, x14)
    x34 = val_func_fork(val_func_connect, x30, x31)
    x35 = val_func_fork(val_func_connect, x32, x33)
    x36 = val_func_fork(val_func_combine, x34, x35)
    x37 = mval_func_apply(x36, x29)
    x38 = val_func_fill(x8, 8, x37)
    O = val_func_fill(x38, 2, x1)
    return [*map(list,O)]

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

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

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

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

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

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

def val_func_shoot(start, direction):
    return val_func_connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

def val_func_inbox(patch):
    ai, aj = val_func_uppermost(patch) + 1, val_func_leftmost(patch) + 1
    bi, bj = val_func_lowermost(patch) - 1, val_func_rightmost(patch) - 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def val_func_cover(grid, patch):
    return val_func_fill(grid, val_func_mostcolor(grid), val_func_toindices(patch))

def underval_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = val_func_mostcolor(grid)
    g = list(list(r) for r in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def val_func_bordering(patch, grid):
    return val_func_uppermost(patch) == 0 or val_func_leftmost(patch) == 0 or val_func_lowermost(patch) == len(grid) - 1 or val_func_rightmost(patch) == len(grid[0]) - 1

def val_func_vmatching(a, b):
    return len(set(j for i, j in val_func_toindices(a)) & set(j for i, j in val_func_toindices(b))) > 0

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_mfilter(container, function):
    return val_func_merge(val_func_sfilter(container, function))

def val_func_argmin(container, compfunc):
    return min(container, key=compfunc)

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_valmax(container, compfunc):
    return compfunc(max(container, key=compfunc, default=0))

def val_func_size(container):
    return len(container)

def val_func_equality(a, b):
    return a == b

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
    x1 = val_func_objects(I, True, False, True)
    x2 = val_func_argmin(x1, val_func_size)
    x3 = val_func_argmax(x1, val_func_size)
    x4 = val_func_vmatching(x2, x3)
    x5 = val_func_branch(x4, (1, 0), (0, 1))
    x6 = val_func_branch(x4, val_func_uppermost, val_func_leftmost)
    x7 = val_func_valmax(x1, x6)
    x8 = x6(x2)
    x9 = val_func_equality(x7, x8)
    x10 = val_func_branch(x9, -1, 1)
    x11 = val_func_multiply(x5, x10)
    x12 = val_func_inbox(x2)
    x13 = val_func_rbind(val_func_shoot, x11)
    x14 = mval_func_apply(x13, x12)
    x15 = underval_func_fill(I, 8, x14)
    x16 = val_func_objects(x15, True, False, True)
    x17 = val_func_colorfilter(x16, 8)
    x18 = val_func_rbind(val_func_bordering, I)
    x19 = val_func_mfilter(x17, x18)
    O = val_func_cover(x15, x19)
    return [*map(list,O)]

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

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

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

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

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_objects(grid, univalued, diagonal, without_bg):
    bg = val_func_mostval_func_color(grid) if without_bg else None
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

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_ofval_func_color(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_sizefilter(container, n):
    return frozenset(item for item in container if len(item) == n)

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

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

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_other(container, value):
    return val_func_first(val_func_remove(value, container))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_intersection(a, b):
    return a & b

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_equality(a, b):
    return a == b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, True, False, False)
    x2 = val_func_sizefilter(x1, 1)
    x3 = val_func_apply(val_func_color, x2)
    x4 = val_func_difference(x1, x2)
    x5 = val_func_apply(val_func_color, x4)
    x6 = val_func_first(x5)
    x7 = val_func_last(x5)
    x8 = val_func_ofval_func_color(I, x6)
    x9 = val_func_ofval_func_color(I, x7)
    x10 = val_func_rbind(val_func_shoot, (1, 1))
    x11 = val_func_rbind(val_func_shoot, (-1, -1))
    x12 = val_func_rbind(val_func_shoot, (1, -1))
    x13 = val_func_rbind(val_func_shoot, (-1, 1))
    x14 = val_func_fork(val_func_combine, x10, x11)
    x15 = val_func_fork(val_func_combine, x12, x13)
    x16 = val_func_fork(val_func_combine, x14, x15)
    x17 = val_func_compose(x16, val_func_center)
    x18 = mval_func_apply(x17, x2)
    x19 = val_func_intersection(x8, x18)
    x20 = val_func_intersection(x9, x18)
    x21 = val_func_first(x2)
    x22 = val_func_color(x21)
    x23 = val_func_center(x21)
    x24 = val_func_neighbors(x23)
    x25 = val_func_toobject(x24, I)
    x26 = val_func_mostval_func_color(x25)
    x27 = val_func_other(x3, x22)
    x28 = val_func_equality(x26, x6)
    x29 = val_func_branch(x28, x22, x27)
    x30 = val_func_branch(x28, x27, x22)
    x31 = val_func_fill(I, x29, x19)
    O = val_func_fill(x31, x30, x20)
    return [*map(list,O)]

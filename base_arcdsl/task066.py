def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_first(container):
    return next(iter(container))

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

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

def val_func_vmatching(a, b):
    return len(set(j for i, j in val_func_toindices(a)) & set(j for i, j in val_func_toindices(b))) > 0

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_shoot(start, direction):
    return val_func_connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

def val_func_gravitate(source, destination):
    si, sj = val_func_center(source)
    di, dj = val_func_center(destination)
    i, j = 0, 0
    if val_func_vmatching(source, destination):
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    gi, gj = i, j
    c = 0
    while not val_func_adjacent(source, destination) and c < 42:
        c += 1
        gi += i
        gj += j
        source = val_func_shift(source, (i, j))
    return (gi - i, gj - j)

def val_func_cover(grid, patch):
    return val_func_fill(grid, val_func_mostcolor(grid), val_func_toindices(patch))

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

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

def val_func_replace(grid, val_func_replacee, val_func_replacer):
    return tuple(tuple(val_func_replacer if v == val_func_replacee else v for v in r) for r in grid)

def underval_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = val_func_mostcolor(grid)
    g = list(list(r) for r in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_adjacent(a, b):
    return val_func_manhattan(a, b) == 1

def val_func_manhattan(a, b):
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in val_func_toindices(a) for bi, bj in val_func_toindices(b))

def val_func_vline(patch):
    return val_func_height(patch) == len(patch) and val_func_width(patch) == 1

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

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

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

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

def val_func_astuple(a, b):
    return (a, b)

def val_func_other(container, value):
    return val_func_first(val_func_remove(value, container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1))

def val_func_both(a, b):
    return a and b

def val_func_initset(value):
    return frozenset({value})

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_greater(a, b):
    return a > b

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_combine(a, b):
    return type(a)((*a, *b))

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
    x2 = val_func_ofcolor(I, 3)
    x3 = val_func_vline(x1)
    x4 = val_func_vline(x2)
    x5 = val_func_center(x1)
    x6 = val_func_branch(x4, val_func_uppermost, val_func_rightmost)
    x7 = x6(x1)
    x8 = x6(x2)
    x9 = val_func_greater(x7, x8)
    x10 = val_func_both(x4, x9)
    x11 = val_func_branch(x10, val_func_lowermost, val_func_uppermost)
    x12 = x11(x2)
    x13 = val_func_branch(x4, val_func_leftmost, val_func_rightmost)
    x14 = x13(x2)
    x15 = val_func_astuple(x12, x14)
    x16 = val_func_other(x2, x15)
    x17 = val_func_subtract(x15, x16)
    x18 = val_func_shoot(x15, x17)
    x19 = underval_func_fill(I, 1, x18)
    x20 = val_func_objects(x19, True, False, False)
    x21 = val_func_colorfilter(x20, 1)
    x22 = val_func_rbind(val_func_adjacent, x2)
    x23 = val_func_sfilter(x21, x22)
    x24 = val_func_difference(x21, x23)
    x25 = val_func_merge(x24)
    x26 = val_func_cover(x19, x25)
    x27 = val_func_shoot(x5, (1, 0))
    x28 = val_func_shoot(x5, (-1, 0))
    x29 = val_func_shoot(x5, (0, -1))
    x30 = val_func_shoot(x5, (0, 1))
    x31 = val_func_combine(x27, x28)
    x32 = val_func_combine(x29, x30)
    x33 = val_func_branch(x3, x31, x32)
    x34 = val_func_ofcolor(x26, 1)
    x35 = val_func_initset(x15)
    x36 = val_func_rbind(val_func_manhattan, x35)
    x37 = val_func_compose(x36, val_func_initset)
    x38 = val_func_argmax(x34, x37)
    x39 = val_func_initset(x38)
    x40 = val_func_gravitate(x39, x33)
    x41 = val_func_crement(x40)
    x42 = val_func_add(x38, x41)
    x43 = val_func_connect(x38, x42)
    x44 = val_func_fill(x26, 1, x43)
    x45 = val_func_connect(x42, x5)
    x46 = underval_func_fill(x44, 1, x45)
    O = val_func_replace(x46, 1, 3)
    return [*map(list,O)]

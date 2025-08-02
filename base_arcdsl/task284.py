def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

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

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_cover(grid, patch):
    return val_func_fill(grid, val_func_mostval_func_color(grid), val_func_toindices(patch))

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

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in val_func_toindices(patch) if 0 <= i < h and 0 <= j < w)

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_centerofmass(patch):
    return tuple(map(lambda x: sum(x) // len(patch), zip(*val_func_toindices(patch))))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_llcorner(patch):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_portrait(piece):
    return val_func_height(piece) > val_func_width(piece)

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

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

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, True, False, True)
    x2 = val_func_merge(x1)
    x3 = val_func_portrait(x2)
    x4 = val_func_branch(x3, val_func_identity, val_func_dmirror)
    x5 = x4(I)
    x6 = val_func_objects(x5, True, False, True)
    x7 = val_func_order(x6, val_func_uppermost)
    x8 = val_func_first(x7)
    x9 = val_func_last(x7)
    x10 = val_func_color(x8)
    x11 = val_func_color(x9)
    x12 = val_func_compose(val_func_first, val_func_toindices)
    x13 = x12(x8)
    x14 = x12(x9)
    x15 = val_func_connect(x13, x14)
    x16 = val_func_centerofmass(x15)
    x17 = val_func_connect(x13, x16)
    x18 = val_func_fill(x5, x11, x15)
    x19 = val_func_fill(x18, x10, x17)
    x20 = val_func_add(x16, (1, 0))
    x21 = val_func_initset(x16)
    x22 = val_func_insert(x20, x21)
    x23 = val_func_toobject(x22, x19)
    x24 = val_func_astuple(0, -2)
    x25 = val_func_shift(x23, (0, 2))
    x26 = val_func_shift(x23, x24)
    x27 = val_func_combine(x25, x26)
    x28 = val_func_ulcorner(x27)
    x29 = val_func_urcorner(x27)
    x30 = val_func_connect(x28, x29)
    x31 = val_func_shift(x30, (-1, 0))
    x32 = val_func_llcorner(x27)
    x33 = val_func_lrcorner(x27)
    x34 = val_func_connect(x32, x33)
    x35 = val_func_shift(x34, (1, 0))
    x36 = val_func_paint(x19, x27)
    x37 = val_func_fill(x36, x10, x31)
    x38 = val_func_fill(x37, x11, x35)
    x39 = val_func_cover(x38, x22)
    O = x4(x39)
    return [*map(list,O)]

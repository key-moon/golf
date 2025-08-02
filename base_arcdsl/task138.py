def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_outbox(patch):
    ai, aj = val_func_uppermost(patch) - 1, val_func_leftmost(patch) - 1
    bi, bj = val_func_lowermost(patch) + 1, val_func_rightmost(patch) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    val_func_vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    val_func_hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(val_func_vlines | val_func_hlines)

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

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_bordering(patch, grid):
    return val_func_uppermost(patch) == 0 or val_func_leftmost(patch) == 0 or val_func_lowermost(patch) == len(grid) - 1 or val_func_rightmost(patch) == len(grid[0]) - 1

def val_func_hline(patch):
    return val_func_width(patch) == len(patch) and val_func_height(patch) == 1

def val_func_vline(patch):
    return val_func_height(patch) == len(patch) and val_func_width(patch) == 1

def val_func_fgpartition(grid):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in val_func_palette(grid) - {val_func_mostval_func_color(grid)}
    )

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

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_prapply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

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

def val_func_extract(container, condition):
    return next(e for e in container if condition(e))

def val_func_mfilter(container, function):
    return val_func_merge(val_func_sfilter(container, function))

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_size(container):
    return len(container)

def val_func_greater(a, b):
    return a > b

def val_func_flip(b):
    return not b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, True, False, False)
    x2 = val_func_val_func_colorfilter(x1, 0)
    x3 = val_func_rbind(val_func_bordering, I)
    x4 = val_func_compose(val_func_flip, x3)
    x5 = val_func_extract(x2, x4)
    x6 = val_func_outbox(x5)
    x7 = val_func_subgrid(x6, I)
    x8 = val_func_fgpartition(x7)
    x9 = val_func_argmax(x8, val_func_size)
    x10 = val_func_color(x9)
    x11 = val_func_toindices(x9)
    x12 = val_func_prapply(val_func_connect, x11, x11)
    x13 = val_func_mfilter(x12, val_func_vline)
    x14 = val_func_mfilter(x12, val_func_hline)
    x15 = val_func_size(x13)
    x16 = val_func_size(x14)
    x17 = val_func_greater(x15, x16)
    x18 = val_func_branch(x17, x13, x14)
    O = val_func_fill(x7, x10, x18)
    return [*map(list,O)]

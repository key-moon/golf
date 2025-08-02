def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

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

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_hfrontier(location):
    return frozenset((location[0], j) for j in range(30))

def val_func_vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

def val_func_trim(grid):
    return tuple(r[1:-1] for r in grid[1:-1])

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

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

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def val_func_power(function, n):
    if n == 1:
        return function
    return val_func_compose(function, val_func_power(function, n - 1))

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_other(container, value):
    return val_func_first(val_func_remove(value, container))

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_either(a, b):
    return a or b

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def val_func_intersection(a, b):
    return a & b

def val_func_combine(a, b):
    return type(a)((*a, *b))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_palette(I)
    x2 = val_func_objects(I, False, False, True)
    x3 = val_func_ofcolor(I, 0)
    x4 = val_func_first(x2)
    x5 = val_func_ulcorner(x4)
    x6 = val_func_subgrid(x4, I)
    x7 = val_func_power(val_func_trim, 2)
    x8 = x7(x6)
    x9 = val_func_asindices(x8)
    x10 = val_func_shift(x9, (2, 2))
    x11 = val_func_fill(x6, 0, x10)
    x12 = val_func_leastcolor(x11)
    x13 = val_func_remove(0, x1)
    x14 = val_func_other(x13, x12)
    x15 = val_func_ofcolor(x11, x12)
    x16 = val_func_shift(x15, x5)
    x17 = val_func_ofcolor(I, x12)
    x18 = val_func_uppermost(x17)
    x19 = val_func_lowermost(x17)
    x20 = val_func_matcher(val_func_first, x18)
    x21 = val_func_matcher(val_func_first, x19)
    x22 = val_func_fork(val_func_either, x20, x21)
    x23 = val_func_sfilter(x16, x22)
    x24 = val_func_difference(x16, x23)
    x25 = mval_func_apply(val_func_vfrontier, x23)
    x26 = mval_func_apply(val_func_hfrontier, x24)
    x27 = val_func_combine(x25, x26)
    x28 = val_func_intersection(x3, x27)
    x29 = val_func_fill(I, x14, x27)
    O = val_func_fill(x29, x12, x28)
    return [*map(list,O)]

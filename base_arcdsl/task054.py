def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_occurrences(grid, obj):
    occs = set()
    normed = val_func_normalize(obj)
    h, w = len(grid), len(grid[0])
    oh, ow = val_func_shape(obj)
    h2, w2 = h - oh + 1, w - ow + 1
    for i in range(h2):
        for j in range(w2):
            occurs = True
            for v, (a, b) in val_func_shift(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and grid[a][b] == v):
                    occurs = False
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)

def val_func_hfrontier(location):
    return frozenset((location[0], j) for j in range(30))

def val_func_vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

def val_func_cover(grid, patch):
    return val_func_fill(grid, val_func_mostcolor(grid), val_func_toindices(patch))

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

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

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

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

def val_func_normalize(patch):
    if len(patch) == 0:
        return patch
    return val_func_shift(patch, (-val_func_uppermost(patch), -val_func_leftmost(patch)))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_recolor(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

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
    

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

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

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_astuple(a, b):
    return (a, b)

def val_func_initset(value):
    return frozenset({value})

def val_func_argmin(container, compfunc):
    return min(container, key=compfunc)

def val_func_size(container):
    return len(container)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_equality(a, b):
    return a == b

def val_func_invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

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
    x1 = val_func_objects(I, False, False, True)
    x2 = val_func_argmin(x1, val_func_size)
    x3 = val_func_normalize(x2)
    x4 = val_func_height(x2)
    x5 = val_func_width(x2)
    x6 = val_func_equality(x4, 5)
    x7 = val_func_equality(x5, 5)
    x8 = val_func_astuple(x6, x7)
    x9 = val_func_add((1, 1), x8)
    x10 = val_func_invert(x9)
    x11 = val_func_center(x2)
    x12 = val_func_index(I, x11)
    x13 = val_func_branch(x6, (-1, 0), (0, 1))
    x14 = val_func_add(x13, x11)
    x15 = val_func_index(I, x14)
    x16 = val_func_astuple(x12, (0, 0))
    x17 = val_func_initset(x16)
    x18 = val_func_cover(I, x2)
    x19 = val_func_mostcolor(x18)
    x20 = val_func_ofcolor(x18, x19)
    x21 = val_func_occurrences(x18, x17)
    x22 = val_func_objects(x18, False, False, True)
    x23 = val_func_rbind(val_func_occurrences, x17)
    x24 = val_func_rbind(val_func_subgrid, x18)
    x25 = val_func_compose(x23, x24)
    x26 = val_func_lbind(mval_func_apply, val_func_vfrontier)
    x27 = val_func_lbind(mval_func_apply, val_func_hfrontier)
    x28 = val_func_compose(x26, x25)
    x29 = val_func_compose(x27, x25)
    x30 = val_func_branch(x6, x28, x29)
    x31 = val_func_branch(x7, x29, x28)
    x32 = val_func_fork(val_func_combine, x30, x31)
    x33 = val_func_lbind(val_func_recolor, x15)
    x34 = val_func_compose(x33, x32)
    x35 = val_func_fork(val_func_paint, x24, x34)
    x36 = val_func_compose(val_func_asobject, x35)
    x37 = val_func_fork(val_func_shift, x36, val_func_ulcorner)
    x38 = mval_func_apply(x37, x22)
    x39 = val_func_paint(x18, x38)
    x40 = val_func_shift(x3, x10)
    x41 = val_func_lbind(val_func_shift, x40)
    x42 = mval_func_apply(x41, x21)
    x43 = val_func_paint(x39, x42)
    O = val_func_fill(x43, x19, x20)
    return [*map(list,O)]

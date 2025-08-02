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
    

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_llcorner(patch):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

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

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_frontiers(grid):
    h, w = len(grid), len(grid[0])
    row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    column_indices = tuple(j for j, c in enumerate(val_func_dmirror(grid)) if len(set(c)) == 1)
    hval_func_frontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
    vval_func_frontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
    return hval_func_frontiers | vval_func_frontiers

def val_func_outbox(patch):
    ai, aj = val_func_uppermost(patch) - 1, val_func_leftmost(patch) - 1
    bi, bj = val_func_lowermost(patch) + 1, val_func_rightmost(patch) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def val_func_corners(patch):
    return frozenset({val_func_ulcorner(patch), val_func_urcorner(patch), val_func_llcorner(patch), val_func_lrcorner(patch)})

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

def val_func_downscale(grid, factor):
    h, w = len(grid), len(grid[0])
    g = tuple()
    for i in range(h):
        r = tuple()
        for j in range(w):
            if j % factor == 0:
                r = r + (grid[i][j],)
        g = g + (r, )
    h = len(g)
    dsg = tuple()
    for i in range(h):
        if i % factor == 0:
            dsg = dsg + (g[i],)
    return dsg

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

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

def val_func_numval_func_colors(element):
    return len(val_func_palette(element))

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

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

def reval_func_color(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

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

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_both(a, b):
    return a and b

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_size(container):
    return len(container)

def val_func_contained(value, container):
    return value in container

def val_func_flip(b):
    return not b

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_fgpartition(I)
    x2 = val_func_argmax(x1, val_func_size)
    x3 = val_func_remove(x2, x1)
    x4 = val_func_merge(x3)
    x5 = val_func_subgrid(x4, I)
    x6 = val_func_chain(val_func_color, val_func_merge, val_func_frontiers)
    x7 = x6(I)
    x8 = val_func_objects(x5, True, False, False)
    x9 = val_func_val_func_colorfilter(x8, 0)
    x10 = val_func_rbind(val_func_toobject, x5)
    x11 = val_func_chain(x10, val_func_corners, val_func_outbox)
    x12 = val_func_lbind(val_func_contained, x7)
    x13 = val_func_chain(x12, val_func_palette, x11)
    x14 = val_func_compose(val_func_numval_func_colors, x11)
    x15 = val_func_compose(val_func_flip, x13)
    x16 = val_func_matcher(x14, 1)
    x17 = val_func_fork(val_func_both, x15, x16)
    x18 = val_func_sfilter(x9, x17)
    x19 = val_func_compose(val_func_color, x11)
    x20 = val_func_fork(reval_func_color, x19, val_func_identity)
    x21 = mval_func_apply(x20, x18)
    x22 = val_func_paint(x5, x21)
    x23 = val_func_first(x9)
    x24 = val_func_height(x23)
    x25 = val_func_height(x5)
    x26 = val_func_increment(x24)
    x27 = val_func_interval(0, x25, x26)
    x28 = val_func_interval(0, x25, 1)
    x29 = val_func_rbind(val_func_contained, x27)
    x30 = val_func_chain(val_func_flip, x29, val_func_last)
    x31 = val_func_lbind(val_func_apply, val_func_first)
    x32 = val_func_rbind(val_func_sfilter, x30)
    x33 = val_func_rbind(val_func_pair, x28)
    x34 = val_func_chain(x31, x32, x33)
    x35 = val_func_compose(val_func_dmirror, x34)
    x36 = val_func_power(x35, 2)
    x37 = x36(x22)
    O = val_func_downscale(x37, x24)
    return [*map(list,O)]

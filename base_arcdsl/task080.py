def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

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

def val_func_outbox(patch):
    ai, aj = val_func_uppermost(patch) - 1, val_func_leftmost(patch) - 1
    bi, bj = val_func_lowermost(patch) + 1, val_func_rightmost(patch) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def val_func_toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in val_func_toindices(patch) if 0 <= i < h and 0 <= j < w)

def val_func_color(obj):
    return next(iter(obj))[0]

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

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

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

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_size(container):
    return len(container)

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

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
    x1 = val_func_fgpartition(I)
    x2 = val_func_objects(I, True, False, True)
    x3 = val_func_order(x1, val_func_height)
    x4 = val_func_last(x3)
    x5 = val_func_remove(x4, x3)
    x6 = val_func_last(x5)
    x7 = val_func_color(x6)
    x8 = val_func_val_func_colorfilter(x2, x7)
    x9 = val_func_power(val_func_outbox, 2)
    x10 = val_func_rbind(val_func_toobject, I)
    x11 = val_func_mostval_func_color(I)
    x12 = val_func_lbind(val_func_remove, x11)
    x13 = val_func_chain(val_func_size, x12, val_func_palette)
    x14 = val_func_chain(x13, x10, x9)
    x15 = val_func_argmax(x8, x14)
    x16 = val_func_ulcorner(x15)
    x17 = val_func_shape(x15)
    x18 = val_func_subtract(x16, x17)
    x19 = val_func_decrement(x18)
    x20 = val_func_multiply(x17, 3)
    x21 = val_func_add(x20, (2, 2))
    x22 = val_func_crop(I, x19, x21)
    x23 = val_func_asobject(x22)
    x24 = val_func_apply(val_func_ulcorner, x8)
    x25 = val_func_increment(x17)
    x26 = val_func_rbind(val_func_subtract, x25)
    x27 = val_func_apply(x26, x24)
    x28 = val_func_lbind(val_func_shift, x23)
    x29 = mval_func_apply(x28, x27)
    O = val_func_paint(I, x29)
    return [*map(list,O)]

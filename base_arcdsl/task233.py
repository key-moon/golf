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

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_switch(grid, a, b):
    return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_cmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*(r[::-1] for r in piece[::-1])))
    return val_func_vmirror(val_func_dmirror(val_func_vmirror(piece)))

def val_func_dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = val_func_ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def val_func_vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = val_func_ulcorner(piece)[1] + val_func_lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def val_func_hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = val_func_ulcorner(piece)[0] + val_func_lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

def val_func_numcolors(element):
    return len(val_func_palette(element))

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

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

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_rval_func_apply(functions, value):
    return type(functions)(function(value) for function in functions)

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

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_product(a, b):
    return frozenset((i, j) for j in b for i in a)

def val_func_astuple(a, b):
    return (a, b)

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_positive(x):
    return x > 0

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_size(container):
    return len(container)

def val_func_greater(a, b):
    return a > b

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_contained(value, container):
    return value in container

def val_func_equality(a, b):
    return a == b

def val_func_flip(b):
    return not b

def val_func_subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, False, True, True)
    x2 = val_func_argmax(x1, val_func_size)
    x3 = val_func_subgrid(x2, I)
    x4 = val_func_rbind(val_func_greater, 1)
    x5 = val_func_compose(x4, val_func_numcolors)
    x6 = val_func_sfilter(x1, x5)
    x7 = val_func_lbind(val_func_rbind, val_func_subtract)
    x8 = val_func_switch(x3, 2, 0)
    x9 = val_func_lbind(val_func_occurrences, x8)
    x10 = val_func_lbind(val_func_lbind, val_func_shift)
    x11 = val_func_compose(x7, val_func_ulcorner)
    x12 = val_func_matcher(val_func_first, 2)
    x13 = val_func_compose(val_func_flip, x12)
    x14 = val_func_rbind(val_func_sfilter, x12)
    x15 = val_func_rbind(val_func_sfilter, x13)
    x16 = val_func_lbind(val_func_recolor, 0)
    x17 = val_func_compose(x16, x15)
    x18 = val_func_fork(val_func_combine, x17, x14)
    x19 = val_func_chain(x11, x18, val_func_normalize)
    x20 = val_func_objects(x8, True, True, True)
    x21 = val_func_apply(val_func_toindices, x20)
    x22 = val_func_chain(x9, x18, val_func_normalize)
    x23 = val_func_rbind(val_func_colorcount, 2)
    x24 = val_func_lbind(val_func_sfilter, x21)
    x25 = val_func_chain(val_func_size, val_func_first, x24)
    x26 = val_func_compose(val_func_positive, val_func_size)
    x27 = val_func_lbind(val_func_lbind, val_func_contained)
    x28 = val_func_chain(x26, x24, x27)
    x29 = val_func_compose(x25, x27)
    x30 = val_func_rbind(val_func_sfilter, x28)
    x31 = val_func_compose(x30, x22)
    x32 = val_func_lbind(val_func_rbind, val_func_equality)
    x33 = val_func_rbind(val_func_compose, x29)
    x34 = val_func_chain(x33, x32, x23)
    x35 = val_func_fork(val_func_sfilter, x31, x34)
    x36 = val_func_fork(val_func_apply, x19, x35)
    x37 = val_func_compose(x10, val_func_normalize)
    x38 = val_func_fork(mval_func_apply, x37, x36)
    x39 = val_func_astuple(val_func_cmirror, val_func_dmirror)
    x40 = val_func_astuple(val_func_hmirror, val_func_vmirror)
    x41 = val_func_combine(x39, x40)
    x42 = val_func_product(x41, x41)
    x43 = val_func_fork(val_func_compose, val_func_first, val_func_last)
    x44 = val_func_apply(x43, x42)
    x45 = val_func_lbind(val_func_rval_func_apply, x44)
    x46 = mval_func_apply(x45, x6)
    x47 = mval_func_apply(x38, x46)
    x48 = val_func_paint(x3, x47)
    x49 = val_func_palette(x47)
    x50 = val_func_lbind(val_func_remove, 2)
    x51 = x50(x49)
    x52 = val_func_chain(val_func_first, x50, val_func_palette)
    x53 = val_func_rbind(val_func_contained, x51)
    x54 = val_func_chain(val_func_flip, x53, x52)
    x55 = val_func_sfilter(x6, x54)
    x56 = val_func_fork(val_func_apply, x19, x22)
    x57 = val_func_fork(mval_func_apply, x37, x56)
    x58 = mval_func_apply(x45, x55)
    x59 = mval_func_apply(x57, x58)
    O = val_func_paint(x48, x59)
    return [*map(list,O)]

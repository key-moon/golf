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

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

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

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

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

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

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

def val_func_astuple(a, b):
    return (a, b)

def val_func_other(container, value):
    return val_func_first(val_func_remove(value, container))

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_initset(value):
    return frozenset({value})

def val_func_argmin(container, compfunc):
    return min(container, key=compfunc)

def val_func_size(container):
    return len(container)

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_intersection(a, b):
    return a & b

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

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, False, False, True)
    x2 = val_func_rbind(val_func_other, 5)
    x3 = val_func_compose(x2, val_func_palette)
    x4 = val_func_fork(val_func_recolor, x3, val_func_identity)
    x5 = val_func_apply(x4, x1)
    x6 = val_func_order(x5, val_func_leftmost)
    x7 = val_func_compose(val_func_last, val_func_last)
    x8 = val_func_lbind(val_func_matcher, x7)
    x9 = val_func_compose(x8, val_func_leftmost)
    x10 = val_func_compose(x8, val_func_rightmost)
    x11 = val_func_fork(val_func_sfilter, val_func_identity, x9)
    x12 = val_func_fork(val_func_sfilter, val_func_identity, x10)
    x13 = val_func_compose(val_func_dval_func_neighbors, val_func_last)
    x14 = val_func_rbind(val_func_chain, x13)
    x15 = val_func_lbind(x14, val_func_size)
    x16 = val_func_lbind(val_func_rbind, val_func_intersection)
    x17 = val_func_chain(x15, x16, val_func_toindices)
    x18 = val_func_fork(val_func_argmin, x11, x17)
    x19 = val_func_fork(val_func_argmin, x12, x17)
    x20 = val_func_compose(val_func_last, x18)
    x21 = val_func_compose(val_func_last, x19)
    x22 = val_func_astuple(0, (1, -1))
    x23 = val_func_initset(x22)
    x24 = val_func_lbind(val_func_add, (0, 1))
    x25 = val_func_chain(x20, val_func_first, val_func_last)
    x26 = val_func_compose(x21, val_func_first)
    x27 = val_func_fork(val_func_subtract, x26, x25)
    x28 = val_func_compose(val_func_first, val_func_last)
    x29 = val_func_compose(x24, x27)
    x30 = val_func_fork(val_func_shift, x28, x29)
    x31 = val_func_fork(val_func_combine, val_func_first, x30)
    x32 = val_func_fork(val_func_remove, x28, val_func_last)
    x33 = val_func_fork(val_func_astuple, x31, x32)
    x34 = val_func_size(x1)
    x35 = val_func_power(x33, x34)
    x36 = val_func_astuple(x23, x6)
    x37 = x35(x36)
    x38 = val_func_first(x37)
    x39 = val_func_width(x38)
    x40 = val_func_decrement(x39)
    x41 = val_func_astuple(3, x40)
    x42 = val_func_canvas(0, x41)
    O = val_func_paint(x42, x38)
    return [*map(list,O)]

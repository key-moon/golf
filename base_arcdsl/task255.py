def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

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

def val_func_normalize(patch):
    if len(patch) == 0:
        return patch
    return val_func_shift(patch, (-val_func_uppermost(patch), -val_func_leftmost(patch)))

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

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def val_func_toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in val_func_toindices(patch) if 0 <= i < h and 0 <= j < w)

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_bordering(patch, grid):
    return val_func_uppermost(patch) == 0 or val_func_leftmost(patch) == 0 or val_func_lowermost(patch) == len(grid) - 1 or val_func_rightmost(patch) == len(grid[0]) - 1

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

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

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_first(container):
    return next(iter(container))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_positive(x):
    return x > 0

def val_func_both(a, b):
    return a and b

def val_func_initset(value):
    return frozenset({value})

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_size(container):
    return len(container)

def val_func_contained(value, container):
    return value in container

def val_func_multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_asindices(I)
    x2 = val_func_fork(val_func_product, val_func_identity, val_func_identity)
    x3 = val_func_lbind(val_func_canvas, 0)
    x4 = val_func_compose(val_func_asobject, x3)
    x5 = val_func_fork(val_func_multiply, val_func_first, val_func_last)
    x6 = val_func_compose(val_func_positive, val_func_size)
    x7 = val_func_lbind(val_func_lbind, val_func_shift)
    x8 = val_func_rbind(val_func_fork, x5)
    x9 = val_func_lbind(x8, val_func_multiply)
    x10 = val_func_lbind(val_func_chain, x6)
    x11 = val_func_rbind(x10, x4)
    x12 = val_func_lbind(val_func_lbind, val_func_occurrences)
    x13 = val_func_chain(x9, x11, x12)
    x14 = val_func_compose(x2, val_func_first)
    x15 = val_func_compose(x13, val_func_last)
    x16 = val_func_fork(val_func_argmax, x14, x15)
    x17 = val_func_chain(x7, x4, x16)
    x18 = val_func_compose(x4, x16)
    x19 = val_func_fork(val_func_occurrences, val_func_last, x18)
    x20 = val_func_fork(mval_func_apply, x17, x19)
    x21 = val_func_multiply(2, 6)
    x22 = val_func_interval(3, x21, 1)
    x23 = val_func_astuple(x22, I)
    x24 = x20(x23)
    x25 = val_func_fill(I, 3, x24)
    x26 = val_func_interval(3, 10, 1)
    x27 = val_func_astuple(x26, x25)
    x28 = x20(x27)
    x29 = val_func_fill(x25, 3, x28)
    x30 = val_func_astuple(x26, x29)
    x31 = x20(x30)
    x32 = val_func_fill(x29, 3, x31)
    x33 = val_func_rbind(val_func_toobject, x32)
    x34 = val_func_rbind(val_func_colorcount, 3)
    x35 = val_func_chain(x34, x33, val_func_neighbors)
    x36 = val_func_matcher(x35, 8)
    x37 = val_func_sfilter(x1, x36)
    x38 = val_func_fill(I, 3, x37)
    x39 = val_func_ofcolor(x38, 0)
    x40 = val_func_rbind(val_func_bordering, x38)
    x41 = val_func_compose(x40, val_func_initset)
    x42 = val_func_lbind(val_func_contained, 3)
    x43 = val_func_rbind(val_func_toobject, x38)
    x44 = val_func_chain(x42, val_func_palette, x43)
    x45 = val_func_compose(x44, val_func_dval_func_neighbors)
    x46 = val_func_fork(val_func_both, x45, x41)
    x47 = val_func_sfilter(x39, x46)
    O = val_func_fill(x38, 3, x47)
    return [*map(list,O)]

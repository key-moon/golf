def val_func_pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

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

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

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

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_centerofmass(patch):
    return tuple(map(lambda x: sum(x) // len(patch), zip(*val_func_toindices(patch))))

def val_func_manhattan(a, b):
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in val_func_toindices(a) for bi, bj in val_func_toindices(b))

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

def val_func_val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_prval_func_apply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

def val_func_mval_func_pval_func_apply(function, a, b):
    return val_func_merge(val_func_pval_func_apply(function, a, b))

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

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_astuple(a, b):
    return (a, b)

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_positive(x):
    return x > 0

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def val_func_initset(value):
    return frozenset({value})

def val_func_argmin(container, compfunc):
    return min(container, key=compfunc)

def val_func_valmax(container, compfunc):
    return compfunc(max(container, key=compfunc, default=0))

def val_func_minimum(container):
    return min(container, default=0)

def val_func_size(container):
    return len(container)

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_contained(value, container):
    return value in container

def val_func_double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

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

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_mostval_func_color(I)
    x2 = val_func_fgpartition(I)
    x3 = val_func_objects(I, True, False, True)
    x4 = val_func_rbind(val_func_valmax, val_func_width)
    x5 = val_func_lbind(val_func_val_func_colorfilter, x3)
    x6 = val_func_compose(x5, val_func_color)
    x7 = val_func_compose(val_func_double, x4)
    x8 = val_func_lbind(val_func_prval_func_apply, val_func_manhattan)
    x9 = val_func_fork(x8, val_func_identity, val_func_identity)
    x10 = val_func_lbind(val_func_remove, 0)
    x11 = val_func_compose(x10, x9)
    x12 = val_func_rbind(val_func_branch, -2)
    x13 = val_func_fork(x12, val_func_positive, val_func_decrement)
    x14 = val_func_chain(x13, val_func_minimum, x11)
    x15 = val_func_fork(val_func_add, x14, x7)
    x16 = val_func_compose(x15, x6)
    x17 = val_func_compose(val_func_invert, x16)
    x18 = val_func_order(x2, x17)
    x19 = val_func_rbind(val_func_argmin, val_func_centerofmass)
    x20 = val_func_compose(val_func_initset, val_func_vmirror)
    x21 = val_func_fork(val_func_insert, val_func_dmirror, x20)
    x22 = val_func_fork(val_func_insert, val_func_cmirror, x21)
    x23 = val_func_fork(val_func_insert, val_func_hmirror, x22)
    x24 = val_func_compose(x19, x23)
    x25 = val_func_apply(x24, x18)
    x26 = val_func_size(x2)
    x27 = val_func_apply(val_func_size, x2)
    x28 = val_func_contained(1, x27)
    x29 = val_func_increment(x26)
    x30 = val_func_branch(x28, x26, x29)
    x31 = val_func_double(x30)
    x32 = val_func_decrement(x31)
    x33 = val_func_apply(val_func_normalize, x25)
    x34 = val_func_interval(0, x30, 1)
    x35 = val_func_pair(x34, x34)
    x36 = val_func_mval_func_pval_func_apply(val_func_shift, x33, x35)
    x37 = val_func_astuple(x32, x32)
    x38 = val_func_canvas(x1, x37)
    x39 = val_func_paint(x38, x36)
    x40 = val_func_rot90(x39)
    x41 = val_func_paint(x40, x36)
    x42 = val_func_rot90(x41)
    x43 = val_func_paint(x42, x36)
    x44 = val_func_rot90(x43)
    O = val_func_paint(x44, x36)
    return [*map(list,O)]

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

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

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_color(obj):
    return next(iter(obj))[0]

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

def val_func_reval_func_color(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

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

def val_func_sign(x):
    if isinstance(x, int):
        return 0 if x == 0 else (1 if x > 0 else -1)
    return (0 if x[0] == 0 else (1 if x[0] > 0 else -1),        0 if x[1] == 0 else (1 if x[1] > 0 else -1))

def val_func_argmin(container, compfunc):
    return min(container, key=compfunc)

def val_func_valmin(container, compfunc):
    return compfunc(min(container, key=compfunc, default=0))

def val_func_maximum(container):
    return max(container, default=0)

def val_func_greater(a, b):
    return a > b

def val_func_intersection(a, b):
    return a & b

def val_func_equality(a, b):
    return a == b

def val_func_even(n):
    return n % 2 == 0

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

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_asindices(I)
    x2 = val_func_objects(I, True, False, True)
    x3 = val_func_fork(val_func_multiply, val_func_sign, val_func_identity)
    x4 = val_func_lbind(val_func_apply, x3)
    x5 = val_func_chain(val_func_even, val_func_maximum, x4)
    x6 = val_func_lbind(val_func_sfilter, x1)
    x7 = val_func_fork(val_func_add, val_func_first, val_func_last)
    x8 = val_func_rbind(val_func_remove, x2)
    x9 = val_func_compose(val_func_center, val_func_last)
    x10 = val_func_fork(val_func_subtract, val_func_first, x9)
    x11 = val_func_compose(x5, x10)
    x12 = val_func_lbind(val_func_rbind, val_func_equality)
    x13 = val_func_lbind(val_func_argmin, x2)
    x14 = val_func_chain(x7, x4, x10)
    x15 = val_func_lbind(val_func_lbind, val_func_astuple)
    x16 = val_func_lbind(val_func_rbind, val_func_astuple)
    x17 = val_func_lbind(val_func_compose, x11)
    x18 = val_func_lbind(val_func_compose, x14)
    x19 = val_func_compose(x18, x15)
    x20 = val_func_compose(x18, x16)
    x21 = val_func_compose(x13, x19)
    x22 = val_func_rbind(val_func_compose, x21)
    x23 = val_func_lbind(val_func_lbind, val_func_valmin)
    x24 = val_func_rbind(val_func_compose, x19)
    x25 = val_func_chain(x24, x23, x8)
    x26 = val_func_lbind(val_func_fork, val_func_greater)
    x27 = val_func_fork(x26, x25, x20)
    x28 = val_func_chain(x6, x17, x16)
    x29 = val_func_chain(x6, x22, x12)
    x30 = val_func_fork(val_func_intersection, x28, x29)
    x31 = val_func_compose(x6, x27)
    x32 = val_func_fork(val_func_intersection, x30, x31)
    x33 = val_func_fork(val_func_reval_func_color, val_func_color, x32)
    x34 = mval_func_apply(x33, x2)
    O = val_func_paint(I, x34)
    return [*map(list,O)]

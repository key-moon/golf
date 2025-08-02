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
    

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_hsplit(grid, n):
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(val_func_crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))

def val_func_hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

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

def val_func_colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

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

def val_func_astuple(a, b):
    return (a, b)

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_first(container):
    return next(iter(container))

def val_func_tojvec(j):
    return (0, j)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_colorcount(I, 0)
    x2 = val_func_subtract(9, x1)
    x3 = val_func_multiply(x1, 3)
    x4 = val_func_multiply(x3, x1)
    x5 = val_func_subtract(x4, 3)
    x6 = val_func_astuple(3, x5)
    x7 = val_func_canvas(0, x6)
    x8 = val_func_hconcat(I, x7)
    x9 = val_func_objects(x8, True, True, True)
    x10 = val_func_first(x9)
    x11 = val_func_lbind(val_func_shift, x10)
    x12 = val_func_compose(x11, val_func_tojvec)
    x13 = val_func_interval(0, x2, 1)
    x14 = val_func_rbind(val_func_multiply, 3)
    x15 = val_func_apply(x14, x13)
    x16 = mval_func_apply(x12, x15)
    x17 = val_func_paint(x8, x16)
    x18 = val_func_hsplit(x17, x1)
    O = val_func_merge(x18)
    return [*map(list,O)]

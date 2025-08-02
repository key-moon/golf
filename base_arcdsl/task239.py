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

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_vconcat(a, b):
    return a + b

def val_func_cmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*(r[::-1] for r in piece[::-1])))
    return val_func_vmirror(val_func_dmirror(val_func_vmirror(piece)))

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

def val_func_valmax(container, compfunc):
    return compfunc(max(container, key=compfunc, default=0))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_size(container):
    return len(container)

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

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
    x1 = val_func_objects(I, True, False, False)
    x2 = val_func_order(x1, val_func_size)
    x3 = val_func_valmax(x1, val_func_size)
    x4 = val_func_rbind(val_func_astuple, 1)
    x5 = val_func_lbind(val_func_subtract, x3)
    x6 = val_func_compose(x4, val_func_size)
    x7 = val_func_chain(x4, x5, val_func_size)
    x8 = val_func_fork(val_func_canvas, val_func_color, x6)
    x9 = val_func_lbind(val_func_canvas, 0)
    x10 = val_func_compose(x9, x7)
    x11 = val_func_fork(val_func_vconcat, x8, x10)
    x12 = val_func_compose(val_func_cmirror, x11)
    x13 = val_func_apply(x12, x2)
    x14 = val_func_merge(x13)
    O = val_func_cmirror(x14)
    return [*map(list,O)]

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def val_func_vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

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

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_fgpartition(grid):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in val_func_palette(grid) - {val_func_mostval_func_color(grid)}
    )

def reval_func_color(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_portrait(piece):
    return val_func_height(piece) > val_func_width(piece)

def val_func_width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return val_func_rightmost(piece) - val_func_leftmost(piece) + 1

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

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_interval(start, stop, step):
    return tuple(range(start, stop, step))

def val_func_tojvec(j):
    return (0, j)

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_portrait(I)
    x2 = val_func_branch(x1, val_func_dmirror, val_func_identity)
    x3 = x2(I)
    x4 = val_func_fgpartition(x3)
    x5 = val_func_merge(x4)
    x6 = val_func_chain(val_func_double, val_func_decrement, val_func_width)
    x7 = x6(x5)
    x8 = val_func_compose(val_func_vfrontier, val_func_tojvec)
    x9 = val_func_lbind(mval_func_apply, x8)
    x10 = val_func_rbind(val_func_interval, x7)
    x11 = val_func_width(x3)
    x12 = val_func_rbind(x10, x11)
    x13 = val_func_chain(x9, x12, val_func_leftmost)
    x14 = val_func_fork(reval_func_color, val_func_color, x13)
    x15 = mval_func_apply(x14, x4)
    x16 = val_func_paint(x3, x15)
    O = x2(x16)
    return [*map(list,O)]

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_mostval_func_color(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_lefthalf(grid):
    return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))

def val_func_tophalf(grid):
    return grid[:len(grid) // 2]

def val_func_cover(grid, patch):
    return val_func_fill(grid, val_func_mostval_func_color(grid), val_func_toindices(patch))

def val_func_connect(a, b):
    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = val_func_ulcorner(piece)[1] + val_func_lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_color(obj):
    return next(iter(obj))[0]

def val_func_numval_func_colors(element):
    return len(val_func_palette(element))

def val_func_partition(grid):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value) for value in val_func_palette(grid))

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

def val_func_reval_func_color(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_lrcorner(patch):
    return tuple(map(max, zip(*val_func_toindices(patch))))

def val_func_llcorner(patch):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*val_func_toindices(patch)))))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_sizefilter(container, n):
    return frozenset(item for item in container if len(item) == n)

def val_func_pval_func_apply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

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

def val_func_pair(a, b):
    return tuple(zip(a, b))

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_last(container):
    return max(enumerate(container))[1]

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_tojvec(j):
    return (0, j)

def val_func_initset(value):
    return frozenset({value})

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_maximum(container):
    return max(container, default=0)

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_even(n):
    return n % 2 == 0

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
    x1 = val_func_rot90(I)
    x2 = val_func_rot180(I)
    x3 = val_func_rot270(I)
    x4 = val_func_initset(I)
    x5 = val_func_chain(val_func_numval_func_colors, val_func_lefthalf, val_func_tophalf)
    x6 = val_func_insert(x1, x4)
    x7 = val_func_insert(x2, x6)
    x8 = val_func_insert(x3, x7)
    x9 = val_func_argmax(x8, x5)
    x10 = val_func_vmirror(x9)
    x11 = val_func_pval_func_apply(val_func_pair, x9, x10)
    x12 = val_func_lbind(val_func_apply, val_func_maximum)
    x13 = val_func_apply(x12, x11)
    x14 = val_func_partition(x13)
    x15 = val_func_sizefilter(x14, 4)
    x16 = val_func_apply(val_func_llcorner, x15)
    x17 = val_func_apply(val_func_lrcorner, x15)
    x18 = val_func_combine(x16, x17)
    x19 = val_func_cover(x13, x18)
    x20 = val_func_tojvec(-2)
    x21 = val_func_rbind(val_func_add, (0, 2))
    x22 = val_func_rbind(val_func_add, x20)
    x23 = val_func_compose(x21, val_func_ulcorner)
    x24 = val_func_compose(x22, val_func_urcorner)
    x25 = val_func_fork(val_func_connect, x23, x24)
    x26 = val_func_compose(val_func_even, val_func_last)
    x27 = val_func_rbind(val_func_sfilter, x26)
    x28 = val_func_chain(val_func_normalize, x27, x25)
    x29 = val_func_fork(val_func_shift, x28, x23)
    x30 = val_func_fork(val_func_reval_func_color, val_func_color, x29)
    x31 = mval_func_apply(x30, x15)
    x32 = val_func_paint(x19, x31)
    x33 = val_func_rot90(x32)
    x34 = val_func_rot180(x32)
    x35 = val_func_rot270(x32)
    x36 = val_func_pval_func_apply(val_func_pair, x32, x33)
    x37 = val_func_apply(x12, x36)
    x38 = val_func_pval_func_apply(val_func_pair, x37, x34)
    x39 = val_func_apply(x12, x38)
    x40 = val_func_pval_func_apply(val_func_pair, x39, x35)
    O = val_func_apply(x12, x40)
    return [*map(list,O)]

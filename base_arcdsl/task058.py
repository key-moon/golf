def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

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

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def val_func_vconcat(a, b):
    return a + b

def val_func_hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def val_func_upscale(element, factor):
    if isinstance(element, tuple):
        g = tuple()
        for row in element:
            val_func_upscaled_row = tuple()
            for value in row:
                val_func_upscaled_row = val_func_upscaled_row + tuple(value for num in range(factor))
            g = g + tuple(val_func_upscaled_row for num in range(factor))
        return g
    else:
        if len(element) == 0:
            return frozenset()
        di_inv, dj_inv = val_func_ulcorner(element)
        di, dj = (-di_inv, -dj_inv)
        normed_obj = val_func_shift(element, (di, dj))
        o = set()
        for value, (i, j) in normed_obj:
            for io in range(factor):
                for jo in range(factor):
                    o.add((value, (i * factor + io, j * factor + jo)))
        return val_func_shift(frozenset(o), (di_inv, dj_inv))

def val_func_vval_func_upscale(grid, factor):
    g = tuple()
    for row in grid:
        g = g + tuple(row for num in range(factor))
    return g

def val_func_hval_func_upscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

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

def val_func_chain(h, g, f,):
    return lambda x: h(g(f(x)))

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_astuple(a, b):
    return (a, b)

def val_func_insert(value, container):
    return container.union(frozenset({value}))

def val_func_decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def val_func_initset(value):
    return frozenset({value})

def val_func_even(n):
    return n % 2 == 0

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
    x1 = val_func_width(I)
    x2 = val_func_astuple(1, 2)
    x3 = val_func_astuple(2, 2)
    x4 = val_func_astuple(2, 1)
    x5 = val_func_astuple(3, 1)
    x6 = val_func_canvas(3, (1, 1))
    x7 = val_func_upscale(x6, 4)
    x8 = val_func_initset((1, 0))
    x9 = val_func_insert((1, 1), x8)
    x10 = val_func_insert(x2, x9)
    x11 = val_func_insert(x3, x10)
    x12 = val_func_fill(x7, 0, x11)
    x13 = val_func_vval_func_upscale(x6, 5)
    x14 = val_func_hval_func_upscale(x13, 3)
    x15 = val_func_insert(x4, x9)
    x16 = val_func_insert(x5, x15)
    x17 = val_func_fill(x14, 0, x16)
    x18 = val_func_even(x1)
    x19 = val_func_branch(x18, x12, x17)
    x20 = val_func_canvas(0, (1, 1))
    x21 = val_func_lbind(val_func_hval_func_upscale, x20)
    x22 = val_func_chain(x21, val_func_decrement, val_func_height)
    x23 = val_func_rbind(val_func_hconcat, x6)
    x24 = val_func_compose(x23, x22)
    x25 = val_func_lbind(val_func_hval_func_upscale, x6)
    x26 = val_func_compose(x25, val_func_height)
    x27 = val_func_fork(val_func_vconcat, x24, val_func_rot90)
    x28 = val_func_fork(val_func_vconcat, x26, x27)
    x29 = val_func_subtract(x1, 4)
    x30 = val_func_power(x28, x29)
    O = x30(x19)
    return [*map(list,O)]

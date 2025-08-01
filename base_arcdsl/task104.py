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

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

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

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

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

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_astuple(a, b):
    return (a, b)

def val_func_first(container):
    return next(iter(container))

def val_func_initset(value):
    return frozenset({value})

def val_func_combine(a, b):
    return type(a)((*a, *b))

def val_func_contained(value, container):
    return value in container

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, False, False, True)
    x2 = val_func_first(x1)
    x3 = val_func_toindices(x2)
    x4 = val_func_contained((0, 2), x3)
    x5 = val_func_contained((2, 2), x3)
    x6 = val_func_contained((2, 0), x3)
    x7 = val_func_astuple(9, 9)
    x8 = val_func_canvas(0, x7)
    x9 = val_func_astuple(3, (0, 0))
    x10 = val_func_initset(x9)
    x11 = val_func_upscale(x10, 2)
    x12 = val_func_upscale(x11, 2)
    x13 = val_func_shape(x12)
    x14 = val_func_shift(x12, x13)
    x15 = val_func_combine(x12, x14)
    x16 = val_func_paint(x8, x15)
    x17 = val_func_rot90(x16)
    x18 = val_func_rot180(x16)
    x19 = val_func_rot270(x16)
    x20 = val_func_branch(x4, x17, x16)
    x21 = val_func_branch(x5, x18, x20)
    O = val_func_branch(x6, x19, x21)
    return [*map(list,O)]

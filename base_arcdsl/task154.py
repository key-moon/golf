def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

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

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_shape(piece):
    return (val_func_height(piece), val_func_width(piece))

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

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

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_cover(grid, patch):
    return val_func_fill(grid, val_func_mostcolor(grid), val_func_toindices(patch))

def val_func_center(patch):
    return (val_func_uppermost(patch) + val_func_height(patch) // 2, val_func_leftmost(patch) + val_func_width(patch) // 2)

def val_func_subgrid(patch, grid):
    return val_func_crop(grid, val_func_ulcorner(patch), val_func_shape(patch))

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = val_func_ulcorner(piece)[0] + val_func_lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_fgpartition(grid):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in val_func_palette(grid) - {val_func_mostcolor(grid)}
    )

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

def val_func_recolor(value, patch):
    return frozenset((value, val_func_index) for val_func_index in val_func_toindices(patch))

def val_func_ulcorner(patch):
    return tuple(map(min, zip(*val_func_toindices(patch))))

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def val_func_portrait(piece):
    return val_func_height(piece) > val_func_width(piece)

def val_func_height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return val_func_lowermost(piece) - val_func_uppermost(piece) + 1

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_branch(condition, a, b):
    return a if condition else b

def val_func_first(container):
    return next(iter(container))

def val_func_extract(container, condition):
    return next(e for e in container if condition(e))

def val_func_toivec(i):
    return (i, 0)

def val_func_valmin(container, compfunc):
    return compfunc(min(container, key=compfunc, default=0))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_flip(b):
    return not b

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

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_fgpartition(I)
    x2 = val_func_rot90(I)
    x3 = val_func_colorfilter(x1, 2)
    x4 = val_func_first(x3)
    x5 = val_func_portrait(x4)
    x6 = val_func_branch(x5, I, x2)
    x7 = val_func_objects(x6, True, False, True)
    x8 = val_func_colorfilter(x7, 5)
    x9 = val_func_apply(val_func_center, x8)
    x10 = val_func_valmin(x9, val_func_first)
    x11 = val_func_compose(val_func_first, val_func_center)
    x12 = val_func_matcher(x11, x10)
    x13 = val_func_compose(val_func_flip, x12)
    x14 = val_func_extract(x8, x12)
    x15 = val_func_extract(x8, x13)
    x16 = val_func_ulcorner(x14)
    x17 = val_func_ulcorner(x15)
    x18 = val_func_subgrid(x14, x6)
    x19 = val_func_subgrid(x15, x6)
    x20 = val_func_hmirror(x18)
    x21 = val_func_hmirror(x19)
    x22 = val_func_ofcolor(x20, 5)
    x23 = val_func_recolor(5, x22)
    x24 = val_func_ofcolor(x21, 5)
    x25 = val_func_recolor(5, x24)
    x26 = val_func_height(x23)
    x27 = val_func_height(x25)
    x28 = val_func_add(3, x26)
    x29 = val_func_add(3, x27)
    x30 = val_func_toivec(x28)
    x31 = val_func_toivec(x29)
    x32 = val_func_add(x16, x30)
    x33 = val_func_subtract(x17, x31)
    x34 = val_func_shift(x23, x32)
    x35 = val_func_shift(x25, x33)
    x36 = val_func_merge(x8)
    x37 = val_func_cover(x6, x36)
    x38 = val_func_paint(x37, x34)
    x39 = val_func_paint(x38, x35)
    x40 = val_func_rot270(x39)
    O = val_func_branch(x5, x39, x40)
    return [*map(list,O)]

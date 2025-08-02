def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

def val_func_shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def val_func_ival_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def val_func_neighbors(loc):
    return val_func_dval_func_neighbors(loc) | val_func_ival_func_neighbors(loc)

def val_func_dval_func_neighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def val_func_mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def val_func_paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_val_func_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_painted[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_painted)

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

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

def val_func_normalize(patch):
    if len(patch) == 0:
        return patch
    return val_func_shift(patch, (-val_func_uppermost(patch), -val_func_leftmost(patch)))

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def val_func_asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def val_func_matcher(function, target):
    return lambda x: function(x) == target

def val_func_compose(outer, inner):
    return lambda x: outer(inner(x))

def val_func_mfilter(container, function):
    return val_func_merge(val_func_sfilter(container, function))

def val_func_difference(a, b):
    return type(a)(e for e in a if e not in b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_crop(I, (0, 0), (3, 3))
    x2 = val_func_ofcolor(x1, 0)
    x3 = val_func_asindices(x1)
    x4 = val_func_difference(x3, x2)
    x5 = val_func_normalize(x4)
    x6 = val_func_objects(I, True, False, True)
    x7 = val_func_compose(val_func_toindices, val_func_normalize)
    x8 = val_func_matcher(x7, x5)
    x9 = val_func_mfilter(x6, x8)
    x10 = val_func_fill(I, 5, x9)
    x11 = val_func_asobject(x1)
    O = val_func_paint(x10, x11)
    return [*map(list,O)]

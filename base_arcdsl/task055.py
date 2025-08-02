def val_func_index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

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
    

def val_func_rightmost(patch):
    return max(j for i, j in val_func_toindices(patch))

def val_func_lowermost(patch):
    return max(i for i, j in val_func_toindices(patch))

def val_func_fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_val_func_filled = list(list(row) for row in grid)
    for i, j in val_func_toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_val_func_filled[i][j] = value
    return tuple(tuple(row) for row in grid_val_func_filled)

def val_func_bordering(patch, grid):
    return val_func_uppermost(patch) == 0 or val_func_leftmost(patch) == 0 or val_func_lowermost(patch) == len(grid) - 1 or val_func_rightmost(patch) == len(grid[0]) - 1

def val_func_vmatching(a, b):
    return len(set(j for i, j in val_func_toindices(a)) & set(j for i, j in val_func_toindices(b))) > 0

def val_func_hmatching(a, b):
    return len(set(i for i, j in val_func_toindices(a)) & set(i for i, j in val_func_toindices(b))) > 0

def val_func_leftmost(patch):
    return min(j for i, j in val_func_toindices(patch))

def val_func_uppermost(patch):
    return min(i for i, j in val_func_toindices(patch))

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

def val_func_toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(val_func_index for value, val_func_index in patch)
    return patch

def val_func_colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

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

def val_func_remove(value, container):
    return type(container)(e for e in container if e != value)

def val_func_extract(container, condition):
    return next(e for e in container if condition(e))

def val_func_sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def val_func_argmin(container, compfunc):
    return min(container, key=compfunc)

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def val_func_flip(b):
    return not b

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_objects(I, True, False, False)
    x2 = val_func_colorfilter(x1, 0)
    x3 = val_func_apply(val_func_toindices, x2)
    x4 = val_func_rbind(val_func_bordering, I)
    x5 = val_func_compose(val_func_flip, x4)
    x6 = val_func_extract(x3, x5)
    x7 = val_func_remove(x6, x3)
    x8 = val_func_lbind(val_func_vmatching, x6)
    x9 = val_func_lbind(val_func_hmatching, x6)
    x10 = val_func_sfilter(x7, x8)
    x11 = val_func_sfilter(x7, x9)
    x12 = val_func_argmin(x10, val_func_uppermost)
    x13 = val_func_argmax(x10, val_func_uppermost)
    x14 = val_func_argmin(x11, val_func_leftmost)
    x15 = val_func_argmax(x11, val_func_leftmost)
    x16 = val_func_fill(I, 6, x6)
    x17 = val_func_fill(x16, 2, x12)
    x18 = val_func_fill(x17, 1, x13)
    x19 = val_func_fill(x18, 4, x14)
    O = val_func_fill(x19, 3, x15)
    return [*map(list,O)]

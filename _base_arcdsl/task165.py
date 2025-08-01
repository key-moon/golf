def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def neighbors(loc):
    return dneighbors(loc) | ineighbors(loc)

def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def lowermost(patch):
    return max(i for i, j in toindices(patch))

def rightmost(patch):
    return max(j for i, j in toindices(patch))

def leftmost(patch):
    return min(j for i, j in toindices(patch))

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

def height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1

def index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def cover(grid, patch):
    return fill(grid, mostcolor(grid), toindices(patch))

def paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

def move(grid, obj, offset):
    return paint(cover(grid, obj), shift(obj, offset))

def center(patch):
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)

def underfill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    bg = mostcolor(grid)
    g = list(list(r) for r in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def color(obj):
    return next(iter(obj))[0]

def vmatching(a, b):
    return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0

def uppermost(patch):
    return min(i for i, j in toindices(patch))

def objects(grid, univalued, diagonal, without_bg):
    bg = mostcolor(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
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

def mapply(function, container):
    return merge(apply(function, container))

def apply(function, container):
    return type(container)(function(e) for e in container)

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def chain(h, g, f,):
    return lambda x: h(g(f(x)))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def remove(value, container):
    return type(container)(e for e in container if e != value)

def first(container):
    return next(iter(container))

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (       0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )

def increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def both(a, b):
    return a and b

def argmax(container, compfunc):
    return max(container, key=compfunc)

def merge(containers):
    return type(containers)(e for c in containers for e in c)

def size(container):
    return len(container)

def greater(a, b):
    return a > b

def p(I):
    x1 = objects(I, True, True, True)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = merge(x3)
    x5 = color(x4)
    x6 = uppermost(x2)
    x7 = rbind(greater, x6)
    x8 = compose(x7, uppermost)
    x9 = rbind(vmatching, x2)
    x10 = fork(both, x9, x8)
    x11 = sfilter(x3, x10)
    x12 = increment(x6)
    x13 = rbind(greater, x12)
    x14 = compose(x13, first)
    x15 = rbind(sfilter, x14)
    x16 = chain(x15, vfrontier, center)
    x17 = mapply(x16, x11)
    O = underfill(I, x5, x17)
    return O

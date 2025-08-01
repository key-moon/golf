def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def merge(containers):
    return type(containers)(e for c in containers for e in c)

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

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

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def compress(grid):
    ri = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    ci = tuple(j for j, c in enumerate(dmirror(grid)) if len(set(c)) == 1)
    return tuple(tuple(v for j, v in enumerate(r) if j not in ci) for i, r in enumerate(grid) if i not in ri)

def replace(grid, replacee, replacer):
    return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)

def downscale(grid, factor):
    h, w = len(grid), len(grid[0])
    g = tuple()
    for i in range(h):
        r = tuple()
        for j in range(w):
            if j % factor == 0:
                r = r + (grid[i][j],)
        g = g + (r, )
    h = len(g)
    dsg = tuple()
    for i in range(h):
        if i % factor == 0:
            dsg = dsg + (g[i],)
    return dsg

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)

def color(obj):
    return next(iter(obj))[0]

def neighbors(loc):
    return dneighbors(loc) | ineighbors(loc)

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

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

def matcher(function, target):
    return lambda x: function(x) == target

def astuple(a, b):
    return (a, b)

def insert(value, container):
    return container.union(frozenset({value}))

def mfilter(container, function):
    return merge(sfilter(container, function))

def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def identity(x):
    return x

def p(I):
    x1 = compress(I)
    x2 = neighbors((0, 0))
    x3 = insert((0, 0), x2)
    x4 = rbind(multiply, 3)
    x5 = apply(x4, x3)
    x6 = astuple(4, 4)
    x7 = shift(x5, x6)
    x8 = fork(insert, identity, neighbors)
    x9 = apply(x8, x7)
    x10 = rbind(toobject, x1)
    x11 = apply(x10, x9)
    x12 = rbind(colorcount, 6)
    x13 = matcher(x12, 2)
    x14 = mfilter(x11, x13)
    x15 = fill(x1, 1, x14)
    x16 = replace(x15, 6, 0)
    O = downscale(x16, 3)
    return O

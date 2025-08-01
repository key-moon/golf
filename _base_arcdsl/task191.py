def merge(containers):
    return type(containers)(e for c in containers for e in c)

def lowermost(patch):
    return max(i for i, j in toindices(patch))

def rightmost(patch):
    return max(j for i, j in toindices(patch))

def leftmost(patch):
    return min(j for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

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

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def shape(piece):
    return (height(piece), width(piece))

def subgrid(patch, grid):
    return crop(grid, ulcorner(patch), shape(patch))

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def color(obj):
    return next(iter(obj))[0]

def normalize(patch):
    if len(patch) == 0:
        return patch
    return shift(patch, (-uppermost(patch), -leftmost(patch)))

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

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

def mpapply(function, a, b):
    return merge(papply(function, a, b))

def papply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

def mapply(function, container):
    return merge(apply(function, container))

def apply(function, container):
    return type(container)(function(e) for e in container)

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

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

def chain(h, g, f,):
    return lambda x: h(g(f(x)))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def product(a, b):
    return frozenset((i, j) for j in b for i in a)

def astuple(a, b):
    return (a, b)

def interval(start, stop, step):
    return tuple(range(start, stop, step))

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (       0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )

def increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def size(container):
    return len(container)

def difference(a, b):
    return type(a)(e for e in a if e not in b)

def combine(a, b):
    return type(a)((*a, *b))

def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def p(I):
    x1 = height(I)
    x2 = width(I)
    x3 = ofcolor(I, 1)
    x4 = ofcolor(I, 4)
    x5 = ulcorner(x3)
    x6 = subgrid(x3, I)
    x7 = rot90(x6)
    x8 = rot180(x6)
    x9 = rot270(x6)
    x10 = matcher(size, 0)
    x11 = rbind(ofcolor, 1)
    x12 = compose(normalize, x11)
    x13 = rbind(ofcolor, 4)
    x14 = rbind(shift, x5)
    x15 = compose(x14, x13)
    x16 = lbind(subtract, x1)
    x17 = chain(increment, x16, height)
    x18 = lbind(subtract, x2)
    x19 = chain(increment, x18, width)
    x20 = rbind(interval, 1)
    x21 = lbind(x20, 0)
    x22 = compose(x21, x17)
    x23 = compose(x21, x19)
    x24 = fork(product, x22, x23)
    x25 = rbind(shift, (-1, -1))
    x26 = lbind(lbind, shift)
    x27 = chain(x26, x25, x12)
    x28 = astuple(x6, x7)
    x29 = astuple(x8, x9)
    x30 = combine(x28, x29)
    x31 = apply(x15, x30)
    x32 = lbind(difference, x4)
    x33 = apply(x32, x31)
    x34 = apply(normalize, x31)
    x35 = apply(x24, x34)
    x36 = lbind(rbind, difference)
    x37 = apply(x26, x34)
    x38 = apply(x36, x33)
    x39 = papply(compose, x38, x37)
    x40 = lbind(compose, x10)
    x41 = apply(x40, x39)
    x42 = papply(sfilter, x35, x41)
    x43 = apply(x27, x30)
    x44 = mpapply(mapply, x43, x42)
    O = fill(I, 1, x44)
    return O

def merge(containers):
    return type(containers)(e for c in containers for e in c)

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def lowermost(patch):
    return max(i for i, j in toindices(patch))

def rightmost(patch):
    return max(j for i, j in toindices(patch))

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

def leftmost(patch):
    return min(j for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

def normalize(patch):
    if len(patch) == 0:
        return patch
    return shift(patch, (-uppermost(patch), -leftmost(patch)))

def shape(piece):
    return (height(piece), width(piece))

def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def occurrences(grid, obj):
    occs = set()
    normed = normalize(obj)
    h, w = len(grid), len(grid[0])
    oh, ow = shape(obj)
    h2, w2 = h - oh + 1, w - ow + 1
    for i in range(h2):
        for j in range(w2):
            occurs = Truerue
            for v, (a, b) in shift(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and grid[a][b] == v):
                    occurs = Falsealse
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)

def canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def vconcat(a, b):
    return a + b

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = ulcorner(piece)[0] + lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

def asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def mapply(function, container):
    return merge(apply(function, container))

def apply(function, container):
    return type(container)(function(e) for e in container)

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def astuple(a, b):
    return (a, b)

def p(I):
    x1 = canvas(5, (2, 2))
    x2 = asobject(x1)
    x3 = occurrences(I, x2)
    x4 = lbind(shift, x2)
    x5 = mapply(x4, x3)
    x6 = fill(I, 8, x5)
    x7 = canvas(5, (1, 1))
    x8 = astuple(2, 1)
    x9 = canvas(8, x8)
    x10 = vconcat(x9, x7)
    x11 = asobject(x10)
    x12 = occurrences(x6, x11)
    x13 = lbind(shift, x11)
    x14 = mapply(x13, x12)
    x15 = fill(x6, 2, x14)
    x16 = astuple(1, 3)
    x17 = canvas(5, x16)
    x18 = asobject(x17)
    x19 = occurrences(x15, x18)
    x20 = lbind(shift, x18)
    x21 = mapply(x20, x19)
    x22 = fill(x15, 2, x21)
    x23 = hmirror(x10)
    x24 = asobject(x23)
    x25 = occurrences(x22, x24)
    x26 = lbind(shift, x24)
    x27 = mapply(x26, x25)
    x28 = fill(x22, 2, x27)
    x29 = dmirror(x10)
    x30 = asobject(x29)
    x31 = occurrences(x28, x30)
    x32 = lbind(shift, x30)
    x33 = mapply(x32, x31)
    x34 = fill(x28, 2, x33)
    x35 = vmirror(x29)
    x36 = asobject(x35)
    x37 = occurrences(x34, x36)
    x38 = lbind(shift, x36)
    x39 = mapply(x38, x37)
    O = fill(x34, 2, x39)
    return O

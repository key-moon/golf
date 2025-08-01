def merge(containers):
    return type(containers)(e for c in containers for e in c)

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

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

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)

def color(obj):
    return next(iter(obj))[0]

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def bordering(patch, grid):
    return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or rightmost(patch) == len(grid[0]) - 1

def neighbors(loc):
    return dneighbors(loc) | ineighbors(loc)

def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

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

def last(container):
    return max(enumerate(container))[1]

def first(container):
    return next(iter(container))

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def positive(x):
    return x > 0

def both(a, b):
    return a and b

def initset(value):
    return frozenset({value})

def argmax(container, compfunc):
    return max(container, key=compfunc)

def size(container):
    return len(container)

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def contained(value, container):
    return value in container

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
    I=tuple(map(tuple,I))
    x1 = asindices(I)
    x2 = fork(product, identity, identity)
    x3 = lbind(canvas, 0)
    x4 = compose(asobject, x3)
    x5 = fork(multiply, first, last)
    x6 = compose(positive, size)
    x7 = lbind(lbind, shift)
    x8 = rbind(fork, x5)
    x9 = lbind(x8, multiply)
    x10 = lbind(chain, x6)
    x11 = rbind(x10, x4)
    x12 = lbind(lbind, occurrences)
    x13 = chain(x9, x11, x12)
    x14 = compose(x2, first)
    x15 = compose(x13, last)
    x16 = fork(argmax, x14, x15)
    x17 = chain(x7, x4, x16)
    x18 = compose(x4, x16)
    x19 = fork(occurrences, last, x18)
    x20 = fork(mapply, x17, x19)
    x21 = multiply(2, 6)
    x22 = interval(3, x21, 1)
    x23 = astuple(x22, I)
    x24 = x20(x23)
    x25 = fill(I, 3, x24)
    x26 = interval(3, 10, 1)
    x27 = astuple(x26, x25)
    x28 = x20(x27)
    x29 = fill(x25, 3, x28)
    x30 = astuple(x26, x29)
    x31 = x20(x30)
    x32 = fill(x29, 3, x31)
    x33 = rbind(toobject, x32)
    x34 = rbind(colorcount, 3)
    x35 = chain(x34, x33, neighbors)
    x36 = matcher(x35, 8)
    x37 = sfilter(x1, x36)
    x38 = fill(I, 3, x37)
    x39 = ofcolor(x38, 0)
    x40 = rbind(bordering, x38)
    x41 = compose(x40, initset)
    x42 = lbind(contained, 3)
    x43 = rbind(toobject, x38)
    x44 = chain(x42, palette, x43)
    x45 = compose(x44, dneighbors)
    x46 = fork(both, x45, x41)
    x47 = sfilter(x39, x46)
    O = fill(x38, 3, x47)
    return [*map(list,O)]

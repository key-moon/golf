def index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def cover(grid, patch):
    return fill(grid, mostcolor(grid), toindices(patch))

def move(grid, obj, offset):
    return paint(cover(grid, obj), shift(obj, offset))

def canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)

def color(obj):
    return next(iter(obj))[0]

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def rightmost(patch):
    return max(j for i, j in toindices(patch))

def leftmost(patch):
    return min(j for i, j in toindices(patch))

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

def recolor(value, patch):
    return frozenset((value, index) for index in toindices(patch))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

def apply(function, container):
    return type(container)(function(e) for e in container)

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

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

def astuple(a, b):
    return (a, b)

def other(container, value):
    return first(remove(value, container))

def remove(value, container):
    return type(container)(e for e in container if e != value)

def last(container):
    return max(enumerate(container))[1]

def first(container):
    return next(iter(container))

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1))

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def initset(value):
    return frozenset({value})

def argmin(container, compfunc):
    return min(container, key=compfunc)

def size(container):
    return len(container)

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def intersection(a, b):
    return a & b

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

def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = objects(I, False, False, True)
    x2 = rbind(other, 5)
    x3 = compose(x2, palette)
    x4 = fork(recolor, x3, identity)
    x5 = apply(x4, x1)
    x6 = order(x5, leftmost)
    x7 = compose(last, last)
    x8 = lbind(matcher, x7)
    x9 = compose(x8, leftmost)
    x10 = compose(x8, rightmost)
    x11 = fork(sfilter, identity, x9)
    x12 = fork(sfilter, identity, x10)
    x13 = compose(dneighbors, last)
    x14 = rbind(chain, x13)
    x15 = lbind(x14, size)
    x16 = lbind(rbind, intersection)
    x17 = chain(x15, x16, toindices)
    x18 = fork(argmin, x11, x17)
    x19 = fork(argmin, x12, x17)
    x20 = compose(last, x18)
    x21 = compose(last, x19)
    x22 = astuple(0, (1, -1))
    x23 = initset(x22)
    x24 = lbind(add, (0, 1))
    x25 = chain(x20, first, last)
    x26 = compose(x21, first)
    x27 = fork(subtract, x26, x25)
    x28 = compose(first, last)
    x29 = compose(x24, x27)
    x30 = fork(shift, x28, x29)
    x31 = fork(combine, first, x30)
    x32 = fork(remove, x28, last)
    x33 = fork(astuple, x31, x32)
    x34 = size(x1)
    x35 = power(x33, x34)
    x36 = astuple(x23, x6)
    x37 = x35(x36)
    x38 = first(x37)
    x39 = width(x38)
    x40 = decrement(x39)
    x41 = astuple(3, x40)
    x42 = canvas(0, x41)
    O = paint(x42, x38)
    return [*map(list,O)]

def merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def manhattan(a, b):
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))

def lowermost(patch):
    return max(i for i, j in toindices(patch))

def rightmost(patch):
    return max(j for i, j in toindices(patch))

def leftmost(patch):
    return min(j for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

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

def center(patch):
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def backdrop(patch):
    if len(patch) == 0:
        return frozenset({})
    indices = toindices(patch)
    si, sj = ulcorner(indices)
    ei, ej = lrcorner(patch)
    return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))

def delta(patch):
    if len(patch) == 0:
        return frozenset({})
    return backdrop(patch) - toindices(patch)

def index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def position(a, b):
    ia, ja = center(toindices(a))
    ib, jb = center(toindices(b))
    if ia == ib:
        return (0, 1 if ja < jb else -1)
    elif ja == jb:
        return (1 if ia < ib else -1, 0)
    elif ia < ib:
        return (1, 1 if ja < jb else -1)
    elif ia > ib:
        return (-1, 1 if ja < jb else -1)

def paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)

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

def color(obj):
    return next(iter(obj))[0]

def adjacent(a, b):
    return manhattan(a, b) == 1

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

def shape(piece):
    return (height(piece), width(piece))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def chain(h, g, f,):
    return lambda x: h(g(f(x)))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def insert(value, container):
    return container.union(frozenset({value}))

def last(container):
    return max(enumerate(container))[1]

def first(container):
    return next(iter(container))

def extract(container, condition):
    return next(e for e in container if condition(e))

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def tojvec(j):
    return (0, j)

def toivec(i):
    return (i, 0)

def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (       0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )

def initset(value):
    return frozenset({value})

def difference(a, b):
    return type(a)(e for e in a if e not in b)

def intersection(a, b):
    return a & b

def combine(a, b):
    return type(a)((*a, *b))

def equality(a, b):
    return a == b

def invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

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
    x1 = objects(I, False, True, True)
    x2 = lbind(rbind, equality)
    x3 = rbind(compose, first)
    x4 = chain(x3, x2, mostcolor)
    x5 = fork(sfilter, identity, x4)
    x6 = fork(difference, identity, x5)
    x7 = lbind(rbind, adjacent)
    x8 = rbind(compose, initset)
    x9 = chain(x8, x7, x6)
    x10 = fork(extract, x5, x9)
    x11 = fork(insert, x10, x6)
    x12 = lbind(recolor, 0)
    x13 = chain(x12, delta, x11)
    x14 = fork(combine, x11, x13)
    x15 = fork(position, x5, x6)
    x16 = chain(toivec, first, x15)
    x17 = chain(tojvec, last, x15)
    x18 = fork(multiply, shape, x16)
    x19 = fork(multiply, shape, x17)
    x20 = fork(multiply, shape, x15)
    x21 = fork(shift, hmirror, x18)
    x22 = fork(shift, vmirror, x19)
    x23 = compose(hmirror, vmirror)
    x24 = fork(shift, x23, x20)
    x25 = lbind(compose, x5)
    x26 = x25(x21)
    x27 = x25(x22)
    x28 = x25(x24)
    x29 = compose(crement, invert)
    x30 = lbind(compose, x29)
    x31 = x30(x16)
    x32 = x30(x17)
    x33 = x30(x15)
    x34 = fork(shift, x26, x31)
    x35 = fork(shift, x27, x32)
    x36 = fork(shift, x28, x33)
    x37 = lbind(index, I)
    x38 = lbind(compose, toindices)
    x39 = x38(x14)
    x40 = x38(x34)
    x41 = x38(x35)
    x42 = x38(x36)
    x43 = fork(intersection, x39, x40)
    x44 = fork(intersection, x39, x41)
    x45 = fork(intersection, x39, x42)
    x46 = chain(x37, first, x43)
    x47 = chain(x37, first, x44)
    x48 = chain(x37, first, x45)
    x49 = fork(recolor, x46, x34)
    x50 = fork(recolor, x47, x35)
    x51 = fork(recolor, x48, x36)
    x52 = mapply(x49, x1)
    x53 = mapply(x50, x1)
    x54 = mapply(x51, x1)
    x55 = paint(I, x52)
    x56 = paint(x55, x53)
    O = paint(x56, x54)
    return O

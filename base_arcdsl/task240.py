def merge(containers):
    return type(containers)(e for c in containers for e in c)

def leftmost(patch):
    return min(j for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def lefthalf(grid):
    return rot270(tophalf(rot90(grid)))

def tophalf(grid):
    return grid[:len(grid) // 2]

def cover(grid, patch):
    return fill(grid, mostcolor(grid), toindices(patch))

def connect(a, b):
    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()

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

def rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def color(obj):
    return next(iter(obj))[0]

def numcolors(element):
    return len(palette(element))

def partition(grid):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value) for value in palette(grid))

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

def recolor(value, patch):
    return frozenset((value, index) for index in toindices(patch))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def llcorner(patch):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

def urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def sizefilter(container, n):
    return frozenset(item for item in container if len(item) == n)

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

def chain(h, g, f,):
    return lambda x: h(g(f(x)))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def pair(a, b):
    return tuple(zip(a, b))

def insert(value, container):
    return container.union(frozenset({value}))

def last(container):
    return max(enumerate(container))[1]

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def tojvec(j):
    return (0, j)

def initset(value):
    return frozenset({value})

def argmax(container, compfunc):
    return max(container, key=compfunc)

def maximum(container):
    return max(container, default=0)

def size(container):
    return len(container)

def combine(a, b):
    return type(a)((*a, *b))

def even(n):
    return n % 2 == 0

def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def p(I):
    I=tuple(map(tuple,I))
    x1 = rot90(I)
    x2 = rot180(I)
    x3 = rot270(I)
    x4 = initset(I)
    x5 = chain(numcolors, lefthalf, tophalf)
    x6 = insert(x1, x4)
    x7 = insert(x2, x6)
    x8 = insert(x3, x7)
    x9 = argmax(x8, x5)
    x10 = vmirror(x9)
    x11 = papply(pair, x9, x10)
    x12 = lbind(apply, maximum)
    x13 = apply(x12, x11)
    x14 = partition(x13)
    x15 = sizefilter(x14, 4)
    x16 = apply(llcorner, x15)
    x17 = apply(lrcorner, x15)
    x18 = combine(x16, x17)
    x19 = cover(x13, x18)
    x20 = tojvec(-2)
    x21 = rbind(add, (0, 2))
    x22 = rbind(add, x20)
    x23 = compose(x21, ulcorner)
    x24 = compose(x22, urcorner)
    x25 = fork(connect, x23, x24)
    x26 = compose(even, last)
    x27 = rbind(sfilter, x26)
    x28 = chain(normalize, x27, x25)
    x29 = fork(shift, x28, x23)
    x30 = fork(recolor, color, x29)
    x31 = mapply(x30, x15)
    x32 = paint(x19, x31)
    x33 = rot90(x32)
    x34 = rot180(x32)
    x35 = rot270(x32)
    x36 = papply(pair, x32, x33)
    x37 = apply(x12, x36)
    x38 = papply(pair, x37, x34)
    x39 = apply(x12, x38)
    x40 = papply(pair, x39, x35)
    O = apply(x12, x40)
    return [*map(list,O)]

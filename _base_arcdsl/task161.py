def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def lowermost(patch):
    return max(i for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

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

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def box(patch):
    if len(patch) == 0:
        return patch
    ai, aj = ulcorner(patch)
    bi, bj = lrcorner(patch)
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

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

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def color(obj):
    return next(iter(obj))[0]

def hline(patch):
    return width(patch) == len(patch) and height(patch) == 1

def vline(patch):
    return height(patch) == len(patch) and width(patch) == 1

def fgpartition(grid):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid) - {mostcolor(grid)}
    )

def partition(grid):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid)
    )

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def prapply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

def rapply(functions, value):
    return type(functions)(function(value) for function in functions)

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

def mfilter(container, function):
    return merge(sfilter(container, function))

def positive(x):
    return x > 0

def either(a, b):
    return a or b

def both(a, b):
    return a and b

def merge(containers):
    return type(containers)(e for c in containers for e in c)

def size(container):
    return len(container)

def difference(a, b):
    return type(a)(e for e in a if e not in b)

def p(I):
    x1 = leastcolor(I)
    x2 = ofcolor(I, x1)
    x3 = prapply(connect, x2, x2)
    x4 = fgpartition(I)
    x5 = merge(x4)
    x6 = cover(I, x5)
    x7 = fork(either, hline, vline)
    x8 = box(x5)
    x9 = rbind(difference, x8)
    x10 = chain(positive, size, x9)
    x11 = fork(both, x7, x10)
    x12 = mfilter(x3, x11)
    O = fill(x6, x1, x12)
    return O

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

def index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def color(obj):
    return next(iter(obj))[0]

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

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

def shoot(start, direction):
    return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

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

def vline(patch):
    return height(patch) == len(patch) and width(patch) == 1

def rightmost(patch):
    return max(j for i, j in toindices(patch))

def leftmost(patch):
    return min(j for i, j in toindices(patch))

def lowermost(patch):
    return max(i for i, j in toindices(patch))

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

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def shape(piece):
    return (height(piece), width(piece))

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

def astuple(a, b):
    return (a, b)

def interval(start, stop, step):
    return tuple(range(start, stop, step))

def first(container):
    return next(iter(container))

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

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def minimum(container):
    return min(container, default=0)

def difference(a, b):
    return type(a)(e for e in a if e not in b)

def combine(a, b):
    return type(a)((*a, *b))

def equality(a, b):
    return a == b

def invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def p(I):
    x1 = objects(I, False, False, True)
    x2 = matcher(first, 2)
    x3 = rbind(sfilter, x2)
    x4 = compose(lowermost, x3)
    x5 = compose(rightmost, x3)
    x6 = compose(uppermost, x3)
    x7 = compose(leftmost, x3)
    x8 = fork(equality, x4, lowermost)
    x9 = fork(equality, x5, rightmost)
    x10 = fork(equality, x6, uppermost)
    x11 = fork(equality, x7, leftmost)
    x12 = compose(invert, x10)
    x13 = compose(invert, x11)
    x14 = fork(add, x12, x8)
    x15 = fork(add, x13, x9)
    x16 = fork(astuple, x14, x15)
    x17 = compose(center, x3)
    x18 = fork(shoot, x17, x16)
    x19 = mapply(x18, x1)
    x20 = fill(I, 2, x19)
    x21 = compose(vline, x18)
    x22 = sfilter(x1, x21)
    x23 = difference(x1, x22)
    x24 = chain(decrement, minimum, shape)
    x25 = compose(increment, x24)
    x26 = compose(invert, x24)
    x27 = rbind(interval, 1)
    x28 = fork(x27, x26, x25)
    x29 = lbind(apply, toivec)
    x30 = lbind(apply, tojvec)
    x31 = lbind(lbind, shift)
    x32 = compose(x31, x18)
    x33 = compose(x29, x28)
    x34 = compose(x30, x28)
    x35 = fork(mapply, x32, x33)
    x36 = fork(mapply, x32, x34)
    x37 = mapply(x35, x23)
    x38 = mapply(x36, x22)
    x39 = combine(x37, x38)
    O = underfill(x20, 3, x39)
    return O

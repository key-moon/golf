def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def merge(containers):
    return type(containers)(e for c in containers for e in c)

def rightmost(patch):
    return max(j for i, j in toindices(patch))

def leftmost(patch):
    return min(j for i, j in toindices(patch))

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

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def lowermost(patch):
    return max(i for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

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

def hline(patch):
    return width(patch) == len(patch) and height(patch) == 1

def vline(patch):
    return height(patch) == len(patch) and width(patch) == 1

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

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def colorfilter(objs, value):
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

def prapply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

def mapply(function, container):
    return merge(apply(function, container))

def rapply(functions, value):
    return type(functions)(function(value) for function in functions)

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

def mfilter(container, function):
    return merge(sfilter(container, function))

def tojvec(j):
    return (0, j)

def toivec(i):
    return (i, 0)

def either(a, b):
    return a or b

def both(a, b):
    return a and b

def initset(value):
    return frozenset({value})

def argmax(container, compfunc):
    return max(container, key=compfunc)

def valmax(container, compfunc):
    return compfunc(max(container, key=compfunc, default=0))

def size(container):
    return len(container)

def greater(a, b):
    return a > b

def combine(a, b):
    return type(a)((*a, *b))

def halve(n):
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)

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

def p(I):
    x1 = ofcolor(I, 2)
    x2 = prapply(connect, x1, x1)
    x3 = lbind(greater, 6)
    x4 = compose(x3, size)
    x5 = fork(either, vline, hline)
    x6 = fork(both, x4, x5)
    x7 = mfilter(x2, x6)
    x8 = fill(I, 2, x7)
    x9 = objects(x8, True, False, False)
    x10 = colorfilter(x9, 2)
    x11 = valmax(x10, width)
    x12 = halve(x11)
    x13 = toivec(x12)
    x14 = tojvec(x12)
    x15 = rbind(add, (0, 2))
    x16 = rbind(add, (2, 0))
    x17 = rbind(subtract, (0, 2))
    x18 = rbind(subtract, (2, 0))
    x19 = rbind(colorcount, 2)
    x20 = rbind(toobject, x8)
    x21 = compose(initset, x15)
    x22 = fork(insert, x16, x21)
    x23 = fork(insert, x17, x22)
    x24 = fork(insert, x18, x23)
    x25 = fork(combine, dneighbors, x24)
    x26 = chain(x19, x20, x25)
    x27 = rbind(argmax, x26)
    x28 = compose(x27, toindices)
    x29 = apply(x28, x10)
    x30 = rbind(add, x13)
    x31 = rbind(subtract, x13)
    x32 = rbind(add, x14)
    x33 = rbind(subtract, x14)
    x34 = fork(connect, x30, x31)
    x35 = fork(connect, x32, x33)
    x36 = fork(combine, x34, x35)
    x37 = mapply(x36, x29)
    x38 = fill(x8, 8, x37)
    O = fill(x38, 2, x1)
    return O

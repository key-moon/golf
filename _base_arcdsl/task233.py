def merge(containers):
    return type(containers)(e for c in containers for e in c)

def index(grid, loc):
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def neighbors(loc):
    return dneighbors(loc) | ineighbors(loc)

def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

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

def move(grid, obj, offset):
    return paint(cover(grid, obj), shift(obj, offset))

def switch(grid, a, b):
    return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)

def subgrid(patch, grid):
    return crop(grid, ulcorner(patch), shape(patch))

def paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)

def cmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*(r[::-1] for r in piece[::-1])))
    return vmirror(dmirror(vmirror(piece)))

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

def color(obj):
    return next(iter(obj))[0]

def numcolors(element):
    return len(palette(element))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

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

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)

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

def remove(value, container):
    return type(container)(e for e in container if e != value)

def last(container):
    return max(enumerate(container))[1]

def first(container):
    return next(iter(container))

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def positive(x):
    return x > 0

def argmax(container, compfunc):
    return max(container, key=compfunc)

def size(container):
    return len(container)

def greater(a, b):
    return a > b

def combine(a, b):
    return type(a)((*a, *b))

def contained(value, container):
    return value in container

def equality(a, b):
    return a == b

def flip(b):
    return not b

def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def p(I):
    x1 = objects(I, False, True, True)
    x2 = argmax(x1, size)
    x3 = subgrid(x2, I)
    x4 = rbind(greater, 1)
    x5 = compose(x4, numcolors)
    x6 = sfilter(x1, x5)
    x7 = lbind(rbind, subtract)
    x8 = switch(x3, 2, 0)
    x9 = lbind(occurrences, x8)
    x10 = lbind(lbind, shift)
    x11 = compose(x7, ulcorner)
    x12 = matcher(first, 2)
    x13 = compose(flip, x12)
    x14 = rbind(sfilter, x12)
    x15 = rbind(sfilter, x13)
    x16 = lbind(recolor, 0)
    x17 = compose(x16, x15)
    x18 = fork(combine, x17, x14)
    x19 = chain(x11, x18, normalize)
    x20 = objects(x8, True, True, True)
    x21 = apply(toindices, x20)
    x22 = chain(x9, x18, normalize)
    x23 = rbind(colorcount, 2)
    x24 = lbind(sfilter, x21)
    x25 = chain(size, first, x24)
    x26 = compose(positive, size)
    x27 = lbind(lbind, contained)
    x28 = chain(x26, x24, x27)
    x29 = compose(x25, x27)
    x30 = rbind(sfilter, x28)
    x31 = compose(x30, x22)
    x32 = lbind(rbind, equality)
    x33 = rbind(compose, x29)
    x34 = chain(x33, x32, x23)
    x35 = fork(sfilter, x31, x34)
    x36 = fork(apply, x19, x35)
    x37 = compose(x10, normalize)
    x38 = fork(mapply, x37, x36)
    x39 = astuple(cmirror, dmirror)
    x40 = astuple(hmirror, vmirror)
    x41 = combine(x39, x40)
    x42 = product(x41, x41)
    x43 = fork(compose, first, last)
    x44 = apply(x43, x42)
    x45 = lbind(rapply, x44)
    x46 = mapply(x45, x6)
    x47 = mapply(x38, x46)
    x48 = paint(x3, x47)
    x49 = palette(x47)
    x50 = lbind(remove, 2)
    x51 = x50(x49)
    x52 = chain(first, x50, palette)
    x53 = rbind(contained, x51)
    x54 = chain(flip, x53, x52)
    x55 = sfilter(x6, x54)
    x56 = fork(apply, x19, x22)
    x57 = fork(mapply, x37, x56)
    x58 = mapply(x45, x55)
    x59 = mapply(x57, x58)
    O = paint(x48, x59)
    return O

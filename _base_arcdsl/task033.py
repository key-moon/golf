def merge(containers):
    return type(containers)(e for c in containers for e in c)

def lowermost(patch):
    return max(i for i, j in toindices(patch))

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

def asobject(grid):
    return frozenset((v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r))

def color(obj):
    return next(iter(obj))[0]

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def partition(grid):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid)
    )

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def papply(function, a, b):
    return tuple(function(i, j) for i, j in zip(a, b))

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

def matcher(function, target):
    return lambda x: function(x) == target

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

def totuple(container):
    return tuple(container)

def extract(container, condition):
    return next(e for e in container if condition(e))

def initset(value):
    return frozenset({value})

def difference(a, b):
    return type(a)(e for e in a if e not in b)

def flip(b):
    return not b

def divide(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)

def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

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
    x1 = height(I)
    x2 = mostcolor(I)
    x3 = asobject(I)
    x4 = subtract(x1, 2)
    x5 = divide(x4, 3)
    x6 = astuple(x5, x5)
    x7 = crop(I, (0, 0), x6)
    x8 = partition(x7)
    x9 = matcher(color, 0)
    x10 = compose(flip, x9)
    x11 = extract(x8, x10)
    x12 = initset(x2)
    x13 = palette(x3)
    x14 = palette(x11)
    x15 = difference(x13, x14)
    x16 = difference(x15, x12)
    x17 = first(x16)
    x18 = interval(0, 3, 1)
    x19 = product(x18, x18)
    x20 = totuple(x19)
    x21 = apply(first, x20)
    x22 = apply(last, x20)
    x23 = lbind(multiply, x5)
    x24 = apply(x23, x21)
    x25 = apply(x23, x22)
    x26 = papply(add, x24, x21)
    x27 = papply(add, x25, x22)
    x28 = papply(astuple, x26, x27)
    x29 = lbind(shift, x11)
    x30 = mapply(x29, x28)
    O = underfill(I, x17, x30)
    return O

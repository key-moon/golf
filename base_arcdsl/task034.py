def merge(containers):
    return type(containers)(e for c in containers for e in c)

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

def replace(grid, replacee, replacer):
    return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)

def paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)

def color(obj):
    return next(iter(obj))[0]

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def recolor(value, patch):
    return frozenset((value, index) for index in toindices(patch))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def prapply(   function, a, b):
    return frozenset(function(i, j) for j in b for i in a)

def mapply(function, container):
    return merge(apply(function, container))

def rapply(functions, value):
    return type(functions)(function(value) for function in functions)

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

def compose(outer, inner):
    return lambda x: outer(inner(x))

def interval(start, stop, step):
    return tuple(range(start, stop, step))

def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1))

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def combine(a, b):
    return type(a)((*a, *b))

def double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

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
    

def p(I):
    I=tuple(map(tuple,I))
    x1 = ofcolor(I, 2)
    x2 = replace(I, 2, 0)
    x3 = leastcolor(x2)
    x4 = ofcolor(x2, x3)
    x5 = combine(x1, x4)
    x6 = recolor(x3, x5)
    x7 = compose(decrement, double)
    x8 = ulcorner(x5)
    x9 = invert(x8)
    x10 = shift(x1, x9)
    x11 = apply(x7, x10)
    x12 = interval(0, 9, 1)
    x13 = prapply(multiply, x11, x12)
    x14 = lbind(shift, x6)
    x15 = mapply(x14, x13)
    O = paint(I, x15)
    return [*map(list,O)]

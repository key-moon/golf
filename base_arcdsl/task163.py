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

def toobject(patch, grid):
    h, w = len(grid), len(grid[0])
    return frozenset((grid[i][j], (i, j)) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)

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

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

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

def branch(condition, a, b):
    return a if condition else b

def product(a, b):
    return frozenset((i, j) for j in b for i in a)

def astuple(a, b):
    return (a, b)

def insert(value, container):
    return container.union(frozenset({value}))

def last(container):
    return max(enumerate(container))[1]

def first(container):
    return next(iter(container))

def initset(value):
    return frozenset({value})

def greater(a, b):
    return a > b

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
    x1 = ofcolor(I, 4)
    x2 = first(x1)
    x3 = first(x2)
    x4 = last(x2)
    x5 = greater(x3, 3)
    x6 = greater(x3, 7)
    x7 = greater(x4, 3)
    x8 = greater(x4, 7)
    x9 = branch(x5, 4, 0)
    x10 = branch(x6, 8, x9)
    x11 = branch(x7, 4, 0)
    x12 = branch(x8, 8, x11)
    x13 = astuple(x10, x12)
    x14 = initset(0)
    x15 = insert(4, x14)
    x16 = insert(8, x15)
    x17 = product(x16, x16)
    x18 = crop(I, (0, 0), (3, 3))
    x19 = asindices(x18)
    x20 = recolor(0, x19)
    x21 = lbind(shift, x20)
    x22 = mapply(x21, x17)
    x23 = paint(I, x22)
    x24 = crop(I, x13, (3, 3))
    x25 = replace(x24, 5, 0)
    x26 = ofcolor(x25, 4)
    x27 = first(x26)
    x28 = asindices(x25)
    x29 = toobject(x28, x25)
    x30 = multiply(x27, 4)
    x31 = shift(x29, x30)
    O = paint(x23, x31)
    return [*map(list,O)]

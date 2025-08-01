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

def rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def righthalf(grid):
    return rot270(bottomhalf(rot90(grid)))

def lefthalf(grid):
    return rot270(tophalf(rot90(grid)))

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def tophalf(grid):
    return grid[:len(grid) // 2]

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

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

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

def difference(a, b):
    return type(a)(e for e in a if e not in b)

def identity(x):
    return x

def p(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = tophalf(x1)
    x4 = bottomhalf(x1)
    x5 = tophalf(x2)
    x6 = bottomhalf(x2)
    x7 = rbind(ofcolor, 0)
    x8 = fork(difference, asindices, x7)
    x9 = fork(toobject, x8, identity)
    x10 = x9(x5)
    x11 = x9(x4)
    x12 = x9(x6)
    x13 = paint(x3, x12)
    x14 = paint(x13, x11)
    O = paint(x14, x10)
    return O

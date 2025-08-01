def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

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

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def vmirror(piece):
    if isinstance(piece, tuple):
        return tuple(row[::-1] for row in piece)
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in piece)
    return frozenset((i, d - j) for i, j in piece)

def color(obj):
    return next(iter(obj))[0]

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def compose(outer, inner):
    return lambda x: outer(inner(x))

def last(container):
    return max(enumerate(container))[1]

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def even(n):
    return n % 2 == 0

def p(I):
    x1 = vmirror(I)
    x2 = ofcolor(x1, 5)
    x3 = compose(even, last)
    x4 = sfilter(x2, x3)
    x5 = fill(x1, 3, x4)
    O = vmirror(x5)
    return O

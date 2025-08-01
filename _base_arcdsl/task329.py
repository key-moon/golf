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

def asindices(grid):
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

def matcher(function, target):
    return lambda x: function(x) == target

def compose(outer, inner):
    return lambda x: outer(inner(x))

def last(container):
    return max(enumerate(container))[1]

def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def flip(b):
    return not b

def halve(n):
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)

def p(I):
    x1 = asindices(I)
    x2 = width(I)
    x3 = halve(x2)
    x4 = matcher(last, x3)
    x5 = compose(flip, x4)
    x6 = sfilter(x1, x5)
    O = fill(I, 0, x6)
    return O

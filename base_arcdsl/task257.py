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

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def color(obj):
    return next(iter(obj))[0]

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def p(I):
    I=tuple(map(tuple,I))
    x1 = tophalf(I)
    x2 = bottomhalf(I)
    x3 = lefthalf(x1)
    x4 = righthalf(x1)
    x5 = lefthalf(x2)
    x6 = righthalf(x2)
    x7 = ofcolor(x4, 4)
    x8 = ofcolor(x3, 7)
    x9 = ofcolor(x5, 8)
    x10 = fill(x6, 8, x9)
    x11 = fill(x10, 4, x7)
    O = fill(x11, 7, x8)
    return [*map(list,O)]

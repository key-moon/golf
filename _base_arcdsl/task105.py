def merge(containers):
    return type(containers)(e for c in containers for e in c)

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def shape(piece):
    return (height(piece), width(piece))

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

def hline(patch):
    return width(patch) == len(patch) and height(patch) == 1

def vline(patch):
    return height(patch) == len(patch) and width(patch) == 1

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def box(patch):
    if len(patch) == 0:
        return patch
    ai, aj = ulcorner(patch)
    bi, bj = lrcorner(patch)
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def hfrontier(location):
    return frozenset((location[0], j) for j in range(30))

def vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

def subgrid(patch, grid):
    return crop(grid, ulcorner(patch), shape(patch))

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

def color(obj):
    return next(iter(obj))[0]

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def mapply(function, container):
    return merge(apply(function, container))

def apply(function, container):
    return type(container)(function(e) for e in container)

def branch(condition, a, b):
    return a if condition else b

def size(container):
    return len(container)

def greater(a, b):
    return a > b

def p(I):
    x1 = ofcolor(I, 1)
    x2 = box(x1)
    x3 = fill(I, 2, x2)
    x4 = subgrid(x1, x3)
    x5 = ofcolor(x4, 1)
    x6 = mapply(vfrontier, x5)
    x7 = mapply(hfrontier, x5)
    x8 = size(x6)
    x9 = size(x7)
    x10 = greater(x8, x9)
    x11 = branch(x10, x7, x6)
    x12 = fill(x4, 2, x11)
    x13 = ofcolor(x12, 2)
    x14 = ulcorner(x1)
    x15 = shift(x13, x14)
    O = underfill(I, 2, x15)
    return O

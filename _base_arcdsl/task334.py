def color(obj):
    return next(iter(obj))[0]

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def cover(grid, patch):
    return fill(grid, mostcolor(grid), toindices(patch))

def paint(grid, obj):
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def move(grid, obj, offset):
    return paint(cover(grid, obj), shift(obj, offset))

def remove(value, container):
    return type(container)(e for e in container if e != value)

def first(container):
    return next(iter(container))

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

def hfrontier(location):
    return frozenset((location[0], j) for j in range(30))

def vfrontier(location):
    return frozenset((i, location[1]) for i in range(30))

def canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def fill(grid, value, patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def branch(condition, a, b):
    return a if condition else b

def other(container, value):
    return first(remove(value, container))

def combine(a, b):
    return type(a)((*a, *b))

def equality(a, b):
    return a == b

def p(I):
    x1 = palette(I)
    x2 = other(x1, 0)
    x3 = equality(x2, 1)
    x4 = equality(x2, 2)
    x5 = branch(x3, (1, 1), (2, 2))
    x6 = branch(x4, (0, 1), x5)
    x7 = fork(combine, vfrontier, hfrontier)
    x8 = x7(x6)
    x9 = canvas(0, (3, 3))
    O = fill(x9, 5, x8)
    return O

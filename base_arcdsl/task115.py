def lowermost(patch):
    return max(i for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

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

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def portrait(piece):
    return height(piece) > width(piece)

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

def apply(function, container):
    return type(container)(function(e) for e in container)

def branch(condition, a, b):
    return a if condition else b

def astuple(a, b):
    return (a, b)

def dedupe(tup):
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)

def identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = portrait(I)
    x2 = branch(x1, dmirror, identity)
    x3 = branch(x1, height, width)
    x4 = x3(I)
    x5 = astuple(1, x4)
    x6 = x2(I)
    x7 = crop(x6, (0, 0), x5)
    x8 = apply(dedupe, x7)
    O = x2(x8)
    return [*map(list,O)]

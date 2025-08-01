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

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def vconcat(a, b):
    return a + b

def hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = ulcorner(piece)[0] + lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in piece)
    return frozenset((d - i, j) for i, j in piece)

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

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

def astuple(a, b):
    return (a, b)

def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (       0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

def p(I):
    x1 = height(I)
    x2 = width(I)
    x3 = decrement(x1)
    x4 = astuple(x3, x2)
    x5 = crop(I, (0, 0), x4)
    x6 = hmirror(x5)
    x7 = vconcat(I, x6)
    x8 = double(x3)
    x9 = astuple(x8, x2)
    x10 = crop(x7, (1, 0), x9)
    O = vconcat(x7, x10)
    return O

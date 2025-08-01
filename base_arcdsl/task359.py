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

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def upscale(element, factor):
    if isinstance(element, tuple):
        g = tuple()
        for row in element:
            upscaled_row = tuple()
            for value in row:
                upscaled_row = upscaled_row + tuple(value for num in range(factor))
            g = g + tuple(upscaled_row for num in range(factor))
        return g
    else:
        if len(element) == 0:
            return frozenset()
        di_inv, dj_inv = ulcorner(element)
        di, dj = (-di_inv, -dj_inv)
        normed_obj = shift(element, (di, dj))
        o = set()
        for value, (i, j) in normed_obj:
            for io in range(factor):
                for jo in range(factor):
                    o.add((value, (i * factor + io, j * factor + jo)))
        return shift(frozenset(o), (di_inv, dj_inv))

def vupscale(grid, factor):
    g = tuple()
    for row in grid:
        g = g + tuple(row for num in range(factor))
    return g

def hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g

def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

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

def compose(outer, inner):
    return lambda x: outer(inner(x))

def branch(condition, a, b):
    return a if condition else b

def mostcommon(container):
    return max(set(container), key=container.count)

def size(container):
    return len(container)

def greater(a, b):
    return a > b

def repeat(item, num):
    return tuple(item for i in range(num))

def dedupe(tup):
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)

def p(I):
    I=tuple(map(tuple,I))
    x1 = rot90(I)
    x2 = apply(mostcommon, I)
    x3 = apply(mostcommon, x1)
    x4 = repeat(x2, 1)
    x5 = repeat(x3, 1)
    x6 = compose(size, dedupe)
    x7 = x6(x2)
    x8 = x6(x3)
    x9 = greater(x8, x7)
    x10 = branch(x9, height, width)
    x11 = x10(I)
    x12 = rot90(x4)
    x13 = branch(x9, x5, x12)
    x14 = branch(x9, vupscale, hupscale)
    O = x14(x13, x11)
    return [*map(list,O)]

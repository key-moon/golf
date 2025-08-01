def lowermost(patch):
    return max(i for i, j in toindices(patch))

def uppermost(patch):
    return min(i for i, j in toindices(patch))

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

def tophalf(grid):
    return grid[:len(grid) // 2]

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def righthalf(grid):
    return rot270(bottomhalf(rot90(grid)))

def lefthalf(grid):
    return rot270(tophalf(rot90(grid)))

def replace(grid, replacee, replacer):
    return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)

def hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    a, b = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)

def color(obj):
    return next(iter(obj))[0]

def ofcolor(grid, value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)

def portrait(piece):
    return height(piece) > width(piece)

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def apply(function, container):
    return type(container)(function(e) for e in container)

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def branch(condition, a, b):
    return a if condition else b

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def identity(x):
    return x

def p(I):
    x1 = leastcolor(I)
    x2 = replace(I, x1, 5)
    x3 = ofcolor(I, 5)
    x4 = portrait(x3)
    x5 = branch(x4, identity, dmirror)
    x6 = x5(x2)
    x7 = lefthalf(x6)
    x8 = righthalf(x6)
    x9 = rbind(order, identity)
    x10 = rbind(order, invert)
    x11 = apply(x9, x7)
    x12 = apply(x10, x8)
    x13 = hconcat(x11, x12)
    O = x5(x13)
    return O

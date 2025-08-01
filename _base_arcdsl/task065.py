def merge(containers):
    return type(containers)(e for c in containers for e in c)

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def vsplit(grid, n):
    h, w = len(grid) // n, len(grid[0])
    offset = len(grid) % n != 0
    return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))

def hsplit(grid, n):
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))

def color(obj):
    return next(iter(obj))[0]

def numcolors(element):
    return len(palette(element))

def mapply(function, container):
    return merge(apply(function, container))

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

def argmax(container, compfunc):
    return max(container, key=compfunc)

def p(I):
    x1 = vsplit(I, 2)
    x2 = rbind(hsplit, 2)
    x3 = mapply(x2, x1)
    O = argmax(x3, numcolors)
    return O

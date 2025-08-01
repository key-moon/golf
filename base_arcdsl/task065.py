def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_merge(containers):
    return type(containers)(e for c in containers for e in c)

def val_func_palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for v, _ in element})

def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_vsplit(grid, n):
    h, w = len(grid) // n, len(grid[0])
    offset = len(grid) % n != 0
    return tuple(val_func_crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))

def val_func_hsplit(grid, n):
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(val_func_crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))

def val_func_numcolors(element):
    return len(val_func_palette(element))

def mval_func_apply(function, container):
    return val_func_merge(val_func_apply(function, container))

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_argmax(container, compfunc):
    return max(container, key=compfunc)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_vsplit(I, 2)
    x2 = val_func_rbind(val_func_hsplit, 2)
    x3 = mval_func_apply(x2, x1)
    O = val_func_argmax(x3, val_func_numcolors)
    return [*map(list,O)]

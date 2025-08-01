def val_func_rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def val_func_rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def val_func_apply(function, container):
    return type(container)(function(e) for e in container)

def val_func_rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def val_func_order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def val_func_identity(x):
    return x

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_rot270(I)
    x2 = val_func_rbind(val_func_order, val_func_identity)
    x3 = val_func_apply(x2, x1)
    O = val_func_rot90(x3)
    return [*map(list,O)]

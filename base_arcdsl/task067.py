def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_hsplit(grid, n):
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(val_func_crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))

def val_func_first(container):
    return next(iter(container))

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_hsplit(I, 3)
    O = val_func_first(x1)
    return [*map(list,O)]

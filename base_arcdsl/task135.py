def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def val_func_tojvec(j):
    return (0, j)

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_tojvec(6)
    O = val_func_crop(I, x1, (3, 3))
    return [*map(list,O)]

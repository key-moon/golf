def val_func_crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def p(I):
    I=tuple(map(tuple,I))
    O = val_func_crop(I, (0, 0), (2, 2))
    return [*map(list,O)]

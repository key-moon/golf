def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def p(I):
    O = crop(I, (0, 0), (2, 2))
    return O

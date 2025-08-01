def crop(grid, start, dims):
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])

def tojvec(j):
    return (0, j)

def p(I):
    x1 = tojvec(6)
    O = crop(I, x1, (3, 3))
    return O

def rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def p(I):
    O = rot180(I)
    return O

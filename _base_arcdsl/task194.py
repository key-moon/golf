def vconcat(a, b):
    return a + b

def hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def rot270(grid):
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def rot180(grid):
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def p(I):
    x1 = rot90(I)
    x2 = rot180(I)
    x3 = rot270(I)
    x4 = hconcat(I, x1)
    x5 = hconcat(x3, x2)
    O = vconcat(x4, x5)
    return O

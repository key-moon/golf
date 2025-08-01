def switch(grid, a, b):
    return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in grid)

def p(I):
    O = switch(I, 5, 8)
    return O

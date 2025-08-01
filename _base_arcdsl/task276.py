def replace(grid, replacee, replacer):
    return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)

def p(I):
    O = replace(I, 6, 2)
    return O

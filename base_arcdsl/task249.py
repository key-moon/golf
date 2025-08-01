def hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def p(I):
    I=tuple(map(tuple,I))
    O = hconcat(I, I)
    return [*map(list,O)]

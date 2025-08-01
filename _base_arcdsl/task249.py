def hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def p(I):
    O = hconcat(I, I)
    return O

def canvas(value, dimensions):
    return tuple(tuple(value for j in range(dimensions[1])) for i in range(dimensions[0]))

def color(obj):
    return next(iter(obj))[0]

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

def p(I):
    x1 = mostcolor(I)
    O = canvas(x1, (3, 3))
    return O

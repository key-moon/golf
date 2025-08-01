def replace(grid, replacee, replacer):
    return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)

def color(obj):
    return next(iter(obj))[0]

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)

def p(I):
    I=tuple(map(tuple,I))
    x1 = leastcolor(I)
    x2 = replace(I, x1, 0)
    x3 = leastcolor(x2)
    O = replace(x2, x3, x1)
    return [*map(list,O)]

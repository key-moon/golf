def val_func_cellwise(a, b, fallback):
    h, w = len(a), len(a[0])
    resulting_grid = tuple()
    for i in range(h):
        row = tuple()
        for j in range(w):
            a_value = a[i][j]
            value = a_value if a_value == b[i][j] else fallback
            row = row + (value,)
        resulting_grid = resulting_grid + (row, )
    return resulting_grid

def val_func_vconcat(a, b):
    return a + b

def val_func_hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))

def val_func_vupscale(grid, factor):
    g = tuple()
    for row in grid:
        g = g + tuple(row for num in range(factor))
    return g

def val_func_hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(factor))
        g = g + (r,)
    return g

def p(I):
    I=tuple(map(tuple,I))
    x1 = val_func_hupscale(I, 3)
    x2 = val_func_vupscale(x1, 3)
    x3 = val_func_hconcat(I, I)
    x4 = val_func_hconcat(x3, I)
    x5 = val_func_vconcat(x4, x4)
    x6 = val_func_vconcat(x5, x4)
    O = val_func_cellwise(x2, x6, 0)
    return [*map(list,O)]

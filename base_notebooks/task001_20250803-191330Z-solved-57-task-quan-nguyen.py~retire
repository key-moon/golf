
def p(g):
    h, w = len(g), len(g[0])
    out = [[0] * (w * w) for _ in range(h * h)]
    for r_p, row_p in enumerate(g):
        for c_p, cell_p in enumerate(row_p):
            if cell_p != 0:
                for r_g, row_g in enumerate(g):
                    for c_g, cell_g in enumerate(row_g):
                        out[r_p*h + r_g][c_p*w + c_g] = cell_g
    return out

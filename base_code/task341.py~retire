def p(g):
    D = {}
    for i, r in enumerate(g):
        for j, v in enumerate(r):
            if v and v ^ 8:
                if v in D:
                    a, b, c, e = D[v]
                    D[v] = [min(a, i), max(b, i), min(c, j), max(e, j)]
                else:
                    D[v] = [i, i, j, j]
    (a, b, c, e), (f, h, d, k) = D.values()
    R = lambda A, B, C, D: range(max(A, C) + 1, min(B, D)) or range(B + 1, C) or range(D + 1, A)
    for i in R(a, b, f, h):
        for j in R(c, e, d, k):
            g[i][j] = 8
    return g

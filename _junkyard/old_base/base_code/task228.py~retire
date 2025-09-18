def p(g):
    D = {}
    for i, r in enumerate(g):
        for j, v in enumerate(r):
            if v:
                D[v] = D.get(v, 0) + 1
    B = max(D, key=D.get)
    r0 = c0 = 99
    r1 = c1 = 0
    for i, r in enumerate(g):
        for j, v in enumerate(r):
            if v == B:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    L = []
    for i, r in enumerate(g):
        for j, v in enumerate(r):
            if v and v != B:
                L += (i, j, v)
                g[i][j] = 0
    it = iter(L)
    for i, j, v in zip(it, it, it):
        x = r1 + 1 if i == r0 + 1 else r0 - 1
        y = c1 + 1 if j == c0 + 1 else c0 - 1
        g[x][y] = v
    return g

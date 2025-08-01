def p(g):
    n = len(g)
    p = [(i, j) for i in range(n) for j in range(n) if g[i][j]]
    (y1, x1), (y2, x2) = p
    c1, c2 = g[y1][x1], g[y2][x2]
    return [[2 if (i==y1 or j==x1) and (i==y2 or j==x2) else c1 if i==y1 or j==x1 else c2 if i==y2 or j==x2 else 0 for j in range(n)]for i in range(n)]

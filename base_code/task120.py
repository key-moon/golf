def p(g):
    for k in {v for r in g for v in r if v and v^8}:
        a = [i for i, r in enumerate(g) for v in r if v == k]
        b = [j for r in g for j, v in enumerate(r) if v == k]
        m, n = min(a), max(a); p, q = min(b), max(b)
        for i in range(m+1, n):
            for j in range(p+1, q):
                if g[i][j] == k: g[i][j] = 8
    return g

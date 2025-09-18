def p(g):
    n = len(g)
    if len({*sum(g, [])}) < 3:
        return [
            [g[i < n and i or 2*n-1-i][j < n and j or 2*n-1-j]
             for j in range(2*n)]
            for i in range(2*n)
        ]
    f = lambda x: [list(r) for r in zip(*x[::-1])]
    return [r + s for r, s in zip(g, f(g))] + \
           [r + s for r, s in zip(f(f(f(g))), f(f(g)))]

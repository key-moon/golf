def p(g):
    m = max(sum(g, []))
    o = [[0]*9 for _ in [1]*9]
    for i, r in enumerate(g):
        for j, v in enumerate(r):
            if v == m:
                for x in range(3):
                    o[3*i+x][3*j:3*j+3] = g[x]
    return o

def p(g):
    s = g[0][5]
    m = [(i,j) for i in range(5) for j in range(5) if g[i][j]]
    for a in range(3):
        for b in range(3):
            if a!=b:
                for i,j in m:
                    g[a*6+i][b*6+j] = s
    return g

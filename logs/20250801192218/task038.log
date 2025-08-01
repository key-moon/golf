def p(g):
    c = sum(g[i][j]==g[i][j+1]==g[i+1][j]==g[i+1][j+1]==1
            for i in range(8) for j in range(8))
    return [1]*c + [0]*(5-c)
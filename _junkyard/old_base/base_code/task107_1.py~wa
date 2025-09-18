def p(g):
    L = len(g)
    s = sum(g[-1][i] != g[-1][i-1] for i in range(1, L)) + 2
    return [[g[i//s][j//s] for j in range(L*s)] for i in range(L*s)]

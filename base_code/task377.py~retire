def p(g):
    # compress rows
    rr = [0] + [i for i in range(1, len(g)) if g[i] != g[i-1]]
    # compress cols via transposed grid
    z = list(zip(*g))
    cc = [0] + [j for j in range(1, len(z)) if z[j] != z[j-1]]
    # build result
    return [[g[i][j] for j in cc] for i in rr]

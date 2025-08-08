A=range
def p(g):r=[not any(x)for x in g];c=[not any(x)for x in zip(*g)];return[[2if r[i]or c[j]else g[i][j]for j in A(len(c))]for i in A(len(r))]
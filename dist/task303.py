def p(g):
 r=[not any(x)for x in g];c=[not any(x)for x in zip(*g)];return[[2 if r[i]or c[j]else g[i][j]for j in range(len(c))]for i in range(len(r))]
def p(g):
    i,j=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v^1])
    return[[v*(v^1)for v in r[min(j):max(j)+1]]for r in g[min(i):max(i)+1]]

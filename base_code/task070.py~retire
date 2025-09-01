def p(g):
    I,J=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==8])
    a,b=min(I),max(I);c,d=min(J),max(J)
    for i in range(a,b+1):
        for j in range(c,d+1):
            if g[i][j]^8: g[i][j]=3
    return g

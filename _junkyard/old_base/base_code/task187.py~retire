def p(g):
    h,w=len(g),len(g[0])
    s=[(i,j)for i in(0,h-1)for j in range(w)if g[i][j]==0]+[(i,j)for i in range(1,h-1)for j in(0,w-1)if g[i][j]==0]
    while s:
        i,j=s.pop()
        if g[i][j]==0:
            g[i][j]=3
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=ni<h and 0<=nj<w and g[ni][nj]==0: s+=[(ni,nj)]
    for i in range(h):
        for j in range(w):
            if g[i][j]==0: g[i][j]=2
    return g

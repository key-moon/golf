def p(g):
    a=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==8]
    (i1,j1),(i2,j2)=a
    di, dj = (i2-i1)//abs(i2-i1), (j2-j1)//abs(j2-j1)
    for x,y in ((i1,j1),(i2,j2)):
        for s in (1,-1):
            i,j=x,y
            while 1:
                i+=s*di; j+=s*dj
                if g[i][j]==2: break
                if g[i][j]==0: g[i][j]=3
    return g

def p(g):
    a,b=len(g),len(g[0])
    s=[(i,j)for i in(0,a-1)for j in range(b)]+[(i,j)for i in range(a)for j in(0,b-1)]
    while s:
        i,j=s.pop()
        if 0<=i<a and 0<=j<b and g[i][j]==0:
            g[i][j]=1; s+=((i+1,j),(i-1,j),(i,j+1),(i,j-1))
    for i in range(a):
        for j in range(b):
            if g[i][j]==0: g[i][j]=2
            elif g[i][j]==1: g[i][j]=0
    return g

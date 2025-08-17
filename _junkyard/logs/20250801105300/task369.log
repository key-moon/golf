def p(g):
    n,m=len(g),len(g[0])
    for i in range(n):
        for j in range(m):
            if not g[i][j]:
                q=[(i,j)];g[i][j]=1
                for x,y in q:
                    for u,v in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0<=u<n and 0<=v<m and not g[u][v]:
                            g[u][v]=1;q+=[(u,v)]
                k=4-len(q)
                for x,y in q:
                    g[x][y]=k
    return g
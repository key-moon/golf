def p(g):
    n=len(g);c=[g[i][i]for i in range((n+1)//2)]
    for i in range(n):
        for j in range(n):
            g[i][j]=c[(min(i,j,n-1-i,n-1-j)-1)%len(c)]
    return g

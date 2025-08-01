def p(g):
    n=len(g);a,b=min((i,j)for i in range(n)for j in range(n)if g[i][j]==1);c,d=min((i,j)for i in range(n)for j in range(n)if g[i][j]==2);i,j=a,b
    while i and j:i-=1;j-=1;g[i][j]=1
    i,j=c+1,d+1;while i<n-1 and j<n-1:i+=1;j+=1;g[i][j]=2
    return g

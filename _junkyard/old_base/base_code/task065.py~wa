def p(g):
    m=len(g)//2;i,j=next((i,j)for i in range(len(g))for j in range(len(g))if i-m and j-m and g[i][j]!=g[0][0])
    A=(m+1,0)[i<m];B=(m+1,0)[j<m]
    return [r[B:B+m] for r in g[A:A+m]]

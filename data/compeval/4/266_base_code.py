def p(g):
    r,c=next((i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==2)
    g[r][c]=0
    for dr,dc,v in(-1,-1,3),(-1,1,6),(1,1,7),(1,-1,8):
        i,j=r+dr,c+dc
        if 0<=i<len(g) and 0<=j<len(g[0]):
            g[i][j]=v
    return g

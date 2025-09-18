def p(g):
    m=r=c=0
    n=len(g)-4
    for i in range(n):
        for j in range(n):
            t=len({*g[i][j:j+5],*g[i+1][j:j+5],
                   *g[i+2][j:j+5],*g[i+3][j:j+5],
                   *g[i+4][j:j+5]})
            if t>m:m,r,c=t,i,j
    return [g[r+k][c:c+5][::-1] for k in range(5)]
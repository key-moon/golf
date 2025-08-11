def p(g):
    R,C=len(g),len(g[0])
    Z=[(i,j)for i in range(R)for j in range(C)if g[i][j]==0]
    for i,j in Z:
        if (i-1,j)in Z and (i+1,j)in Z and (i,j-1)in Z and (i,j+1)in Z:
            r0,c0=i,j;break
    bg=g[0][0]
    for i in range(R):
        for j in range(C):
            if g[i][j]!=bg and g[i][j]!=0:
                r1,c1,clr=i,j,g[i][j];break
        else:continue
        break
    dr,dc=r1-r0,c1-c0
    k=1
    while 1:
        rr,cc=r0+dr*k,c0+dc*k
        if not(0<=rr<R and 0<=cc<C):break
        g[rr][cc]=clr; k+=1
    return g

def p(g):
    r,c=len(g),len(g[0])
    r0=min(i for i in range(r) for j in range(c) if g[i][j]==5)
    r1=max(i for i in range(r) for j in range(c) if g[i][j]==5)
    c0=min(j for i in range(r) for j in range(c) if g[i][j]==5)
    c1=max(j for i in range(r) for j in range(c) if g[i][j]==5)
    for k in range(c0,c1+1):
        if g[r0][k]==0:
            i0,j0=r0,k
            break
    else:
        for k in range(c0,c1+1):
            if g[r1][k]==0:
                i0,j0=r1,k
                break
        else:
            for i in range(r0,r1+1):
                if g[i][c0]==0:
                    i0,j0=i,c0
                    break
            else:
                for i in range(r0,r1+1):
                    if g[i][c1]==0:
                        i0,j0=i,c1
                        break
    for i in range(r0+1,r1):
        for j in range(c0+1,c1):
            if g[i][j]==0:
                g[i][j]=8
    if i0==r0:
        for i in range(i0+1):
            g[i][j0]=8
    elif i0==r1:
        for i in range(i0,r):
            g[i][j0]=8
    elif j0==c0:
        for k in range(j0+1):
            g[i0][k]=8
    else:
        for k in range(j0,c):
            g[i0][k]=8
    return g

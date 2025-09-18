def p(g):
    H,W=len(g),len(g[0])
    # collect the two 8‐cells
    a=[(i,j)for i in range(H)for j in range(W)if g[i][j]==8]
    (i0,j0),(i1,j1)=a
    # unit step of the 8–line
    di, dj = (i1-i0)//abs(i1-i0), (j1-j0)//abs(j1-j0)
    # perpendicular direction for the 3–line
    pi, pj = -dj, di
    # step once along the 8–line into the zero‐region
    i2,j2 = i0+di, j0+dj
    # walk “backwards” along (pi,pj) until border of the zero‐patch
    while 0<=i2-pi<H and 0<=j2-pj<W and g[i2-pi][j2-pj]==0:
        i2,j2 = i2-pi, j2-pj
    # now march forwards stamping 3’s until we hit non‐zero
    while 0<=i2<H and 0<=j2<W and g[i2][j2]==0:
        g[i2][j2]=3
        i2,j2 = i2+pi, j2+pj
    return g

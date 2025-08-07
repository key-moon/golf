def p(g):
    R,C=len(g),len(g[0])
    # collect 5‐cells
    val_A=[(i,j)for i in range(R)for j in range(C)if g[i][j]==5]
    if not val_A: return g
    # bbox of the 5‐patch
    y0=min(i for i,j in val_A);x0=min(j for i,j in val_A)
    h=max(i for i,j in val_A)-y0
    # rotate 90° CW around the patch’s top‐left
    val_S=[(j-x0,h-(i-y0))for i,j in val_A]
    # find where to “drop” it: first row/col where 2 appears
    oy=min(i for i in range(R)for j in range(C)if g[i][j]==2)
    ox=min(j for j in range(C)for i in range(R)if g[i][j]==2)
    # paint 1’s under any 0’s
    for dy,dx in val_S:
        i,j=oy+dy,ox+dx
        if 0<=i<R and 0<=j<C and g[i][j]==0:
            g[i][j]=1
    return g

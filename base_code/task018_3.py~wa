def p(g):
    # find connected nonzero components
    val_r,val_c=len(g),len(g[0])
    val_v=[[0]*val_c for _ in g]
    val_C=[]
    for i in range(val_r):
        for j in range(val_c):
            if g[i][j] and not val_v[i][j]:
                # flood fill
                val_s=[(i,j)]
                val_v[i][j]=1
                for x,y in val_s:
                    for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
                        ii, jj = x+di, y+dj
                        if 0<=ii<val_r and 0<=jj<val_c and g[ii][jj] and not val_v[ii][jj]:
                            val_v[ii][jj]=1
                            val_s.append((ii,jj))
                val_C.append((val_s,[g[x][y] for x,y in val_s]))
    if len(val_C)!=2: return g
    (A,va),(B,vb)=val_C
    # compute top-left of each
    ax=min(x for x,y in A); ay=min(y for x,y in A)
    bx=min(x for x,y in B); by=min(y for x,y in B)
    # erase originals
    for x,y in A: g[x][y]=0
    for x,y in B: g[x][y]=0
    # paste A→B, B→A
    for (x,y),w in zip(A,va): g[bx+(x-ax)][by+(y-ay)]=w
    for (x,y),w in zip(B,vb): g[ax+(x- bx)][ay+(y- by)]=w
    return g

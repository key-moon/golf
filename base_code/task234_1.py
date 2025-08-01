def p(val_g):
    # find nonzero colors and their bounding‐boxes
    val_cs={v for r in val_g for v in r if v}
    val_b={}
    for v in val_cs:
        pts=[(i,j) for i,row in enumerate(val_g) for j,x in enumerate(row) if x==v]
        I=[p[0] for p in pts];J=[p[1] for p in pts]
        val_b[v]=[min(I),max(I),min(J),max(J)]
    # detect the full rectangle (bbox full) vs the L‐shape
    def full(c):
        y1,y2,x1,x2=val_b[c]
        return all(val_g[i][j]==c for i in range(y1,y2+1) for j in range(x1,x2+1))
    for v in val_cs:
        if full(v): val_rec=v
    val_L=(val_cs-{val_rec}).pop()
    # collect L‐cells that belong to a horizontal vs vertical run
    n,m=len(val_g),len(val_g[0])
    val_hc=[(i,j) for i in range(n) for j in range(m)
            if val_g[i][j]==val_L and ((j>0   and val_g[i][j-1]==val_L)
                                     or (j<m-1 and val_g[i][j+1]==val_L))]
    val_vc=[(i,j) for i in range(n) for j in range(m)
            if val_g[i][j]==val_L and ((i>0   and val_g[i-1][j]==val_L)
                                     or (i<n-1 and val_g[i+1][j]==val_L))]
    y1,y2,x1,x2=val_b[val_rec]
    y3,y4,x3,x4=val_b[val_L]
    # decide which branch to move and by how much
    if y2<y3:
        dr=(y2+1)-min(i for i,j in val_hc);dc=0;bc=val_hc
    elif y1>y4:
        dr=y1-1-max(i for i,j in val_hc);dc=0;bc=val_hc
    elif x2<x3:
        dc=(x2+1)-min(j for i,j in val_vc);dr=0;bc=val_vc
    else:
        dc=x1-1-max(j for i,j in val_vc);dr=0;bc=val_vc
    # build the result
    val_out=[row[:] for row in val_g]
    for i,j in bc: val_out[i][j]=0
    for i,j in bc: val_out[i+dr][j+dc]=val_L
    return val_out

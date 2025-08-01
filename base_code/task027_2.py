def p(g):
    val_h,val_w=len(g),len(g[0])
    val_v=lambda r,c:0<=r<val_h and 0<=c<val_w and g[r][c]>0
    while 1:
        val_a=[(r,c)
            for r in range(val_h) for c in range(val_w)
            if g[r][c]==0 and (
               val_v(r-1,c) and val_v(r,c-1) or
               val_v(r-1,c) and val_v(r,c+1) or
               val_v(r+1,c) and val_v(r,c-1) or
               val_v(r+1,c) and val_v(r,c+1)
            )]
        if not val_a: break
        for r,c in val_a: g[r][c]=2
    return g

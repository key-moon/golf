def p(g):
    # count all colours
    val_cnt={}
    for val_row in g:
        for v in val_row:
            val_cnt[v]=val_cnt.get(v,0)+1
    # the inner square's fill‐colour is the 2nd most common overall
    val_sq=sorted(val_cnt,key=lambda k:-val_cnt[k])[1]
    # collect coords of that colour
    val_sqPts=[(i,j)
        for i,row in enumerate(g)
        for j,v in enumerate(row)
        if v==val_sq]
    # bounding‐box of the square
    val_rs=[i for i,j in val_sqPts]
    val_cs=[j for i,j in val_sqPts]
    val_r0,val_r1=min(val_rs),max(val_rs)
    val_c0,val_c1=min(val_cs),max(val_cs)
    # the “shape” pixels inside (≠fill) are either the centre (once) or line‐pixels
    val_inner=[(i,j)
        for i,j in val_sqPts
        if val_r0<i<val_r1 and val_c0<j<val_c1 and g[i][j]!=val_sq]
    from collections import Counter
    val_subcnt=Counter(g[i][j] for i,j in val_inner)
    # centre is the colour occurring least, shape‐col the one occurring more
    val_centCol=min(val_subcnt,key=lambda c:val_subcnt[c])
    val_shpCol=max(val_subcnt,key=lambda c:val_subcnt[c])
    # find actual centre‐coords
    val_cent=[(i,j)
        for i,j in val_inner
        if g[i][j]==val_centCol][0]
    # rotation about (0,0)
    def val_rot(dy,dx): return dx,-dy
    # for each shape­pixel compute its vector to centre, rotate 90° three times
    # and stamp that pixel‐colour back
    for i,j in val_inner:
        if g[i][j]==val_shpCol:
            dy,dx=i-val_cent[0],j-val_cent[1]
            for _ in range(3):
                dy,dx=val_rot(dy,dx)
                g[val_cent[0]+dy][val_cent[1]+dx]=val_shpCol
    return g

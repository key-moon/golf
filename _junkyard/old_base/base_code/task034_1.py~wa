def p(g):
    H=len(g)
    W=len(g[0])
    # 1) find the 2×2 nonzero block
    cells=[]
    for i in range(H):
        for j in range(W):
            if g[i][j]!=0:
                cells.append((i,j,g[i][j]))
    # extract the 2×2 row/col extents
    rs=sorted({r for r,_,_ in cells})
    cs=sorted({c for _,c,_ in cells})
    r0,r1=rs[0],rs[-1]
    c0,c1=cs[0],cs[-1]
    # 2) find the oddball value O (occurs once)
    vals=[v for *_,v in cells]
    for v in set(vals):
        if vals.count(v)==1:
            O=v
        else:
            M=v
    C=max(O,M)
    # locate the position of the oddball and of its diagonal-opposite
    ro,co = next((r,c) for r,c,v in cells if v==O)
    # the opposite corner of the 2×2 is (r0+r1-ro, c0+c1-co)
    rop, cop = r0+r1-ro, c0+c1-co
    # direction vector from the opposite corner toward the oddball
    dr = (ro - rop) and ((ro-rop)//abs(ro-rop))
    dc = (co - cop) and ((co-cop)//abs(co-cop))
    # 3) walk from (rop,cop) in steps (dr,dc) until we leave the grid,
    #    and at each step paint the 3-wide stripe perpendicular to (dr,dc).
    #    Perp = (dc, -dr); width=3 => offsets -1,0,+1
    perp = (dc, -dr)
    out=[row[:] for row in g]
    r,c = rop, cop
    while 0<=r<H and 0<=c<W:
        for k in (-1,0,1):
            rr = r + perp[0]*k
            cc = c + perp[1]*k
            if 0<=rr<H and 0<=cc<W:
                out[rr][cc] = C
        r+=dr; c+=dc
    return out

def p(g):
    h,w=len(g),len(g[0])
    o=[r[:]for r in g]
    for v in{c for r in g for c in r} -{0}:
        pts=[(i,j)for i,row in enumerate(g)for j,c in enumerate(row)if c==v]
        # find the "ring" in pts, sorted clockwise
        # build a cycle of its border cells
        mnr=min(i for i,_ in pts);mnr=mnr
        mnc=min(j for _,j in pts)
        # get cycle order by angle around center
        cx=sum(i for i,_ in pts)/len(pts)
        cy=sum(j for _,j in pts)/len(pts)
        cyc=sorted(pts, key=lambda p: -__import__('math').atan2(p[1]-cy,p[0]-cx))
        L=len(cyc)
        for k,(i,j) in enumerate(cyc):
            i0,j0=cyc[(k+1)%L]
            o[i0][j0]=v
            o[i][j]=0
    return o
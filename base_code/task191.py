def p(g):
    # find bounding box of the “seed” shape (all non-zero cells)
    pts=[(i,j) for i in range(len(g)) for j in range(len(g[0])) if g[i][j]]
    y0,y1=min(i for i,j in pts),max(i for i,j in pts)
    x0,x1=min(j for i,j in pts),max(j for i,j in pts)
    P=[row[x0:x1+1] for row in g[y0:y1+1]]
    # find the first tile of value==4 in the seed
    anchors=[(i,j) for i in range(len(P)) for j in range(len(P[0])) if P[i][j]==4]
    ay,ax=anchors[0]
    H,W=len(P),len(P[0])
    # for every 4 in g outside the original seed, re-stamp P
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j]==4 and not (y0+ay==i and x0+ax==j):
                dy,dx=i-(y0+ay), j-(x0+ax)
                for ii in range(H):
                    for jj in range(W):
                        pv=P[ii][jj]
                        if pv:
                            g[dy+ii][dx+jj] = pv if pv==4 else 1
    return g

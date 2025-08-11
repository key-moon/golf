def p(g):
    val_n,val_m=len(g),len(g[0])
    # find full‐row stripes
    val_rr=[(i,g[i][0])
            for i in range(val_n)
            if g[i][0] and g[i].count(g[i][0])==val_m]
    # find full‐col stripes
    val_cc=[(j,g[0][j])
            for j in range(val_m)
            if g[0][j] and sum(g[i][j]==g[0][j] for i in range(val_n))==val_n]
    # start empty
    val_o=[[0]*val_m for _ in range(val_n)]
    # redraw stripes
    for i,c in val_rr: val_o[i]=[c]*val_m
    for j,c in val_cc:
        for i in range(val_n): val_o[i][j]=c
    # for every stray of a stripe‐color, plant one extra cell next to its stripe
    for i in range(val_n):
        for j in range(val_m):
            v=g[i][j]
            if not v: continue
            # horizontal stripes => extend vertically one step toward the stray
            for r,c in val_rr:
                if v==c and i!=r:
                    val_o[r+(-1 if i<r else 1)][j]=c
            # vertical stripes => extend one cell to the right
            for t,c in val_cc:
                if v==c and j!=t:
                    val_o[i][t+1]=c
    return val_o

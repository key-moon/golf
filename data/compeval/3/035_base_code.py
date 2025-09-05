def p(g):
    # find all rows/cols occupied by 8
    ys=[i for i,r in enumerate(g) for v in r if v==8]
    xs=[j for r in g for j,v in enumerate(r) if v==8]
    y0,y1=min(ys),max(ys); x0,x1=min(xs),max(xs)
    # for each guard cell, map it onto the rectangle edge
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v%8:  # non-zero and not 8
                if x<x0: g[y][x0]=v
                elif x>x1: g[y][x1]=v
                elif y<y0: g[y0][x]=v
                elif y>y1: g[y1][x]=v
    return g

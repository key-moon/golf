def p(g):
    h,w=len(g),len(g[0])
    for v in 1,2:
        r=min(i for i,row in enumerate(g) for x in row if x==v)
        c=min(j for row in g for j,x in enumerate(row) if x==v)
        for d in range(10):
            if r-d>=0 and c-d>=0:       g[r-d][c-d]=v
            if r+1+d<h and c+1+d<w:     g[r+1+d][c+1+d]=v
    return g

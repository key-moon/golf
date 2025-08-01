def p(g):
    h,w=len(g),len(g[0]);f=sum(g,[]);a=list({*f}-{0})
    x=[c for c in a if f.count(c)==1][0];y=[c for c in a if c!=x][0]
    for r in range(h):
        for c in range(w):
            if g[r][c]==x: break
     else
        break
    for dr,dc in[(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=r+dr<h and 0<=c+dc<w and g[r+dr][c+dc]==y:
            dr,dc=-dr,-dc
            break
    while 0<=r+dr<h and 0<=c+dc<w:
        r+=dr; c+=dc; g[r][c]=x
    return g

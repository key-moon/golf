def p(g):
    h,len0=len(g),len(g[0])
    # find cells of each color
    m={}
    for i,row in enumerate(g):
        for j,v in enumerate(row):
            if v:
                m.setdefault(v,[]).append((i,j))
    for c,cells in m.items():
        rs=[i for i,_ in cells]; cs=[j for _,j in cells]
        H=max(rs)-min(rs)+1; W=max(cs)-min(cs)+1
        for di,dj in ((-H,0),(H,0),(0,-W),(0,W)):
            ok=1
            for i,j in cells:
                ii, jj = i+di, j+dj
                if not(0<=ii<h and 0<=jj<len0 and (g[ii][jj]==0)):
                    ok=0; break
            if ok:
                for i,j in cells:
                    g[i+di][j+dj]=c
    return g

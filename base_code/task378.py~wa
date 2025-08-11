def p(g):
    h,w=len(g),len(g[0])
    o={}
    for i in range(h):
        for j in range(w):
            v=g[i][j]
            if v:o[v]=o.get(v,0)+1
    c=min(o,key=o.get)
    r1,c1=h,w; r2,c2=-1,-1
    for i in range(h):
        for j in range(w):
            if g[i][j]==c:
                if i<r1:r1=i
                if i>r2:r2=i
                if j<c1:c1=j
                if j>c2:c2=j
    for rr in(r1,r2):
        for cc in(c1,c2):
            dr=-1 if rr==r1 else 1
            dc=-1 if cc==c1 else 1
            i,j=rr+dr,cc+dc
            # skip empties and small‐shape cells
            while 0<=i<h and 0<=j<w and g[i][j] in (0,c):
                i+=dr; j+=dc
            # if we hit other color, start filling beyond it
            if 0<=i<h and 0<=j<w and g[i][j] not in (0,c):
                i+=dr; j+=dc
                while 0<=i<h and 0<=j<w:
                    if g[i][j]==0:g[i][j]=c
                    i+=dr; j+=dc
    return g

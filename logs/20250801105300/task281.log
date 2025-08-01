def p(g):
    m,n=len(g),len(g[0])
    a,c=m,n; b=d=0
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==8: e,f=i,j
            elif v:
                if i<a: a=i
                if i>b: b=i
                if j<c: c=j
                if j>d: d=j
    c1=g[a][c]
    for r in g:
        for v in r:
            if v and v!=8 and v!=c1:
                c2=v; break
     else
        break
    a,b,c,d = min(a,e),max(b,e),min(c,f),max(d,f)
    for i in range(a,b+1):
        for j in range(c,d+1):
            g[i][j] = c1 if i in (a,b) or j in (c,d) else c2
    return g
def p(g):
    from math import gcd
    H,W=len(g),len(g[0])
    P=[(i,j,v) for i,r in enumerate(g) for j,v in enumerate(r) if v]
    v=P[0][2]
    rs=sorted({i for i,_,_ in P})
    cs=sorted({j for _,j,_ in P})
    gr=0
    for a,b in zip(rs,rs[1:]): gr=gcd(gr,b-a)
    gc=0
    for a,b in zip(cs,cs[1:]): gc=gcd(gc,b-a)
    d=max(gr,gc)
    r0, c0 = rs[0], cs[0]
    for i in range(H):
        for j in range(W):
            g[i][j]=v if (i-r0)%d==0 or (j-c0)%d==0 else 0
    return g

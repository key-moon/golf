def p(g):
    C={c for R in g for c in R if c}
    b=[]
    for c in C:
        rs=[i for i,R in enumerate(g) for j,v in enumerate(R) if v==c]
        cs=[j for i,R in enumerate(g) for j,v in enumerate(R) if v==c]
        b.append((c,min(rs),max(rs),min(cs),max(cs)))
    # decide which box is the horizontal one
    b1,b2=sorted(b,key=lambda t:(t[4]-t[3])-(t[2]-t[1]),reverse=True)
    ch,r1,r2,c1,c2=b1
    cv,r3,r4,c3,c4=b2
    # fill the horizontal rectangle unchanged
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            g[i][j]=ch
    # build the “vertical” rectangle of width=hor­width and height=hor­height
    hh,ww=r2-r1+1,c2-c1+1
    for i in range(r2+1,r2+1+hh):
        for j in range(c3,c3+ww):
            g[i][j]=cv
    return g

def p(g):
    val_=[v for r in g for v in r if v][0]
    R_=sorted({i for i,row in enumerate(g) for v in row if v})
    C_=sorted({j for row in g for j,v in enumerate(row) if v})
    dr_=R_[1]-R_[0]; dc_=C_[1]-C_[0]
    r0,r1=R_[0],R_[-1]; c0,c1=C_[0],C_[-1]
    H,W=len(g),len(g[0])
    return [[val_ if ((r0<=r<=r1 and (c-c0)%dc_==0) or (c0<=c<=c1 and (r-r0)%dr_==0)) else 0
             for c in range(W)] for r in range(H)]

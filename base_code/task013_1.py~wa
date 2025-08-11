def p(g):
    H,W=len(g),len(g[0])
    # find the two nonzero seeds
    P=[(i,j,v) for i,row in enumerate(g) for j,v in enumerate(row) if v]
    (r1,c1,a),(r2,c2,b)=P
    dr,dc=abs(r2-r1),abs(c2-c1)
    # prepare output
    o=[[0]*W for _ in range(H)]
    if dc<=dr:
        D=dc*2
        for r in range(H):
            for c in range(W):
                if (c-c1)%D==0: o[r][c]=a
                if (c-c2)%D==0: o[r][c]=b
    else:
        D=dr*2
        for r in range(H):
            for c in range(W):
                if (r-r1)%D==0: o[r][c]=a
                if (r-r2)%D==D-b% D: o[r][c]=b  # (r−r2)%D==0, equivalently
                if (r-r2)%D==0: o[r][c]=b
    return o

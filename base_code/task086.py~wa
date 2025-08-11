def p(g):
    h,w=len(g),len(g[0])
    # find all nonzero cells and their colors
    nz=[(i,j) for i in range(h) for j in range(w) if g[i][j]]
    cs=[g[i][j] for i,j in nz]
    # outer color = most frequent, inner = the other
    a=max({*cs}, key=cs.count)
    b=next(x for x in { *cs } if x!=a)
    # scale coordinates by 2 to keep center integral
    pts=[(2*i,2*j,c) for (i,j),c in zip(nz,cs)]
    # center = average of inner‐color pts
    ib=[(i,j) for i,j,c in pts if c==b]
    cy=sum(i for i,j in ib)//len(ib)
    cx=sum(j for i,j in ib)//len(ib)
    # find max Manhattan radius in scaled grid
    R=max(abs(i-cy)+abs(j-cx) for i,j,c in pts)
    # build output
    out=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            d=abs(2*i-cy)+abs(2*j-cx)
            if d<=R:
                # alternate colors by parity of d//2
                out[i][j]=a if (d//2)%2==0 else b
    return out

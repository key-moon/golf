def p(g):
    h,w=len(g),len(g[0])
    # find zero‐rows
    zr=[i for i,row in enumerate(g) if row.count(0)==w]
    r0,r1=zr[0],zr[-1]
    # find zero‐cols
    zc=[j for j in range(w) if all(g[i][j]==0 for i in range(h))]
    c0,c1=zc[0],zc[-1]
    # colors in top vs bottom
    top={x for i in range(r0)   for x in g[i] if x}
    bot={x for i in range(r1+1,h) for x in g[i] if x}
    new=(bot-top).pop()
    # which side is it on?
    if any(g[i][j]==new for i in range(r1+1,h) for j in range(c0)):
        L,R=0,c0
    else:
        L,R=c1+1,w
    # slice out that quadrant
    return [row[L:R] for row in g[r1+1:h]]

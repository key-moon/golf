def p(g):
    n=len(g)
    # find the main‐diagonal color C (it appears once in every row of that diagonal)
    C=max({v for r in g for v in r if v}, key=lambda x:sum(row.count(x) for row in g))
    # collect all non-C cells (the "block")
    B=[(i,j) for i,row in enumerate(g) for j,v in enumerate(row) if v and v!=C]
    if not B: return g
    # bounding box of the block
    r0=min(i for i,j in B); r1=max(i for i,j in B)
    c0=min(j for i,j in B); c1=max(j for i,j in B)
    # clear grid
    for i in range(n):
        for j in range(n):
            g[i][j]=0
    # draw two slope-1 diagonals through the box corners
    for k in range(r1-r0+1):
        i=r0+k
        g[i][c0+k]=C
        g[i][c1-k]=C
    return g
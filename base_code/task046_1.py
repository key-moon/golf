def p(g):
    # drop any column containing a 5
    cols = list(zip(*g))
    cols = [c for c in cols if 5 not in c]
    h = [list(r) for r in zip(*cols)]
    H = len(h); W = len(h[0])
    # fill zeros by pulling from the nearest nonzero in the same column
    for i in range(H):
        for j in range(W):
            if h[i][j]==0:
                for di in (1,-1):
                    ni = i+di
                    if 0<=ni<H and h[ni][j]!=0:
                        h[i][j]=h[ni][j]
                        break
    return h

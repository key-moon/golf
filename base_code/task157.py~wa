def p(g):
    H,W = len(g), len(g[0])
    # collect all 5‐cells
    S = [(i,j) for i in range(H) for j in range(W) if g[i][j]==5]
    # shift S up until it first hits a 2‐cell
    for k in range(1,H):
        if any(0<=i-k<H and g[i-k][j]==2 for i,j in S):
            break
    # paint all overlapping 2's to 1
    for i,j in S:
        ii = i-k
        if 0<=ii<H and g[ii][j]==2:
            g[ii][j] = 1
    return g

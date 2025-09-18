def p(g):
    h,w = len(g), len(g[0])
    R = [r.count(8) for r in g]
    C = [sum(r[c]==8 for r in g) for c in range(w)]
    H = max(R) > max(C)
    B = [i for i in (range(h) if H else range(w)) if (H and R[i]) or ((not H) and C[i])]
    for r,c in [(i,j) for i in range(h) for j in range(w) if g[i][j]==2]:
        x = (r,c)[not H]
        b = min(B, key=lambda y:(abs(x-y), x-y))
        if H:
            for i in range(min(r,b), max(r,b)+1): g[i][c] = 2
            for i in range(b-1, b+2):
                for j in range(c-1, c+2):
                    if 0<=i<h and 0<=j<w: g[i][j] = 8
            g[b][c] = 2
        else:
            for j in range(min(c,b), max(c,b)+1): g[r][j] = 2
            for i in range(r-1, r+2):
                for j in range(b-1, b+2):
                    if 0<=i<h and 0<=j<w: g[i][j] = 8
            g[r][b] = 2
    return g

def p(g):
    n=len(g);m=len(g[0])
    # find grid‐line color
    for i in range(n):
        if g[i][0] and all(x==g[i][0] for x in g[i]):
            c=g[i][0]; break
    # row and col line indices
    L=[i for i in range(n) if all(x==c for x in g[i])]
    K=[j for j in range(m) if all(g[i][j]==c for i in range(n))]
    # map each cell to its row‐band and col‐band
    R=[-1]*n
    for i in range(len(L)-1):
        for r in range(L[i]+1, L[i+1]): R[r]=i
    C=[-1]*m
    for i in range(len(K)-1):
        for c0 in range(K[i]+1, K[i+1]): C[c0]=i
    # collect seeds (rband, cband, color)
    T=[(R[i],C[j],g[i][j])
       for i in range(n) for j in range(m)
       if g[i][j]!=0 and g[i][j]!=c]
    # fill along rows
    for ri in {t[0] for t in T}:
        vs=[t[2] for t in T if t[0]==ri]
        if len({*vs})==1:
            v=vs[0]
            cs=[t[1] for t in T if t[0]==ri]
            a,b=min(cs),max(cs)
            for i in range(n):
                if R[i]==ri:
                    for j in range(m):
                        if a<=C[j]<=b: g[i][j]=v
    # fill along cols
    for cj in {t[1] for t in T}:
        vs=[t[2] for t in T if t[1]==cj]
        if len({*vs})==1:
            v=vs[0]
            rs=[t[0] for t in T if t[1]==cj]
            a,b=min(rs),max(rs)
            for j in range(m):
                if C[j]==cj:
                    for i in range(n):
                        if a<=R[i]<=b: g[i][j]=v
    return g

def p(g):
    h,w=len(g),len(g[0])
    # pick the one nonzero color
    v=next(c for r in g for c in r if c)
    # row‐patterns
    R=[tuple(i for i,a in enumerate(r) if a==v) for r in g]
    # detect vertical tiling period
    p=0
    for k in range(1,h):
        if h>=2*k and all(R[i]==R[i+k] for i in range(h-k)):
            p=k; break
    # build a 10×w zero grid
    A=[[0]*w for _ in range(10)]
    # copy input
    for i in range(h):
        for j in R[i]:
            A[i][j]=v
    if p:
        # tile the row‐patterns
        for i in range(h,10):
            for j in R[i-p]:
                A[i][j]=v
    else:
        # snake extension
        # collect v‐cells
        S={(i,j) for i in range(h) for j in R[i]}
        # adjacency
        N={s:[] for s in S}
        for i,j in S:
            for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
                t=(i+di,j+dj)
                if t in S: N[(i,j)].append(t)
        # endpoints
        E=[s for s in S if len(N[s])==1]
        a,b=min(E),max(E)
        # find path a→b
        def dfs(u,p):
            if u==b: return [u]
            for q in N[u]:
                if q!=p:
                    r=dfs(q,u)
                    if r: return [u]+r
        P=dfs(a,None)
        # moves
        M=[(P[i+1][0]-P[i][0],P[i+1][1]-P[i][1]) for i in range(len(P)-1)]
        # minimal cycle
        for L in range(1,len(M)+1):
            if all(M[i]==M[i+L] for i in range(len(M)-L)):
                C=M[:L]; break
        idx=len(M)%len(C)
        cur=b
        # extend until border
        while True:
            dr,dc=C[idx]
            nr,nc=cur[0]+dr,cur[1]+dc
            if not(0<=nr<10 and 0<=nc<w): break
            A[nr][nc]=v
            cur=(nr,nc)
            idx=(idx+1)%len(C)
    return A

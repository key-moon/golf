def p(g):
    n=len(g)
    # compute tile‐count s = max block index so that g[i][j]!=0 ⇒ i+j<s
    s=0
    for i,row in enumerate(g):
        for j,v in enumerate(row):
            if v and i+j+1>s: s=i+j+1
    N=n*s
    R=[[0]*N for _ in range(N)]
    for i in range(N):
        bi, ai = divmod(i,n)
        for j in range(N):
            bj, aj = divmod(j,n)
            if bi+bj<s:
                R[i][j]=g[ai][aj]
    return R

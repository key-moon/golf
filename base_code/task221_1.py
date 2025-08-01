def p(g):
    n=3
    S=0
    while S<n and any(g[S][j] for j in range(n)): S+=1
    T=0
    while T<n and any(g[i][T] for i in range(n)): T+=1
    R=[[0]*(n*T) for _ in range(n*S)]
    for i in range(S):
        for j in range(T):
            for a in range(n):
                R[i*n+a][j*n:j*n+n]=g[a][:]
    return R

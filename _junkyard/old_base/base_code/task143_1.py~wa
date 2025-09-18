def p(g):
    A=[v for r in g for v in r if v]
    C=[x for x in set(A) if A.count(x)==7][0]
    P=[(i,j) for i in range(10) for j in range(10) if g[i][j]==C]
    r0,c0=min(i for i,_ in P),min(j for _,j in P)
    P=[(i-r0,j-c0)for i,j in P]
    for x in set(A)-{C}:
        Q=[(i,j)for i in range(10)for j in range(10)if g[i][j]==x]
        r1,c1=min(i for i,_ in Q),min(j for _,j in Q)
        for di,dj in P:
            i,j=r1+di,c1+dj
            if 0<=i<10<j<10 or 0<=j<10: g[i][j]=C
    return g

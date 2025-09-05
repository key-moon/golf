def p(g):
    A=[i for i,r in enumerate(g) for v in r if v==2];B=[j for r in g for j,v in enumerate(r) if v==2]
    a,b=min(A),max(A);c,d=min(B),max(B)
    n=[[0]*len(g[0])for _ in g]
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==2:n[i][j]=2
            if v==5:
                ii=a-1 if i<a else b+1 if i>b else i
                jj=c-1 if j<c else d+1 if j>d else j
                n[ii][jj]=5
    return n
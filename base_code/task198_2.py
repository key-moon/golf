def p(g):
    h,w=len(g),len(g[0])
    # sepVal = the nonzero that forms the grid lines
    sv=next(x for r in g for x in r if x)
    # heavy rows/cols are the separator lines
    Rs=[i for i in range(h) if g[i].count(sv)>w/2]
    Cs=[j for j in range(w) if sum(g[i][j]==sv for i in range(h))>h/2]
    # build the breakpoints: -1, all Rs, h  (and same for Cs)
    Rb=[-1]+Rs+[h]; Cb=[-1]+Cs+[w]
    nr, nc=len(Rb)-1, len(Cb)-1
    # union-find
    P=list(range(nr*nc))
    def f(x):
        while P[x]!=x: x=P[x]
        return x
    def u(a,b):
        a,b=f(a),f(b)
        if a!=b: P[a]=b
    # holes in horizontal separators link block(i,j)<->block(i+1,j)
    for r in Rs:
        i=sum(1 for x in Rs if x<r)
        for c in range(w):
            if g[r][c]==0 and c not in Cs:
                j=sum(1 for x in Cs if x<c)
                u(i*nc+j,(i+1)*nc+j)
    # holes in vertical separators link block(i,j)<->block(i,j+1)
    for c in Cs:
        j=sum(1 for x in Cs if x<c)
        for r in range(h):
            if g[r][c]==0 and r not in Rs:
                i=sum(1 for x in Rs if x<r)
                u(i*nc+j,i*nc+j+1)
    # count component sizes
    from collections import Counter
    cnt=Counter(f(i) for i in range(nr*nc))
    big=cnt.most_common(1)[0][0]
    # fill each block
    for i in range(nr):
        for j in range(nc):
            col=4 if f(i*nc+j)==big else 3
            for r in range(Rb[i]+1,Rb[i+1]):
                for c in range(Cb[j]+1,Cb[j+1]):
                    g[r][c]=col
    return g

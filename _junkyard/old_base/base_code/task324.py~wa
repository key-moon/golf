def p(g):
    h,w=len(g),len(g[0])
    # find background color b as most frequent
    b=max({c for R in g for c in R}, key=lambda x: sum(r.count(x) for r in g))
    # find seed points (roughly isolated non-b pixels)
    S=[(i,j,g[i][j]) for i in range(h) for j in range(w)
         if g[i][j]!=b and sum((0<=i+di<h and 0<=j+dj<w and g[i+di][j+dj]==g[i][j])
                               for di,dj in((1,0),(-1,0),(0,1),(0,-1)))<2]
    # propagate seeds diagonally, closest-wins
    for i in range(h):
        for j in range(w):
            if g[i][j]==b:
                bestd=10**9;val=None
                for r,c,v in S:
                    d=abs(i-r)
                    if d==abs(j-c)<bestd:
                        bestd=d; val=v
                if val is not None:
                    g[i][j]=val
    return g

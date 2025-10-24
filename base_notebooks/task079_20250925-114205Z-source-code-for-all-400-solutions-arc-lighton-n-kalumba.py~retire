def p(g):
    L=[];n=len(g)-2
    for i in range(n):
        for j in range(n):
            t=tuple(tuple(g[i+k][j:j+3])for k in(0,1,2))
            for q in {*sum(t,())}-{0}:
                m=tuple(tuple(x*(x==q)for x in r)for r in t)
                if min(map(sum,m))and min(map(sum,zip(*m))):L+=m,
    return [list(r)for r in max(L,key=L.count)]

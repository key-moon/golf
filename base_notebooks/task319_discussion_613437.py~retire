def p(g):
    b=max(sum(g,[]),key=sum(g,[]).count)
    a=[v for v in sum(g,[])if f"{b}, {v}, {b}"not in str(g+[*zip(*g)])][0]
    o=[[[b,a][v==a]for v in r[::2]]for r in g[::2]]
    m=[r*2for r in g*2]
    for i,r in enumerate(m):
        for j,v in enumerate(r):
            for k in{*sum(g,[])}:
                if[[[b,a][v==k]for v in r[j:j+len(o[0])]]for r in m[i:i+len(o)]]==o:
                    s=g
                    s=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i]
                    s=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i]
                    return s
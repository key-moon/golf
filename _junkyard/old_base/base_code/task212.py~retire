def p(g):
    n=len(g)
    b=next(i for i,r in enumerate(g) if r[0]==5)
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if 0<v<5:
                if v^1:
                    a=range(i+1,b) if i<b else range(b+1,i)
                else:
                    a=range(i)   if i<b else range(i+1,n)
                for k in a:
                    g[k][j]=v
    return g

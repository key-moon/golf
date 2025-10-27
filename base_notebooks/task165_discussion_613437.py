def p(g):
    *g,=zip(*g)
    for v in sum(g,()):
        X=[x for x,c in enumerate(g)if v in c]
        if X[-1]-X[0]==6:
            for x in X:r=g[x];j=20-r[::-1].index(v);g[x]=r[:j]+(max(r[j:]),)*(20-j)
    return[*zip(*g)]
def p(g):
    val_t=0
    if len({x for x in g[0] if x})>1:
        g=[list(r) for r in zip(*g)]; val_t=1
    val_l,val_w=len(g),len(g[0]); val_i=0
    while val_i<val_l:
        val_c=next(x for x in g[val_i] if x); val_j=val_i
        while val_j<val_l and set(g[val_j])-{0}=={val_c}: val_j+=1
        val_z={k for r in range(val_i,val_j) for k in range(val_w) if g[r][k]==0}
        for r in range(val_i,val_j):
            for k in val_z: g[r][k]=0
        val_i=val_j
    if val_t:
        g=[list(r) for r in zip(*g)]
    return g

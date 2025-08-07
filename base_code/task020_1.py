def p(g):
    val_a,len_g0,len_g1=len(g[0]),0,0
    val_a,val_b=len(g[0]),0
    for val_r in g:
        for val_j,val_v in enumerate(val_r):
            if val_v:
                val_a=min(val_a,val_j);val_b=max(val_b,val_j)
    val_m=val_a+val_b
    for val_i,val_r in enumerate(g):
        for val_j,val_v in enumerate(val_r):
            if val_v and not g[val_i][val_m-val_j]:
                g[val_i][val_m-val_j]=val_v
    return g

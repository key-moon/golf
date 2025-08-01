def p(val_g):
    val_a,len_g0,len_g1=len(val_g[0]),0,0
    val_a,val_b=len(val_g[0]),0
    for val_r in val_g:
        for val_j,val_v in enumerate(val_r):
            if val_v:
                val_a=min(val_a,val_j);val_b=max(val_b,val_j)
    val_m=val_a+val_b
    for val_i,val_r in enumerate(val_g):
        for val_j,val_v in enumerate(val_r):
            if val_v and not val_g[val_i][val_m-val_j]:
                val_g[val_i][val_m-val_j]=val_v
    return val_g

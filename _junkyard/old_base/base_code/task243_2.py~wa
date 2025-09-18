def p(g):
    for val_r in g:
        val_nz=[i for i,v in enumerate(val_r) if v]
        for val_i,val_j in zip(val_nz,val_nz[1:]):
            for val_k in range(val_i+1,val_j):
                if val_r[val_k]==0: val_r[val_k]=1
    return g

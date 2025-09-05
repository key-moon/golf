def p(g):
    # collect all original 8‐positions
    val_o=[(val_i,val_j) for val_i,val_r in enumerate(g) for val_j,val_v in enumerate(val_r) if val_v==8]
    # for each row with ≥2 originals, fill the min…max span
    for val_i in {val_i for val_i,_ in val_o}:
        val_L=[val_j for ii,val_j in val_o if ii==val_i]
        a,b=min(val_L),max(val_L)
        for val_j in range(a,b+1): g[val_i][val_j]=8
    # for each column with ≥2 originals, fill the min…max span
    for val_j in {val_j for _,val_j in val_o}:
        val_L=[val_i for val_i,jj in val_o if jj==val_j]
        a,b=min(val_L),max(val_L)
        for val_i in range(a,b+1): g[val_i][val_j]=8
    return g

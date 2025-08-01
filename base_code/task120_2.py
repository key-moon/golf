def p(val_g):
    val_a,val_b=len(val_g),len(val_g[0])
    for val_i in range(val_a):
        for val_j in range(val_b):
            val_c=val_g[val_i][val_j]
            if val_c:
                val_mi,val_Mi,val_mj,val_Mj=val_a,0,val_b,0
                for val_r in range(val_a):
                    for val_k in range(val_b):
                        if val_g[val_r][val_k]==val_c:
                            if val_r<val_mi: val_mi=val_r
                            if val_r>val_Mi: val_Mi=val_r
                            if val_k<val_mj: val_mj=val_k
                            if val_k>val_Mj: val_Mj=val_k
                if val_Mi-val_mi>1 and val_Mj-val_mj>1:
                    for val_r in range(val_mi+1,val_Mi):
                        for val_k in range(val_mj+1,val_Mj):
                            if val_g[val_r][val_k]==0:
                                val_g[val_r][val_k]=8
    return val_g

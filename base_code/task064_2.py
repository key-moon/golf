def p(g):
    val_d={}
    for val_rw in g:
        for val_v in val_rw:
            val_d[val_v]=val_d.get(val_v,0)+1
    val_o=sorted(val_d,key=val_d.get,reverse=1)
    val_r,val_p=val_o[1],val_o[2]
    val_z=[(val_i,val_j)
           for val_i,val_rw in enumerate(g)
           for val_j,val_v in enumerate(val_rw)
           if val_v==val_r]
    val_r0=min(val_i for val_i,val_j in val_z)
    val_r1=max(val_i for val_i,val_j in val_z)
    val_c0=min(val_j for val_i,val_j in val_z)
    val_c1=max(val_j for val_i,val_j in val_z)
    for val_i,val_rw in enumerate(g):
        for val_j,val_v in enumerate(val_rw):
            if val_v==val_p:
                if val_r0<=val_i<=val_r1:
                    for val_jj in range(min(val_j,val_c0),max(val_j,val_c1)+1):
                        g[val_i][val_jj]=val_p
                if val_c0<=val_j<=val_c1:
                    for val_ii in range(min(val_i,val_r0),max(val_i,val_r1)+1):
                        g[val_ii][val_j]=val_p
    return g

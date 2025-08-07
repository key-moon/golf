def p(g):
    val_n,val_m=len(g),len(g[0])
    val_f=[(val_i,val_j)
           for val_i in range(val_n)
           for val_j in range(val_m-4)
           if g[val_i][val_j:val_j+5]==[4]*5]
    val_r0,val_c0=val_f[0]; val_r1,val_c1=val_f[1]
    if not any(g[val_r0+val_d][val_c0+val_k]
               for val_d in(1,-1)
               for val_k in range(5)):
        val_r0,val_c0,val_r1,val_c1=val_r1,val_c1,val_r0,val_c0
    for val_d in(1,-1):
        for val_k in range(5):
            val_v=g[val_r0+val_d][val_c0+val_k]
            if val_v: g[val_r1-val_d][val_c1+val_k]=val_v
    return g

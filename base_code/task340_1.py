def p(g):
    val_t,val_b,val_l,val_r=g[0][1],g[-1][1],g[1][0],g[1][-1]
    for val_i in range(1,len(g)-1):
        for val_j in range(1,len(g[0])-1):
            val_v=g[val_i][val_j]
            if   val_v==val_t: g[1][val_j]=val_t
            elif val_v==val_b: g[-2][val_j]=val_b
            elif val_v==val_l: g[val_i][1]=val_l
            elif val_v==val_r: g[val_i][-2]=val_r
            g[val_i][val_j]=0
    return g

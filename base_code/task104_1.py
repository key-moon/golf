def p(g):
    val_C=max(map(max,g))
    val_x=[i for i,r in enumerate(g) for v in r if v==val_C]
    val_y=[j for r in g for j,v in enumerate(r) if v==val_C]
    val_m,val_M,val_n,val_N=min(val_x),max(val_x),min(val_y),max(val_y)
    val_L=[(val_m,val_M,val_n,val_N),(2-val_M,2-val_m,2-val_N,2-val_n)]
    val_h=[[0]*9 for _ in[0]*9]
    for val_a,val_b,val_c,val_d in val_L:
        for val_i in range(val_a*4,(val_b+1)*4):
            for val_j in range(val_c*4,(val_d+1)*4):
                val_h[val_i][val_j]=val_C
    return val_h

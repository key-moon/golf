def p(g):
    val_C=[]
    for val_y,val_r in enumerate(g):
        for val_x,val_v in enumerate(val_r):
            if val_v: val_C.append((val_x,val_y,val_v))
    for val_x,val_y,val_v in val_C:
        for val_dy in(-1,0,1):
            for val_dx in(-1,0,1):
                g[val_y+val_dy][val_x+val_dx]=val_v if val_dx|val_dy else 5
    val_X={}; val_Y={}
    for val_x,val_y,_ in val_C:
        val_X.setdefault(val_x,[]).append(val_y)
        val_Y.setdefault(val_y,[]).append(val_x)
    for val_k,val_L in val_X.items():
        if len(val_L)==2:
            val_a,val_b=sorted(val_L)
            for val_t in range(val_a+1,val_b):
                if (val_t-val_a)&1: g[val_t][val_k]=5
    for val_k,val_L in val_Y.items():
        if len(val_L)==2:
            val_a,val_b=sorted(val_L)
            for val_t in range(val_a+1,val_b):
                if (val_t-val_a)&1: g[val_k][val_t]=5
    return g

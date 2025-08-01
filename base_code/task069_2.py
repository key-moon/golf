def p(g):
    # dims
    val_a,val_b=len(g),len(g[0])
    # count nonzero cells to pick mask = most frequent nonzero
    val_d={}
    for val_i in range(val_a):
        for val_j in range(val_b):
            val_v=g[val_i][val_j]
            if val_v:
                val_d[val_v]=val_d.get(val_v,0)+1
    val_m=max(val_d,key=val_d.get)
    # collect the one non‐mask connected pattern (the stamp)
    val_S=[(val_i,val_j,g[val_i][val_j]) for val_i in range(val_a) for val_j in range(val_b) if (val_v:=g[val_i][val_j]) and val_v!=val_m]
    val_x=min(val_i for val_i,val_j,val_v in val_S)
    val_y=min(val_j for val_i,val_j,val_v in val_S)
    val_P=[(val_i-val_x,val_j-val_y,val_v) for val_i,val_j,val_v in val_S]
    # prepare empty output
    val_R=[[0]*val_b for _ in range(val_a)]
    # slide stamp over grid; where it exactly covers the mask, paint it
    for val_I in range(val_a):
        for val_J in range(val_b):
            if all(0<=val_I+di<val_a and 0<=val_J+dj<val_b and g[val_I+di][val_J+dj]==val_m for di,dj,_ in val_P):
                for di,dj,c in val_P:
                    val_R[val_I+di][val_J+dj]=c
    return val_R

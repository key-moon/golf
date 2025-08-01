def p(g):
    val_R=len(g)//3+1;val_C=len(g[0])//3+1
    val_b=[[0]*val_C for _ in range(val_R)]
    for val_i in range(val_R):
        for val_j in range(val_C):
            for val_u in (0,1):
                for val_v in (0,1):
                    val_x=g[3*val_i+val_u][3*val_j+val_v]
                    if val_x: val_b[val_i][val_j]=val_x
    for val_i in range(val_R):
        for val_j in range(val_C):
            val_x=val_b[val_i][val_j]
            if val_x:
                for val_k in range(val_C):
                    if val_x: val_b[val_i][val_k] = val_x
                for val_k in range(val_R):
                    if val_x: val_b[val_k][val_j] = val_x
    for val_i in range(val_R):
        for val_j in range(val_C):
            val_x=val_b[val_i][val_j]
            if val_x:
                for val_u in (0,1):
                    for val_v in (0,1):
                        g[3*val_i+val_u][3*val_j+val_v]=val_x
    return g

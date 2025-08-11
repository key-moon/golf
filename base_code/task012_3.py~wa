def p(g):
    val_r,val_c=len(g),len(g[0]);val_h=[[0]*val_c for _ in g]
    for val_i in range(1,val_r-1):
        for val_j in range(1,val_c-1):
            val_t=g[val_i][val_j]
            if val_t and g[val_i-1][val_j]==g[val_i+1][val_j]==g[val_i][val_j-1]==g[val_i][val_j+1]:
                val_w=g[val_i-1][val_j]
                for val_dx in range(-2,3):
                    for val_dy in range(-2,3):
                        if val_dx|val_dy and (val_dx*val_dy==0 or abs(val_dx)==abs(val_dy)):
                            val_h[val_i+val_dx][val_j+val_dy] = val_t if abs(val_dx)==abs(val_dy) else val_w
    return val_h

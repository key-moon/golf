def p(g):
    val_m={3:6,8:4,2:1}
    for val_i,val_row in enumerate(g):
        for val_j,val_v in enumerate(val_row):
            if val_v in val_m:
                for val_di in(-1,0,1):
                    for val_dj in(-1,0,1):
                        if val_di or val_dj:
                            g[val_i+val_di][val_j+val_dj]=val_m[val_v]
    return g

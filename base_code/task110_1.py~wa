def p(g):
    val_h,val_w=len(g),len(g[0])
    val_ds=((1,0),(0,1),(-1,0),(0,-1))
    while any(0 in r for r in g):
        for val_y in range(val_h):
            for val_x in range(val_w):
                if not g[val_y][val_x]:
                    for val_dy,val_dx in val_ds:
                        val_i,val_j=val_y+val_dy,val_x+val_dx
                        if 0<=val_i<val_h and 0<=val_j<val_w and g[val_i][val_j]:
                            g[val_y][val_x]=g[val_i][val_j]
                            break
    return g

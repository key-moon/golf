def p(g):
    val_H,val_W=len(g),len(g[0])
    val_D=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    for val_i in range(val_H):
        for val_j in range(val_W):
            if g[val_i][val_j]==3:
                for val_dx,val_dy in val_D:
                    val_ni,val_nj=val_i+val_dx,val_j+val_dy
                    if 0<=val_ni<val_H and 0<=val_nj<val_W and g[val_ni][val_nj]==3:
                        for val_sgn in(-1,1):
                            val_r,val_c=val_i-val_dx*val_sgn,val_j-val_dy*val_sgn
                            if 0<=val_r<val_H and 0<=val_c<val_W and g[val_r][val_c]==0:
                                g[val_r][val_c]=8
    return g

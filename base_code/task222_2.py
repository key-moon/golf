def p(g):
    val_h=len(g);val_w=len(g[0]);val_b=0
    for val_i in range(val_h):
        for val_j in range(val_w):
            val_c=g[val_i][val_j]
            if val_c:
                for val_i2 in range(val_i,val_h):
                    for val_j2 in range(val_j,val_w):
                        val_a=(val_i2-val_i+1)*(val_j2-val_j+1)
                        if val_a>val_b and all(g[x][y]==val_c
                               for x in range(val_i,val_i2+1)
                               for y in range(val_j,val_j2+1)):
                            val_b=val_a
                            val_ti,val_tj,val_bi,val_bj,val_cl=val_i,val_j,val_i2,val_j2,val_c
    res=[[0]*val_w for _ in range(val_h)]
    for x in range(val_ti,val_bi+1):
        for y in range(val_tj,val_bj+1):
            res[x][y]=val_cl
    return res

def p(g):
    val_h,val_w=len(g),len(g[0]);val_r=g[0]
    val_w0=next(val_d for val_d in range(1,val_w)
                if all(val_r[val_j] and val_r[val_j]==val_r[val_j+val_d]
                       for val_j in range(val_w-val_d)))
    val_c=[g[val_i][0] for val_i in range(val_h)]
    val_h0=next(val_d for val_d in range(1,val_h)
                if all(val_c[val_i] and val_c[val_i]==val_c[val_i+val_d]
                       for val_i in range(val_h-val_d)))
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==0:
                g[val_i][val_j]=g[val_i%val_h0][val_j%val_w0]
    return g

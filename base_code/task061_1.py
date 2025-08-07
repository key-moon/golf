def p(g):
    val_m=len(g);_=0
    for val_d in range(1,val_m+1):
        if val_m%val_d: continue
        for val_a in range(val_m//val_d):
            for val_b in range(val_m//val_d):
                if all(g[val_a*val_d+val_k][val_b*val_d+val_l]
                       for val_k in range(val_d)
                       for val_l in range(val_d)):
                    val_t=[r[val_b*val_d:val_b*val_d+val_d]
                           for r in g[val_a*val_d:val_a*val_d+val_d]]
                    _=1
                    break
            if _: break
        if _: break
    for val_i in range(val_m):
        for val_j in range(val_m):
            if not g[val_i][val_j]:
                g[val_i][val_j]=val_t[val_i%val_d][val_j%val_d]
    return g

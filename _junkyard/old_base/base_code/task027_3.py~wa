def p(g):
    val_h,val_w=len(g),len(g[0])
    val_s=[(i,j)for i in(0,val_h-1)for j in range(val_w)]+[(i,j)for i in range(val_h)for j in(0,val_w-1)]
    for val_i,val_j in val_s:
        if g[val_i][val_j]==0:g[val_i][val_j]=-1
    while val_s:
        val_i,val_j=val_s.pop()
        for val_a,val_b in((val_i-1,val_j),(val_i+1,val_j),(val_i,val_j-1),(val_i,val_j+1)):
            if 0<=val_a<val_h and 0<=val_b<val_w and g[val_a][val_b]==0:
                g[val_a][val_b]=-1;val_s.append((val_a,val_b))
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==0:   g[val_i][val_j]=2
            elif g[val_i][val_j]<0:  g[val_i][val_j]=0
    return g

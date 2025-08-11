def p(g):
    val_h,val_w=len(g),len(g[0])
    val_s=[(val_i,val_j)
           for val_i in range(val_h)
           for val_j in range(val_w)
           if val_i*val_j*(val_h-1-val_i)*(val_w-1-val_j)==0
           and g[val_i][val_j]==0]
    while val_s:
        val_i,val_j=val_s.pop()
        if g[val_i][val_j]==0:
            g[val_i][val_j]=-1
            val_s+=((val_i+1,val_j),(val_i-1,val_j),
                    (val_i,val_j+1),(val_i,val_j-1))
    for val_i in range(val_h):
        for val_j in range(val_w):
            if   g[val_i][val_j]==0:  g[val_i][val_j]=2
            elif g[val_i][val_j]<0:   g[val_i][val_j]=0
    return g

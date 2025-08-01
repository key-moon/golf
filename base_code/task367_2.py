def p(g):
    val_h=[val_r[:]for val_r in g]
    val_R,val_C=len(g),len(g[0])
    val_s=[(val_i,val_j)
           for val_i in(0,val_R-1)
           for val_j in range(val_C)
           if g[val_i][val_j]!=5]+[
           (val_i,val_j)
           for val_i in range(val_R)
           for val_j in(0,val_C-1)
           if g[val_i][val_j]!=5]
    val_v=set()
    while val_s:
        val_i,val_j=val_s.pop()
        if(val_i,val_j) in val_v: continue
        val_v.add((val_i,val_j))
        for val_di,val_dj in((1,0),(-1,0),(0,1),(0,-1)):
            val_x,val_y=val_i+val_di,val_j+val_dj
            if 0<=val_x<val_R and 0<=val_y<val_C \
               and g[val_x][val_y]!=5 \
               and (val_x,val_y) not in val_v:
                val_s.append((val_x,val_y))
    for val_i in range(val_R):
        for val_j in range(val_C):
            if g[val_i][val_j]==0 \
               and (val_i,val_j) not in val_v:
                val_h[val_i][val_j]=4
    return val_h

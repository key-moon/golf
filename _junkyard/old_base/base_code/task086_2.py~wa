def p(g):
    val_h,val_w=len(g),len(g[0])
    val_c=[(val_i,val_j)
           for val_i in range(val_h)
           for val_j in range(val_w)
           if g[val_i][val_j]]
    while val_c:
        val_i,val_j=val_c[0]; val_s=[(val_i,val_j)]; val_R=[]
        while val_s:
            val_i,val_j=val_s.pop()
            if (val_i,val_j) in val_c:
                val_c.remove((val_i,val_j)); val_R.append((val_i,val_j))
                val_s+=[(val_i-1,val_j),(val_i+1,val_j),
                        (val_i,val_j-1),(val_i,val_j+1)]
        xs,ys=zip(*val_R)
        val_r0,val_r1=min(xs),max(xs)
        val_c0,val_c1=min(ys),max(ys)
        val_B=g[val_r0][val_c0]
        val_I=g[val_r0+1][val_c0+1]
        for val_x in range(val_r0-1,val_r1+2):
            for val_y in range(val_c0-1,val_c1+2):
                if 0<=val_x<val_h and 0<=val_y<val_w:
                    g[val_x][val_y]=val_I
        for val_x in (val_r0-1,val_r1+1):
            for val_y in range(val_c0-1,val_c1+2):
                if 0<=val_x<val_h and 0<=val_y<val_w:
                    g[val_x][val_y]=val_B
        for val_x in range(val_r0-1,val_r1+2):
            for val_y in (val_c0-1,val_c1+1):
                if 0<=val_x<val_h and 0<=val_y<val_w:
                    g[val_x][val_y]=val_B
    return g

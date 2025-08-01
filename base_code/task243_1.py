def p(g):
    val_r,val_c=len(g),len(g[0])
    val_v=set();val_b=()
    for val_i in range(val_r):
        for val_j in range(val_c):
            if not g[val_i][val_j] and (val_i,val_j) not in val_v:
                val_q=[(val_i,val_j)]
                val_s={(val_i,val_j)}
                val_v.add((val_i,val_j))
                for val_x,val_y in val_q:
                    for val_dx,val_dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        val_nx,val_ny=val_x+val_dx,val_y+val_dy
                        if 0<=val_nx<val_r and 0<=val_ny<val_c \
                           and not g[val_nx][val_ny] \
                           and (val_nx,val_ny) not in val_v:
                            val_v.add((val_nx,val_ny))
                            val_s.add((val_nx,val_ny))
                            val_q.append((val_nx,val_ny))
                if len(val_s)>len(val_b):
                    val_b=val_s
    for val_x,val_y in val_b:
        g[val_x][val_y]=1
    return g

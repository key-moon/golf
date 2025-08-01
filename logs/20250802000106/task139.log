def p(g):
    val_v=set();val_n=len(g);val_m=len(g[0]);val_t=((1,0),(-1,0),(0,1),(0,-1))
    for val_i in range(val_n):
        for val_j in range(val_m):
            if g[val_i][val_j]==4 and (val_i,val_j) not in val_v:
                val_l=[(val_i,val_j)];val_v.add((val_i,val_j))
                for val_x,val_y in val_l:
                    for val_dx,val_dy in val_t:
                        val_u=(val_x+val_dx,val_y+val_dy)
                        if val_u not in val_v and 0<=val_u[0]<val_n and 0<=val_u[1]<val_m and g[val_u[0]][val_u[1]]==4:
                            val_v.add(val_u);val_l.append(val_u)
                val_a=min(_[0] for _ in val_l);val_b=max(_[0] for _ in val_l)
                val_c=min(_[1] for _ in val_l);val_d=max(_[1] for _ in val_l)
                for val_x in range(val_a,val_b+1):
                    for val_y in range(val_c,val_d+1):
                        if g[val_x][val_y]==0:g[val_x][val_y]=7
    return g
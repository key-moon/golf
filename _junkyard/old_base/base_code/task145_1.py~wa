def p(g):
    val_h,val_w=len(g),len(g[0]);val_D=[(1,0),(-1,0),(0,1),(0,-1)]
    for val_i in range(val_h):
        for val_j in range(val_w):
            if g[val_i][val_j]==2:
                val_b=[d for d in val_D
                       if 0<=val_i+d[0]<val_h and 0<=val_j+d[1]<val_w
                       and g[val_i+d[0]][val_j+d[1]]==2]
                for val_x in range(len(val_b)):
                    for val_y in range(val_x+1,len(val_b)):
                        val_u,val_v=val_b[val_x],val_b[val_y]
                        if val_u[0]*val_v[0]+val_u[1]*val_v[1]==0:
                            for val_s,val_c in [
                                ((-val_u[0]-val_v[0],-val_u[1]-val_v[1]),1),
                                (( val_u[0]+val_v[0], val_u[1]+val_v[1]),8)
                            ]:
                                val_X,val_Y=val_i+val_s[0],val_j+val_s[1]
                                if 0<=val_X<val_h and 0<=val_Y<val_w and g[val_X][val_Y]==0:
                                    val_S=[(val_X,val_Y)];g[val_X][val_Y]=val_c
                                    while val_S:
                                        val_a,val_b0=val_S.pop()
                                        for val_dx,val_dy in val_D:
                                            val_A,val_B=val_a+val_dx,val_b0+val_dy
                                            if 0<=val_A<val_h and 0<=val_B<val_w and g[val_A][val_B]==0:
                                                g[val_A][val_B]=val_c
                                                val_S.append((val_A,val_B))
    return g

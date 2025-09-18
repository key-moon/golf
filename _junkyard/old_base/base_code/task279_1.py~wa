def p(g):
    val_R=len(g);val_C=len(g[0])
    val_V=[[0]*val_C for _ in range(val_R)]
    val_B=[]
    for val_i in range(val_R):
        for val_j in range(val_C):
            if g[val_i][val_j]==1 and not val_V[val_i][val_j]:
                val_S=[(val_i,val_j)];val_V[val_i][val_j]=1
                for val_x,val_y in val_S:
                    for val_dx,val_dy in((1,0),(-1,0),(0,1),(0,-1)):
                        val_nx=val_x+val_dx;val_ny=val_y+val_dy
                        if 0<=val_nx<val_R and 0<=val_ny<val_C and g[val_nx][val_ny]==1 and not val_V[val_nx][val_ny]:
                            val_V[val_nx][val_ny]=1;val_S.append((val_nx,val_ny))
                if len(val_S)>len(val_B): val_B=val_S
    for val_x,val_y in val_B: g[val_x][val_y]=8
    return g

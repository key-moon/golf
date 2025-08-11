def p(g):
    val_h,val_len=len(g),len(g[0]);val_v=[[0]*val_len for _ in g];val_C=[]
    for val_i in range(val_h):
        for val_j in range(val_len):
            if g[val_i][val_j]==3 and not val_v[val_i][val_j]:
                val_q=[(val_i,val_j)];val_v[val_i][val_j]=1
                for val_x,val_y in val_q:
                    for val_dx,val_dy in((1,0),(-1,0),(0,1),(0,-1)):
                        val_nx,val_ny=val_x+val_dx,val_y+val_dy
                        if 0<=val_nx<val_h and 0<=val_ny<val_len and g[val_nx][val_ny]==3 and not val_v[val_nx][val_ny]:
                            val_v[val_nx][val_ny]=1;val_q.append((val_nx,val_ny))
                val_C.append(val_q)
    val_sz=sorted({len(q) for q in val_C});val_M={s:c for s,c in zip(val_sz,(1,2,6))}
    for val_q in val_C:
        for val_x,val_y in val_q: g[val_x][val_y]=val_M[len(val_q)]
    return g

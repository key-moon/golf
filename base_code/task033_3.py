def p(g):
    val_n=len(g);val_s=val_n//3;val_d=val_s+1;val_c=g[val_s][val_s]
    val_H=[[any(g[i*val_d+u][j*val_d+v]for u in range(val_s)for v in range(val_s))
            for j in range(3)]for i in range(3)]
    for i in range(3):
        for j in range(3):
            if not val_H[i][j]:
                row_idxs=[k for k in range(3) if val_H[i][k]]
                if len(row_idxs)>1:
                    a,b=row_idxs[0],row_idxs[1]
                    for u in range(val_s):
                        for v in range(val_s):
                            if g[i*val_d+u][a*val_d+v] or g[i*val_d+u][b*val_d+v]:
                                g[i*val_d+u][j*val_d+v]=val_c
                else:
                    col_idxs=[k for k in range(3) if val_H[k][j]]
                    a,b=col_idxs[0],col_idxs[1]
                    for u in range(val_s):
                        for v in range(val_s):
                            if g[a*val_d+u][j*val_d+v] or g[b*val_d+u][j*val_d+v]:
                                g[i*val_d+u][j*val_d+v]=val_c
    return g

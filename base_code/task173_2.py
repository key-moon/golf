def p(g):
    val_m,val_n=len(g),len(g[0])
    val_D,val_A={},{}
    # 1) find prototypes: any v with >1 nonzero neighbour
    for val_i in range(val_m):
        for val_j in range(val_n):
            v=g[val_i][val_j]
            if v and v not in val_D:
                val_o=[]
                for val_di,val_dj in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    x,y=val_i+val_di,val_j+val_dj
                    if 0<=x<val_m and 0<=y<val_n and g[x][y]:
                        val_o.append((val_di,val_dj))
                if len(val_o)>1:
                    val_D[v]=val_o
                    # take the first neighbour’s colour as the “arm” colour
                    val_A[v]=g[val_i+val_o[0][0]][val_j+val_o[0][1]]
    # 2) replay each prototype at every centre cell of that colour
    for val_i in range(val_m):
        for val_j in range(val_n):
            v=g[val_i][val_j]
            if v in val_D:
                for val_di,val_dj in val_D[v]:
                    g[val_i+val_di][val_j+val_dj]=val_A[v]
    return g

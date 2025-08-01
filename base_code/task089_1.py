def p(g):
    val_n,len0=len(g),len(g[0])
    val_S={(i,j) for i in range(val_n) for j in range(len0) if g[i][j]}
    while val_S:
        val_comp=[val_S.pop()]
        for val_i in val_comp:
            x,y=val_i
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                nb=(x+dx,y+dy)
                if nb in val_S:
                    val_S.remove(nb)
                    val_comp.append(nb)
        if len(val_comp)>1:
            val_cnt={}
            for x,y in val_comp:
                val_cnt[g[x][y]]=val_cnt.get(g[x][y],0)+1
            for val_c,val_v in val_cnt.items():
                if val_v==1: break
            # pivot = the one cell of color val_c
            val_px,val_py=[(x,y) for x,y in val_comp if g[x][y]==val_c][0]
            val_shape=[(x-val_px,y-val_py,g[x][y]) for x,y in val_comp]
            for i in range(val_n):
                for j in range(len0):
                    if g[i][j]==val_c and (i,j)!=(val_px,val_py):
                        for dx,dy,v in val_shape:
                            g[i+dx][j+dy]=v
    return g

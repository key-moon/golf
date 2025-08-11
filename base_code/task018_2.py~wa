def p(g):
    val_H,val_W=len(g),len(g[0]);val_O=[[0]*val_W for _ in g];val_M=[[0]*val_W for _ in g]
    for val_i in range(val_H):
        for val_j in range(val_W):
            if g[val_i][val_j] and not val_M[val_i][val_j]:
                val_Q=[(val_i,val_j)];val_M[val_i][val_j]=1
                for _ in val_Q:
                    val_r,val_c=_
                    for val_dr,val_dc in((1,0),(-1,0),(0,1),(0,-1)):
                        val_nr,val_nc=val_r+val_dr,val_c+val_dc
                        if 0<=val_nr<val_H and 0<=val_nc<val_W and g[val_nr][val_nc] and not val_M[val_nr][val_nc]:
                            val_M[val_nr][val_nc]=1;val_Q.append((val_nr,val_nc))
                val_rs,val_cs=zip(*val_Q);val_rc,val_cc=(min(val_rs)+max(val_rs))//2,(min(val_cs)+max(val_cs))//2
                for val_r,val_c in val_Q:
                    val_dr,val_dc=val_r-val_rc,val_c-val_cc
                    val_O[(val_H-1-val_rc)-val_dc][val_cc+val_dr]=g[val_r][val_c]
    return val_O

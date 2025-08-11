def p(g):
    val_H,val_W=len(g),len(g[0])
    val_R=[i for i,a in enumerate(g)if min(a)==8]
    val_C=[j for j in range(val_W)if min(g[i][j]for i in range(val_H))==8]
    val_T=[(i,j)for i,a in enumerate(g)for j,v in enumerate(a)if v==2]
    for val_r,val_c in val_T:
        val_sr=min(val_R,key=lambda x:abs(x-val_r))if val_R else 0
        val_sc=min(val_C,key=lambda x:abs(x-val_c))if val_C else 0
        if val_R and (not val_C or abs(val_r-val_sr)<=abs(val_c-val_sc)):
            # connect vertically to horizontal stripe at row val_sr
            for val_i in range(min(val_r,val_sr),max(val_r,val_sr)+1):g[val_i][val_c]=2
            for val_i in range(val_c-1,val_c+2):
                for val_j in(val_sr-1,val_sr,val_sr+1):g[val_j][val_i]=8
            g[val_sr][val_c]=2
        else:
            # connect horizontally to vertical stripe at col val_sc
            for val_i in range(min(val_c,val_sc),max(val_c,val_sc)+1):g[val_r][val_i]=2
            for val_i in range(val_sc-1,val_sc+2):
                for val_j in(val_r-1,val_r,val_r+1):g[val_j][val_i]=8
            g[val_r][val_sc]=2
    return g

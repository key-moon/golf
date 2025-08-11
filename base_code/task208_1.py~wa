def p(g):
    val_h,val_w=len(g),len(g[0]);val_cnt={}
    for val_r in g:
        for val_v in val_r:val_cnt[val_v]=val_cnt.get(val_v,0)+1
    val_c=min(val_cnt,key=val_cnt.get)
    for val_i,val_r in enumerate(g):
        for val_j,val_v in enumerate(val_r):
            if val_v==val_c:g[val_h-1-val_i][val_w-1-val_j]=val_c
    return g

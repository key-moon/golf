def p(g):
    val_r=g[-1]
    val_c=min({*val_r}-{0},key=val_r.count)
    val_s=[i for i,v in enumerate(val_r) if v==val_c]
    val_a,val_b=val_s[0],val_s[-1]
    val_t=len(g)-2; val_w=len(g[0])
    for val_i in range(1,len(g)):
        val_y=val_t-val_i
        if val_y<0: break
        for val_x in (val_a-val_i,val_b+val_i):
            if 0<=val_x<val_w and g[val_y][val_x]==0:
                g[val_y][val_x]=val_c
    return g

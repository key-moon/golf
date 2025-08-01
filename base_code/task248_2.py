def p(g):
    val_m=len(g[0]);val_x=g[-1].index(1);val_d=1
    val_h=[[0]*val_m for _ in g]
    for val_r in val_h[::-1]:
        val_r[val_x]=1
        val_t=val_x+val_d
        (val_t<0 or val_t>=val_m) and (val_d:=-val_d)
        val_x+=val_d
    return val_h

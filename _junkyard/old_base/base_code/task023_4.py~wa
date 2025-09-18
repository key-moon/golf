def p(g):
    val_v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==5]
    if not val_v:return g
    val_r0=min(i for i,j in val_v);val_c0=min(j for i,j in val_v)
    val_a=sum(1 for i,j in val_v if j-val_c0<=i-val_r0)
    val_b=len(val_v)-val_a
    val_m,val_n=(2,8)if val_b>val_a else(8,2)
    for i,j in val_v:g[i][j]=val_m if j-val_c0<=i-val_r0 else val_n
    return g

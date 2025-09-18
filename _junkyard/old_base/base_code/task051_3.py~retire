def p(g):
    # build lists of positions per value
    val_d={}
    [val_d.setdefault(v,[]).append((i,j))
        for i,row in enumerate(g) for j,v in enumerate(row)]
    # find the unique marker
    val_k=[k for k,v in val_d.items() if k and len(v)==1][0]
    val_r,val_c=val_d[val_k][0]
    # gather all the other nonzero points
    val_arr=[p for k,v in val_d.items() if k and k!=val_k for p in v]
    val_rs,val_cs=zip(*val_arr)
    val_r0,val_r1,val_c0,val_c1=(
        min(val_rs),max(val_rs),min(val_cs),max(val_cs))
    val_n,val_m=len(g),len(g[0])
    # decide which side the marker sits on and extend opposite
    if val_c==val_c0:
        for j in range(val_c1+1,val_m): g[val_r][j]=val_k
    elif val_c==val_c1:
        for j in range(val_c0):           g[val_r][j]=val_k
    elif val_r==val_r0:
        for i in range(val_r1+1,val_n):   g[i][val_c]=val_k
    else:
        for i in range(val_r0):           g[i][val_c]=val_k
    return g

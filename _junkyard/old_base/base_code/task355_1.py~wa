def p(g):
    val_m,val_n=len(g),len(g[0]);val_a=g[0][0]
    for val_C in range(val_n):
        if g[0][val_C]!=val_a:break
    for val_R in range(val_m):
        if g[val_R][0]!=val_a:break
    val_b,val_d=val_a,sum(g[i][j]!=val_a for i in range(val_R)for j in range(val_C))
    for val_X,val_Y,val_U,val_V in((0,val_C,val_R,val_n),(val_R,0,val_m,val_C),(val_R,val_C,val_m,val_n)):
        val_c=sum(g[i][j]!=g[val_X][val_Y]for i in range(val_X,val_U)for j in range(val_Y,val_V))
        if val_c>val_d:val_b,val_d=g[val_X][val_Y],val_c
    return val_b

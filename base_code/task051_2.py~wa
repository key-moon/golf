def p(g):
    val_l=[x for r in g for x in r if x]
    val_=next(v for v in set(val_l) if val_l.count(v)==1)
    for val_i,val_r in enumerate(g):
        if val_ in val_r:
            val_y,val_x=val_i,val_r.index(val_)
            break
    val_u=sum(g[i][val_x]==0 for i in range(val_y))
    val_d=sum(g[i][val_x]==0 for i in range(val_y+1,len(g)))
    val_l2=sum(g[val_y][j]==0 for j in range(val_x))
    val_r2=sum(g[val_y][j]==0 for j in range(val_x+1,len(g[0])))
    val_m=max((val_u,'u'),(val_d,'d'),(val_l2,'l'),(val_r2,'r'))[1]
    if val_m=='u':
        for i in range(val_y):
            if g[i][val_x]==0: g[i][val_x]=val_
    if val_m=='d':
        for i in range(val_y+1,len(g)):
            if g[i][val_x]==0: g[i][val_x]=val_
    if val_m=='l':
        for j in range(val_x):
            if g[val_y][j]==0: g[val_y][j]=val_
    if val_m=='r':
        for j in range(val_x+1,len(g[0])):
            if g[val_y][j]==0: g[val_y][j]=val_
    return g

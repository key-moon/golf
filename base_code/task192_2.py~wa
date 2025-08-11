def p(g):
    val_h,val_w=len(g),len(g[0])
    val_C=max(set(sum(g,[]))-{0},key=lambda v:sum(r.count(v)for r in g))
    val_V=set();val_Q=[]
    for val_y in range(val_h):
        for val_x in range(val_w):
            if g[val_y][val_x]==val_C and (val_y,val_x) not in val_V:
                val_M=[val_y,val_x,val_y,val_x];val_S=[(val_y,val_x)];val_V.add((val_y,val_x))
                while val_S:
                    y,x=val_S.pop()
                    val_M[0]=min(val_M[0],y);val_M[1]=min(val_M[1],x)
                    val_M[2]=max(val_M[2],y);val_M[3]=max(val_M[3],x)
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        y1,x1=y+dy,x+dx
                        if 0<=y1<val_h and 0<=x1<val_w and g[y1][x1]==val_C and (y1,x1) not in val_V:
                            val_V.add((y1,x1));val_S.append((y1,x1))
                val_Q.append(val_M)
    for a,b,c,d in val_Q:
        for y in range(a,c+1):
            for x in range(b,d+1):
                g[y][x]=val_C
    for y in range(val_h):
        for x in range(val_w):
            if g[y][x]!=val_C: g[y][x]=0
    return g

def p(g):
    val_R=len(g);val_C=len(g[0])
    val_o=[[0]*val_C for _ in range(val_R)]
    val_V=set()
    for val_i in range(val_R):
        for val_j in range(val_C):
            if g[val_i][val_j] and (val_i,val_j) not in val_V:
                val_v=g[val_i][val_j]
                val_s=[(val_i,val_j)]; val_P=[]
                while val_s:
                    x,y=val_s.pop()
                    if 0<=x<val_R and 0<=y<val_C and (x,y) not in val_V and g[x][y]==val_v:
                        val_V.add((x,y)); val_P.append((x,y))
                        val_s+=((x+1,y),(x-1,y),(x,y+1),(x,y-1))
                val_d={}
                for x,y in val_P: val_d.setdefault(x,set()).add(y)
                val_I=set.intersection(*val_d.values())
                for x in val_d:
                    for y in val_I:
                        val_o[x][y]=val_v
    return val_o

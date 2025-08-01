def p(g):
    val_r=len(g);val_c=len(g[0]);val_v=[[0]*val_c for _ in g];val_m={}
    for val_i in range(val_r):
        for val_j in range(val_c):
            if g[val_i][val_j] and not val_v[val_i][val_j]:
                val_t=g[val_i][val_j];val_s=[(val_i,val_j)];val_v[val_i][val_j]=1;val_C=[]
                while val_s:
                    x,y=val_s.pop();val_C.append((x,y))
                    for dx,dy in((1,0),(0,1),(-1,0),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<val_r and 0<=ny<val_c and not val_v[nx][ny] and g[nx][ny]==val_t:
                            val_v[nx][ny]=1;val_s.append((nx,ny))
                val_X=min(x for x,y in val_C);val_Y=min(y for x,y in val_C)
                val_f=tuple(val_t if (val_X+u,val_Y+v) in val_C else 0
                             for u in range(3) for v in range(3))
                val_m.setdefault(val_t,[]).append(val_f)
    val_t=max(val_m,key=lambda k:len(val_m[k]));val_L=val_m[val_t]
    val_M=max(set(val_L),key=val_L.count)
    return [list(val_M[i*3:(i+1)*3]) for i in range(3)]

def p(g):
    h,w=len(g),len(g[0])
    v=set();b=set()
    for i in range(h):
        for j in range(w):
            if g[i][j] and (i,j) not in v:
                s=[(i,j)];c={(i,j)}
                while s:
                    x,y=s.pop()
                    for dx in(-1,0,1):
                        for dy in(-1,0,1):
                            if dx|dy:
                                nx,ny=x+dx,y+dy
                                if 0<=nx<h and 0<=ny<w and g[nx][ny] and (nx,ny) not in c:
                                    c.add((nx,ny));s.append((nx,ny))
                v |= c
                if len(c)>len(b): b=c
    for i in range(h):
        for j in range(w):
            if g[i][j] and (i,j) not in b:
                g[i][j]=0
    return g

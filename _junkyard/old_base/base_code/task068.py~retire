def p(g):
    u=next(v for r in g for v in r if v and sum(x==v for y in g for x in y)==1)
    x,y=next((i,j) for i,r in enumerate(g) for j,v in enumerate(r) if v==u)
    r,c=len(g),len(g[0]);h=[[0]*c for _ in g]
    for dx in(-1,0,1):
        for dy in(-1,0,1):
            a,b=x+dx,y+dy
            if 0<=a<r and 0<=b<c:h[a][b]=2
    h[x][y]=u;return h

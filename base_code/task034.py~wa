def p(g):
    N=9
    # locate the pivot "2"
    for x in range(N):
        for y in range(N):
            if g[x][y]==2:
                px,py=x,y
    # find the two orthogonal neighbors of color c
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        x,y=px+dx,py+dy
        if 0<=x<N and 0<=y<N and g[x][y]>2:
            c=g[x][y]; d1=(dx,dy)
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        if (dx,dy)==d1 or (dx,dy)==(-d1[0],-d1[1]): continue
        x,y=px+dx,py+dy
        if 0<=x<N and 0<=y<N and g[x][y]>2:
            d2=(dx,dy)
    # color the pivot
    g[px][py]=c
    # grow the triangle: fill any 0-cell whose two
    # predecessors along d1 and d2 are already c
    while True:
        grew=False
        for x in range(N):
            for y in range(N):
                if g[x][y]==0:
                    x1,y1=x-d1[0],y-d1[1]
                    x2,y2=x-d2[0],y-d2[1]
                    if 0<=x1<N and 0<=y1<N and 0<=x2<N and 0<=y2<N:
                        if g[x1][y1]==c and g[x2][y2]==c:
                            g[x][y]=c
                            grew=True
        if not grew:
            break
    return g

def p(g):
    h,w=len(g),len(g[0])
    f=[row[:]for row in g]
    d=[(i,j)for i in(-1,0,1)for j in(-1,0,1)if i or j]
    for y in range(h):
        for x in range(w):
            if g[y][x]==0 and any(0<=y+dy<h and 0<=x+dx<w and g[y+dy][x+dx]==9 for dy,dx in d):
                f[y][x]=3
    for y in range(h):
        for x in range(w):
            if f[y][x]==0 and any(0<=y+dy<h and 0<=x+dx<w and f[y+dy][x+dx]==3 for dy,dx in d):
                f[y][x]=1
    return f

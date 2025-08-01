def p(g):
    h=len(g);w=len(g[0])
    # find background = most frequent color
    d={}
    for R in g:
        for v in R:d[v]=d.get(v,0)+1
    bg=max(d,key=d.get)
    # flood‐fill all non‐bg comps
    vis=[[0]*w for _ in g]
    ds=[(1,0),(-1,0),(0,1),(0,-1)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]!=bg and not vis[i][j]:
                Q=[(i,j)];vis[i][j]=1
                for x,y in Q:
                    for dx,dy in ds:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and g[nx][ny]!=bg and not vis[nx][ny]:
                            vis[nx][ny]=1;Q.append((nx,ny))
                xs,ys=zip(*Q)
                x0,y0,minx,maxx=min(xs),max(xs),min(ys),max(ys)
                dx=max(xs)-min(xs)+1;dy=max(ys)-min(ys)+1
                comps.append((x0,y0,dx,dy,Q))
    # pick the multicolor / “irregular” piece
    for x0,y0,dx,dy,Q in comps:
        if len(Q)!=dx*dy or len({g[x][y] for x,y in Q})>1:
            piece=(dx,dy,[(x-x0,y-y0,g[x][y]) for x,y in Q])
            break
    # stamp that piece onto every *other* comp of the same box‐size
    for x0,y0,dx,dy,Q in comps:
        if (dx,dy)==(piece[0],piece[1]) and len(Q)==dx*dy:
            for ox,oy,c in piece[2]:
                g[x0+ox][y0+oy]=c
    return g

import collections
def p(g):
    # find the blob of 5s
    h,w=len(g),len(g[0])
    seen=[[0]*w for _ in range(h)]
    qs=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]==5:
                qs.append((i,j)); seen[i][j]=1
    # flood-fill to get all 5s
    q=qs[:]
    for x,y in q:
        for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny=x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and g[nx][ny]==5:
                seen[nx][ny]=1; q.append((nx,ny))
    # now find all other blobs, record their shapes
    blobs=collections.defaultdict(list)
    for i in range(h):
        for j in range(w):
            v=g[i][j]
            if v and v!=5 and not seen[i][j]:
                # flood this blob
                pts=[(i,j)]; seen[i][j]=1
                for x,y in pts:
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and g[nx][ny]==v:
                            seen[nx][ny]=1; pts.append((nx,ny))
                # normalize shape
                mi=min(x for x,y in pts); mj=min(y for x,y in pts)
                shape=tuple(sorted((x-mi,y-mj) for x,y in pts))
                blobs[shape].append(v)
    # find the shape that occurs twice
    for shape,vals in blobs.items():
        if len(vals)==2:
            # pick the larger color
            v=max(vals)
            # recolor all of v->5
            for i in range(h):
                for j in range(w):
                    if g[i][j]==v:
                        g[i][j]=5
            return g
    return g  # fallback
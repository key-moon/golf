def p(g):
    h,w=len(g),len(g[0])
    # mark outside‐connected 0’s
    from collections import deque
    seen=[[0]*w for _ in g]
    Q=deque()
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 and (i==0 or j==0 or i==h-1 or j==w-1):
                seen[i][j]=1; Q.append((i,j))
    while Q:
        i,j=Q.popleft()
        for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and g[ni][nj]==0 and not seen[ni][nj]:
                seen[ni][nj]=1; Q.append((ni,nj))
    # fill interior zeros →1
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 and not seen[i][j]:
                g[i][j]=1
    # fill outside zeros that touch a “2” →8
    for i in range(h):
        for j in range(w):
            if g[i][j]==0:
                for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = i+di, j+dj
                    if 0<=ni<h and 0<=nj<w and g[ni][nj]==2:
                        g[i][j]=8
                        break
    return g

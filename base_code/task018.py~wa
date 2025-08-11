def p(g):
    from collections import deque
    n,m=len(g),len(g[0])
    # find nonzero CCs
    vis=[[0]*m for _ in g]
    cc=[]
    for i in range(n):
        for j in range(m):
            if g[i][j] and not vis[i][j]:
                q=deque([(i,j)])
                vis[i][j]=1
                pix=[]
                while q:
                    x,y=q.popleft(); pix.append((x,y))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        u,v=x+dx,y+dy
                        if 0<=u<n and 0<=v<m and g[u][v] and not vis[u][v]:
                            vis[u][v]=1; q.append((u,v))
                cc.append(pix)
    # pick the one whose bounding‐box is altitude > width
    def bb(p):
        rs=[x for x,y in p]; cs=[y for x,y in p]
        return max(rs)-min(rs),max(cs)-min(cs)
    big=[c for c in cc if bb(c)[0]>bb(c)[1]][0]
    # rotate cw around its center
    rs=[x for x,y in big]; cs=[y for x,y in big]
    r0,r1,r2=min(rs),max(rs),(min(rs)+max(rs))/2
    c0,c1,c2=min(cs),max(cs),(min(cs)+max(cs))/2
    P=[(x-r2,y-c2) for x,y in big]
    Q=[(int(r2+(c-c2)),int(c2-(r-r2))) for r,c in P]
    # choose target so shape fits in empty
    out=[[0]*m for _ in g]
    for x,y in Q:
        out[x][y]=g[int(r2+x-r2)][int(c2+y-c2)]
    return out

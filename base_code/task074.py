def p(g):
    h,w=len(g),len(g[0]);v=set();c=[]
    for i in range(h):
        for j in range(w):
            if g[i][j]==9 and (i,j) not in v:
                s=[(i,j)];v.add((i,j))
                for x,y in s:
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        u,k=x+dx,y+dy
                        if 0<=u<h and 0<=k<w and g[u][k]==9 and (u,k) not in v:
                            v.add((u,k));s.append((u,k))
                c.append(s)
    s=max(c,key=len)
    ys=[x for x,y in s]; xs=[y for x,y in s]
    y0,x0=min(ys),min(xs);H=max(ys)-y0+1;W=max(xs)-x0+1
    for i in range(h-H+1):
        for j in range(w-W+1):
            if (i,j)!=(y0,x0) and any(g[i+a][j+b] for a in range(H) for b in range(W))\
                              and all(g[i+a][j+b]!=9 for a in range(H) for b in range(W)):
                for a in range(H):
                    for b in range(W):
                        g[y0+a][x0+b]=g[i+a][j+b]
                return g
    return g

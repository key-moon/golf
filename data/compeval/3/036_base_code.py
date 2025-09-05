def p(g):
    n,m=len(g),len(g[0])
    v=set();b1=set();cc=0
    for i in range(n):
        for j in range(m):
            if g[i][j] and (i,j) not in v:
                c=g[i][j];q=[(i,j)];v.add((i,j));s={(i,j)}
                while q:
                    x,y=q.pop()
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<m and g[nx][ny]==c and (nx,ny) not in v:
                            v.add((nx,ny));q.append((nx,ny));s.add((nx,ny))
                if len(s)>len(b1): b1=s; cc=c
    r0,r1=min(i for i,j in b1),max(i for i,j in b1)
    c0,c1=min(j for i,j in b1),max(j for i,j in b1)
    return [[cc if (i,j) in b1 else 0 for j in range(c0,c1+1)]
            for i in range(r0,r1+1)]
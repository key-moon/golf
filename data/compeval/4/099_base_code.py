def p(g):
    V=set();B=[];Z=[]
    n,m=len(g),len(g[0])
    for i in range(n):
        for j in range(m):
            t=g[i][j]
            if t==1 and (i,j) not in V:
                a=c=i; b=d=j; s=[(i,j)]; V.add((i,j))
                while s:
                    x,y=s.pop()
                    if x<a: a=x
                    if x>c: c=x
                    if y<b: b=y
                    if y>d: d=y
                    for k in (1,-1):
                        nx,ny=x+k,y
                        if 0<=nx<n and g[nx][ny]==1 and (nx,ny) not in V:
                            V.add((nx,ny)); s.append((nx,ny))
                        nx,ny=x,y+k
                        if 0<=ny<m and g[nx][ny]==1 and (nx,ny) not in V:
                            V.add((nx,ny)); s.append((nx,ny))
                B.append((a,c,b,d))
            elif t>1:
                Z.append((i,j,t))
    for i,j,t in Z:
        for a,c,b,d in B:
            if a<=i<=c and b<=j<=d:
                r0=a-1 if a else 0
                for x in range(r0,c+1):
                    for y in range(b,d+1):
                        if g[x][y]==0:
                            g[x][y]=t
                break
    return g

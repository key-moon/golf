def p(g):
    m,n=len(g),len(g[0])
    v=[[0]*n for _ in g]
    for i in range(m):
        for j in range(n):
            if g[i][j]==2 and not v[i][j]:
                st=[(i,j)];comp=[]
                v[i][j]=1
                while st:
                    x,y=st.pop();comp.append((x,y))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<m and 0<=ny<n and g[nx][ny]==2 and not v[nx][ny]:
                            v[nx][ny]=1;st.append((nx,ny))
                rows=[x for x,y in comp];a,b=min(rows),max(rows)
                d=(b-a+1)//2
                start=b-d+1
                for r in range(start,b+1):
                    t=r-start+1
                    cols=sorted(y for x,y in comp if x==r)
                    for y in cols[:t]:
                        g[r][y]=8
    return g
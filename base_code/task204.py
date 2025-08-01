def p(g):
    m,n=len(g),len(g[0])
    v=[[0]*n for _ in g]
    d=((1,0),(-1,0),(0,1),(0,-1))
    # mark zeros connected to border
    b=[(i,j) for i in range(m) for j in (0,n-1)] + [(i,j) for j in range(n) for i in (0,m-1)]
    for i,j in b:
        if g[i][j]==0 and not v[i][j]:
            st=[(i,j)]; v[i][j]=1
            while st:
                a,b0=st.pop()
                for u,w in d:
                    x,y=a+u,b0+w
                    if 0<=x<m and 0<=y<n and g[x][y]==0 and not v[x][y]:
                        v[x][y]=1; st.append((x,y))
    # fill each enclosed zero‐region
    for i in range(m):
        for j in range(n):
            if g[i][j]==0 and not v[i][j]:
                st=[(i,j)]; v[i][j]=1; R=[(i,j)]
                x0=i; x1=i; y0=j; y1=j
                while st:
                    a,b0=st.pop()
                    for u,w in d:
                        x,y=a+u,b0+w
                        if 0<=x<m and 0<=y<n and g[x][y]==0 and not v[x][y]:
                            v[x][y]=1; st.append((x,y)); R.append((x,y))
                            x0=min(x0,x); x1=max(x1,x)
                            y0=min(y0,y); y1=max(y1,y)
                # if region‐width is odd ⇒ 7 else ⇒ 2
                c=7 if (y1-y0+1)%2 else 2
                for a,b0 in R:
                    g[a][b0]=c
    return g

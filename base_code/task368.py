def p(g):
    n,m=len(g),len(g[0]);v=[[0]*m for _ in g];f={}
    for i in range(n):
        for j in range(m):
            if g[i][j]and not v[i][j]:
                s=[(i,j)];v[i][j]=1;c=[]
                while s:
                    x,y=s.pop();c.append((x,y))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        X,Y=x+dx,y+dy
                        if 0<=X<n and 0<=Y<m and g[X][Y]and not v[X][Y]:
                            v[X][Y]=1;s.append((X,Y))
                u0=min(x for x,_ in c);v0=min(y for _,y in c)
                k=tuple(sorted((a-u0,b-v0)for a,b in c))
                f.setdefault(k,[]).append((u0,v0,c))
    for k,l in f.items():
        for u0,v0,c in l:
            if len({g[a][b]for a,b in c})>1:
                z=(u0,v0,c);break
     else
        P={(a-z[0],b-z[1]):g[a][b]for a,b in z[2]}
        for u0,v0,c in l:
            if c!=z[2]:
                for a,b in c: g[a][b]=P[(a-u0,b-v0)]
    return g

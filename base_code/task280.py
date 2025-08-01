def p(g):
 n,m=len(g),len(g[0])
 for i in range(n):
  for j in range(m):
   if g[i][j]==2:
    b=0
    for di,dj in(-1,0),(1,0),(0,-1),(0,1):
     x,y=i+di,j+dj;c=0
     while 0<=x<n and 0<=y<m and g[x][y]==0:c+=1;x+=di;y+=dj
     if c>b:b=c;bd=(di,dj)
    di,dj=bd
    for k in range(b+1):
     x,y=i+di*k,j+dj*k;g[x][y]=2
     for ui,uj in(-dj,di),(dj,-di):
      a,b2=x+ui,y+uj
      if 0<=a<n and 0<=b2<m and g[a][b2]==0:g[a][b2]=3
 return g

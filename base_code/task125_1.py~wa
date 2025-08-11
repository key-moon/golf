def p(g):
 h,w=len(g),len(g[0]);v=[[0]*w for _ in g];q=[]
 for i in(0,h-1):
  for j in range(w):
   if g[i][j]!=6:v[i][j]=1;q+=[(i,j)]
 for i in range(1,h-1):
  for j in(0,w-1):
   if g[i][j]!=6:v[i][j]=1;q+=[(i,j)]
 while q:
  x,y=q.pop()
  for dx,dy in(1,0),(-1,0),(0,1),(0,-1):
   X,Y=x+dx,y+dy
   if 0<=X<h and 0<=Y<w and not v[X][Y] and g[X][Y]!=6:v[X][Y]=1;q+=[(X,Y)]
 for i in range(h):
  for j in range(w):
   if g[i][j]==8:
    if not v[i][j]:g[i][j]=4
    else:
     for dx,dy in(1,0),(-1,0),(0,1),(0,-1):
      a,b=i+dx,j+dy
      if 0<=a<h and 0<=b<w and g[a][b]==6:g[i][j]=3;break
 return g
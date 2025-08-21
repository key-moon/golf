def p(g):
 R=range
 r=[x[:]for x in g]
 n,m=len(g),len(g[0])
 v=set()
 q=[]
 for i in R(n):
  for j in R(m):
   if((i==0)|(i==n-1)|(j==0)|(j==m-1))and g[i][j]==0:q.append((i,j));v.add((i,j))
 while q:
  i,j=q.pop(0)
  for d,e in[(0,1),(1,0),(0,-1),(-1,0)]:
   x,y=i+d,j+e
   if 0<=x<n and 0<=y<m and g[x][y]==0and(x,y)not in v:v.add((x,y));q.append((x,y))
 for i in R(n):
  for j in R(m):
   if g[i][j]==0and(i,j)not in v:r[i][j]=1
 return r
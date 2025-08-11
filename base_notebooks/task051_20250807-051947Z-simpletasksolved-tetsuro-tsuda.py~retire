def p(g):
 q=range
 r=[o[:]for o in g]
 m,n=len(g),len(g[0])
 c={}
 for i in q(m):
  for j in q(n):
   if g[i][j]:c[g[i][j]]=c.get(g[i][j],0)+1
 i,j,v=next((i,j,g[i][j])for i in q(m)for j in q(n)if g[i][j]and c[g[i][j]]==1)
 for w,x in[(0,1),(1,0),(0,-1),(-1,0)]:
  y,z=i+w,j+x
  if (y<0)|(y>=m)|(z<0)|(z>=n)|(g[y][z]==0):
   k=1
   while (0<=i-k*w<m)&(0<=j-k*x<n):
    if g[i-k*w][j-k*x]==0:
     r[i-k*w][j-k*x]=v
    k+=1
 return r
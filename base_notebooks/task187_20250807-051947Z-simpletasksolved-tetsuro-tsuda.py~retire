def p(g):
 R=range
 n,m=len(g),len(g[0])
 x=next(g[i][j]for i in R(n)for j in R(m)if g[i][j])
 v=set()
 q=[(i,j)for i in R(n)for j in R(m)if(i==0 or i==n-1 or j==0 or j==m-1)and g[i][j]==0]
 for i,j in q:
  v.add((i,j))
 while q:
  i,j=q.pop(0)
  for a,b in[(0,1),(1,0),(0,-1),(-1,0)]:
   if 0<=i+a<n and 0<=j+b<m and g[i+a][j+b]==0and(i+a,j+b)not in v:
    v.add((i+a,j+b))
    q.append((i+a,j+b))
 return[[x if g[i][j]==x else(3if(i,j)in v else 2)for j in R(m)]for i in R(n)]
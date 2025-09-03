def p(g):
 r,c=len(g),len(g[0]);s=[(i,j)for i in range(r)for j in range(c)if(i<1 or i>r-2 or j<1 or j>c-2)and not g[i][j]]
 while s:
  i,j=s.pop()
  if 0<=i<r and 0<=j<c and not g[i][j]:
   g[i][j]=-1;s+=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
 for i in range(r):
  for j in range(c):
   if g[i][j]<0:g[i][j]=0
   elif not g[i][j]:g[i][j]=1
 return g

def p(g):
 r=[x[:]for x in g]
 n,m=len(g),len(g[0])
 for i in range(n-1):
  for j in range(m-1):
   if g[i][j]==g[i+1][j]==g[i][j+1]==g[i+1][j+1]==1:
    x,y=i-1,j-1
    while x>=0and y>=0:
     r[x][y]=1
     x-=1
     y-=1
   if g[i][j]==g[i+1][j]==g[i][j+1]==g[i+1][j+1]==2:
    x,y=i+2,j+2
    while x<n and y<m:
     r[x][y]=2
     x+=1
     y+=1
 return r
def p(g):
 a=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]]
 r0,c0=min(a);r1,c1=max(a)
 x=g[r0][c0];y=[g[i][j]for i,j in a if g[i][j]!=x][0]
 for r,c,o in((r0,c0,y),(r0,c1,x),(r1,c0,x),(r1,c1,y)):
  for d in(-1,0,1):
   for e in(-1,0,1):g[r+d][c+e]=o
 for j in range(c0+2,c1-1,2):g[r0][j]=g[r1][j]=5
 for i in range(r0+2,r1-1,2):g[i][c0]=g[i][c1]=5
 return g

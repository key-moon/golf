def p(g):
 m=len(g)//2;s=2*m;c=g[m][m];r=[[0]*s for _ in[0]*s]
 for y in range(m):
  for x in range(m):
   if g[y][x]:i=s-1-y;j=s-1-x;r[y][x]=r[y][j]=r[i][x]=r[i][j]=c
 return r
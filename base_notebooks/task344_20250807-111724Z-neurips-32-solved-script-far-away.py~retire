def p(g,e=enumerate):
 for i,r in e(g):
  for j,v in e(r):
   for x,y in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
    if v==2and 0<=x<len(g)and 0<=y<len(r)and g[x][y]==3:g[i][j]=0;g[x][y]=8
 return g
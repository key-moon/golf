def p(g):
 H=len(g);W=len(g[0]);o=[r[:]for r in g]
 for i in range(H):
  for j in range(W):
   c=g[i][j]
   if not c:continue
   x,y=i+1,j+1
   while x<H and y<W and g[x][y]==0:x+=1;y+=1
   if x<H and y<W and g[x][y]==c:
    for k in range(1,min(x-i,y-j)):o[i+k][j+k]=c
   x,y=i+1,j-1
   while x<H and y>=0 and g[x][y]==0:x+=1;y-=1
   if x<H and y>=0 and g[x][y]==c:
    for k in range(1,min(x-i,j-y)):o[i+k][j-k]=c
 return o
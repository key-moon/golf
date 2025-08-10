def p(g):
 h,w=len(g),len(g[0])
 r=[x[:]for x in g]
 for i in range(h):
  for j in range(w):
   if g[i][j]==3:
    for a,b in[(-1,0),(1,0),(0,-1),(0,1)]:
     if 0<=i+a<h and 0<=j+b<w and g[i+a][j+b]==2:r[i][j]=8;r[i+a][j+b]=0
 return r

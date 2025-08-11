def p(g):
 h,w=len(g),len(g[0])
 for c in range(w):
  if g[-1][c]==2:
   j=0
   for i in range(h):
    if g[-(i+1)][c+j]==5:j+=1;g[-(i)][c+j]=2
    g[-(i+1)][c+j]=2
 return g
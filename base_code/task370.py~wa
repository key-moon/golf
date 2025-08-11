def p(g):
 b=g[0][0];H,W=len(g),len(g[0])
 # find the “seed” cell: value≠background and ≠0
 for i in range(H):
  for j in range(W):
   v=g[i][j]
   if v-b and v:
    X,Y,v0=i,j,v
    break
  else: continue
  break
 # carve out all four diagonals until we hit a non-background cell or the edge
 for dx,dy in((1,1),(1,-1),(-1,1),(-1,-1)):
  i,j=X,Y
  while 0<=i+dx<H and 0<=j+dy<W and g[i+dx][j+dy]==b:
   i+=dx; j+=dy
   g[i][j]=v0
 return g

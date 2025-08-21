def p(g):
 H=len(g);W=len(g[0]);o=[[0]*W for _ in range(H)]
 for i in range(H):
  for j in range(W):
   c=g[i][j]
   if c and any(0<=a<H and 0<=b<W and g[a][b]==0 for a,b in[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]):o[i][j]=c
 return o
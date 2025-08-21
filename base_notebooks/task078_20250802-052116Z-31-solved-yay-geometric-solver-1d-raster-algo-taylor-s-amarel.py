def p(g):
 h,w=len(g),len(g[0])
 res=[[0]*w for _ in range(h)]
 for j in range(w):
  nz=[g[i][j]for i in range(h)if g[i][j]!=0]
  for k,v in enumerate(nz):
   res[k][j]=v
 return res

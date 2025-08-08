def p(g):
 h,w=len(g),len(g[0])
 res=[[0]*w for _ in range(h)]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=0:
    ni,nj=i+1,j+0
    if 0<=ni<h and 0<=nj<w:
     res[ni][nj]=g[i][j]
 return res

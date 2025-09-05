def p(g):
 h,w=len(g),len(g[0])
 res=[[0]*w for _ in range(h)]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=0:
    edge=False
    for di,dj in[(0,1),(1,0),(0,-1),(-1,0)]:
     ni,nj=i+di,j+dj
     if not(0<=ni<h and 0<=nj<w)or g[ni][nj]==0:
      edge=True
      break
    if edge:
     res[i][j]=g[i][j]
 return res

def p(g):
 r=[o[:]for o in g]
 n=len(g)
 for i in range(n):
  for j in range(n):
   if g[i][j]==5:
    for di in[-1,0,1]:
     for dj in[-1,0,1]:
      if di or dj:
       ni,nj=i+di,j+dj
       if 0<=ni<n and 0<=nj<n:r[ni][nj]=1
 return r
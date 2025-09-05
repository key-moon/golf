def p(g):
 R=range
 v=set()
 r=[x[:]for x in g]
 def d(i,j):
  if(i,j)in v or not(0<=i<10 and 0<=j<10)or g[i][j]:return[]
  v.add((i,j))
  return[(i,j)]+sum([d(i+a,j+b)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]],[])
 for i in R(10):
  for j in R(10):
   if g[i][j]==0 and(i,j)not in v:
    s=d(i,j)
    for a,b in s:r[a][b]=abs(len(s)-4)
 return r

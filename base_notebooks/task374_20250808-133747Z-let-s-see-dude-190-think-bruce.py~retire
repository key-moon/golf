def p(g):
 R=range
 v=set()
 r=[x[:]for x in g]
 s=[]
 def d(i,j):
  if(i,j)in v or not(0<=i<10 and 0<=j<10)or g[i][j]!=5:return[]
  v.add((i,j))
  return[(i,j)]+sum([d(i+a,j+b)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]],[])
 for i in R(10):
  for j in R(10):
   if g[i][j]==5 and(i,j)not in v:c=d(i,j);s.append((len(c),c))
 s.sort(reverse=True)
 for k,(l,c)in enumerate(s):
  for i,j in c:r[i][j]=[1,4,2][k]
 return r
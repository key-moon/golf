def p(g):
 R=range
 h,w=len(g),len(g[0])
 v=set()
 s=[x[:]for x in g]
 def d(i,j):
  if(i,j)in v or not(0<=i<h and 0<=j<w)or g[i][j]!=1:return[]
  v.add((i,j))
  return[(i,j)]+sum([d(i+a,j+b)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]],[])
 for i in R(h):
  for j in R(w):
   if g[i][j]==1 and(i,j)not in v:
    c=d(i,j)
    t,m,l,n=min(x[0]for x in c),max(x[0]for x in c),min(x[1]for x in c),max(x[1]for x in c)
    if len(c)==2*(m-t+n-l)and m>t and n>l and any(g[x][y]==0 for x in R(t+1,m)for y in R(l+1,n)):
     for u,e in c:s[u][e]=3
 return s

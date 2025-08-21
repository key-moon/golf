def p(g):
 R=range
 r=[x[:]for x in g]
 v=set()
 d=[(0,1),(1,0),(0,-1),(-1,0)]
 for i in R(10):
  for j in R(10):
   if g[i][j]==5and(i,j)not in v:
    c,q=set(),[(i,j)]
    c.add((i,j))
    v.add((i,j))
    while q:
     x,y=q.pop(0)
     for a,b in d:
      u,w=x+a,y+b
      if 0<=u<10and 0<=w<10and g[u][w]==5and(u,w)not in c:c.add((u,w));v.add((u,w));q.append((u,w))
    n=5-len(c)
    for x,y in c:r[x][y]=n
 return r
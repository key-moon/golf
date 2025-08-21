def p(g):
 r=[x[:]for x in g]
 n,m=len(g),len(g[0])
 v=set()
 a=[]
 for i in range(n):
  for j in range(m):
   if g[i][j]!=2and(i,j)not in v:
    c,q=[],[(i,j)]
    v.add((i,j))
    z=0
    while q:
     x,y=q.pop()
     c.append((x,y))
     if g[x][y]==0:z+=1
     for d,e in[(0,1),(1,0),(0,-1),(-1,0)]:
      if 0<=x+d<n and 0<=y+e<m and g[x+d][y+e]!=2and(x+d,y+e)not in v:v.add((x+d,y+e));q.append((x+d,y+e))
    a.append((z,c))
 V=max(x[0]for x in a)
 F=min(x[0]for x in a)
 for z,c in a:
  v=1if z==V else(8if z==F else 0)
  if v:
   for x,y in c:
    if g[x][y]==0:r[x][y]=v
 return r
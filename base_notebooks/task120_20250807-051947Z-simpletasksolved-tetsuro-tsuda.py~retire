def p(g):
 q=range
 l=len
 r=[o[:]for o in g]
 v=set()
 for i in q(l(g)):
  for j in q(l(g[0])):
   if g[i][j]and(i,j)not in v:
    c,w=[(i,j)],[(i,j)]
    v.add((i,j))
    val=g[i][j]
    while w:
     x,y=w.pop()
     for f,h in[(0,1),(1,0),(0,-1),(-1,0)]:
      m,n=x+f,y+h
      if 0<=m<l(g)and 0<=n<l(g[0])and g[m][n]==val and(m,n)not in v:
       v.add((m,n))
       c.append((m,n))
       w.append((m,n))
    s=min(p[0]for p in c)
    t=max(p[0]for p in c)
    d=min(p[1]for p in c)
    e=max(p[1]for p in c)
    for x in q(s+1,t):
     for y in q(d+1,e):
      r[x][y]=8
 return r
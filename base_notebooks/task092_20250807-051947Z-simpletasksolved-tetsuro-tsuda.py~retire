def p(g):
 q=range
 n,m=len(g),len(g[0])
 c={}
 for i in q(n):
  for j in q(m):
   if g[i][j]:
    c[g[i][j]]=c.get(g[i][j],[])
    c[g[i][j]].append((i,j))
 r=[row[:]for row in g]
 for v,p in c.items():
  if len(p)==2:
   if p[0][0]==p[1][0]:
    for j in q(min(p[0][1],p[1][1]),max(p[0][1],p[1][1])+1):
     r[p[0][0]][j]=v
 for v,p in c.items():
  if len(p)==2:
   if p[0][1]==p[1][1]:
    for i in q(min(p[0][0],p[1][0]),max(p[0][0],p[1][0])+1):
     r[i][p[0][1]]=v
 return r
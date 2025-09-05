def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:d.setdefault(v,[]).append((i,j))
 for v,P in d.items():
  (i,j),(k,l)=P
  if i==k:
   for x in range(min(j,l),max(j,l)+1):g[i][x]=v
 for v,P in d.items():
  (i,j),(k,l)=P
  if j==l:
   for y in range(min(i,k),max(i,k)+1):g[y][j]=v
 return g

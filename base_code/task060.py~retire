def p(g):
 for r in g:
  t=[i for i,x in enumerate(r) if x]
  if t:
   u,v=t;m=sum(t)//2
   for i in range(u+1,v):r[i]=[r[u],5,r[v]][(i>m)+(i>=m)]
 return g
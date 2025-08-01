def p(g):
 u=[s[:]for s in g]
 for _ in 0,1:
  for i in range(len(g)):
   *a,=filter(int,s:=g[i])
   if a and s.count(a[0])|1==3:
    l=s.index(0,k:=s.index(a[0]))
    u[i]=[a[2]]*len(g[0])
    u[i][k:l]=[a[0]]*(l-k)
  *g,=zip(*g)
  *u,=map(list,zip(*u))
 return u

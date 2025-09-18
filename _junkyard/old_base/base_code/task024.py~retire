def p(g):
 r,c={},set()
 for i,a in enumerate(g):
  for j,v in enumerate(a):
   if v&1:r[i]=v
   elif v:c|={j}
 return[[r.get(i)or(j in c)*2for j,_ in enumerate(g[0])]for i,_ in enumerate(g)]

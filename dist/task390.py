def p(g):
 for _ in 0,1:
  for i in range(15):
   if g[i].count(2)>4:
    g[i+2],g[i-2]=g[i-2],g[i+2];g[i+3],g[i-3]=g[i-3],g[i+3]
  *g,=zip(*g)
 return[*map(list,g)]
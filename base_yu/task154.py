def p(g):
 for i in range(30):
  i%=15
  if g[i].count(2)>4:
   g[i-3:i-1],g[i+2:i+4]=g[i+3:i+1:-1],g[i-3:i-1][::-1]
  *g,=map(list,zip(*g))
 return g

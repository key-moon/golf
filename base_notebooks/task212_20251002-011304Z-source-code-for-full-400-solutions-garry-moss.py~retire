def p(g,l=len,p=range):
 e,e=l(g),l(g[0]);f=[u for u in p(l(g))if 5in g[u]][0]
 for u in p(e):
  for o in p(e):
   if g[u][o]==1and u<f:
    for i in p(u,-1,-1):g[i][o]=1
   elif g[u][o]==1and u>f:
    for i in p(u,e):g[i][o]=1
   if g[u][o]==2and u<f:
    for i in p(u,f):g[i][o]=2
   elif g[u][o]==2and u>f:
    for i in p(f+1,u):g[i][o]=2
 return g
def p(g,I=range):
 h,w=len(g),len(g[0])
 for y in I(h):
  if sum(g[y])==0:g[y]=[2]*w
 for x in I(w):
  if all(g[y][x]in[0,2]for y in I(h)):
   for y in I(h):g[y][x]=2
 return g

def p(g):
 for r,s in zip(g,g[1:]):
  for i,c in enumerate(r[:-1]):
   if not c|r[i+1]|s[i]|s[i+1]:r[i]=r[i+1]=s[i]=s[i+1]=2
 return g
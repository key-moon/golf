def p(g):
 for a,b in zip(g[1:],g):
  for i in range(len(a)):a[i]=a[i] or b[i]
 return g
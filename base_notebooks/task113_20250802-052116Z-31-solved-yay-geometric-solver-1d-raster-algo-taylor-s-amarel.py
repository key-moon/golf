def p(g):
 h=len(g)
 res=[r[:]for r in g]
 for i in range(h//2):
  res[h-1-i]=res[i][:]
 return res

def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if not sum(sum(r[j:j+3])for r in g[i:i+3]):
    for r in g[i:i+3]: r[j:j+3]=[1]*3
    return g

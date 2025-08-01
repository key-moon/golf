def p(g):
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if not v and1 in r[:j] and1 in r[j+1:] or1 in[r[j]for r in g[:i]] and1 in[r[j]for r in g[i+1:]]:g[i][j]=2
 return g

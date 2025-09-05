def α(a,c):return len(set([r[c] for r in a]))
def p(g):
 E=enumerate
 h,w=len(g),len(g[0])
 vh=α(g,0)+α(g,-1)<len(set(g[0]))+len(set(g[-1]))
 g=[[C if C!=5 else 0 for C in R] for R in g]
 for r,R in E(g):
  for c,C in E(R):
   if vh:g[r][c]=max([g[0][c],g[-1][c]])
   else:g[r][c]=max([g[r][0],g[r][-1]])
 if vh:
  g=[[c for c in R if c>0] for R in g]
  g=g[:len(g[0])]
 else:
  g=[R for R in g if sum(R)>0]
  g=[R[:len(g)] for R in g]
 return g

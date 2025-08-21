def p(g,u=range):
 h,w=len(g),len(g[0])
 g=[[2 if C>0 else 0 for C in R]for R in g]
 for c in u(w):
  C=[g[r][c]for r in u(h)][::-1]
  r=sum(C)//2//2
  for i in u(r):g[-(i+1)][c]=8
 return g
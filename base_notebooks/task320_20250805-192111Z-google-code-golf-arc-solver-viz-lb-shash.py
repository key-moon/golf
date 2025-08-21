def p(g,E=range):
 h,w=len(g),len(g[0]);g=[[2 if C>0 else 0 for C in R]for R in g]
 for c in E(w):
  C=[g[r][c]for r in E(h)][::-1]
  r=sum(C)//2//2
  for i in E(r):g[-(i+1)][c]=8
 return g
def p(g,F=range):
 h,w=len(g),len(g[0])
 g=[[2 if C>0 else 0 for C in R]for R in g]
 for c in F(w):
  C=[g[r][c]for r in F(h)][::-1]
  r=sum(C)//2//2
  for i in F(r):g[-(i+1)][c]=8
 return g
def p(g,K=range):
 a=len(g)
 b=len(g[0])
 m=[[0 for _ in K(b)]for _ in K(a)]
 for r in K(a):
  for c in K(b):
   if r==0 or r==a-1 or c==0 or c==b-1:
    m[r][c]=8
   else:
    m[r][c]=0
 return m
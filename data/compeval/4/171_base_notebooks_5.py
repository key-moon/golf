def p(g,k=range):
 X=len(g)
 v=len(g[0])
 n=[[0 for _ in k(v)]for _ in k(X)]
 for r in k(X):
  for c in k(v):
   if r==0 or r==X-1 or c==0 or c==v-1:
    n[r][c]=8
   else:
    n[r][c]=0      
 return n
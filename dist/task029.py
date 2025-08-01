def p(E):
 for D in set(sum(E,[])):
  A=[(i,j)for i,r in enumerate(E)for j,v in enumerate(r)if v==D];F,G=min(A);B,C=max(A)
  if B-F>1<C-G and all((i in(F,B)or j in(G,C))for i,j in A):
   return[r[G+1:C]for r in E[F+1:B]]
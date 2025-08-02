def p(g):
 E=len(g);C=E-1;F=len(set(g[0]))==1
 for(D,B)in enumerate(g):
  for(A,G)in enumerate(B):
   if G==3:B[A]=(g[0][A]if D<C-D else g[-1][A])if F else B[0]if A<C-A else B[-1]
 return g
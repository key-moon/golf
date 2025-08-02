def p(g):
 A,B=next((A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D);D=g[A][B]
 for E in range(A+1):
  for C in range(len(g[0])):
   if C&1==B&1:g[E][C]=4
 g[A+1][B]=D;return g
def p(A):
 F,G=len(A),len(A[0])
 for B in range(F):
  for C in range(G):
   if A[B][C]==3:
    for(D,E)in((1,0),(0,1),(-1,0),(0,-1)):
     if 0<=B+D<F and 0<=C+E<G and A[B+D][C+E]==2:A[B][C]=8;A[B+D][C+E]=0
 return A
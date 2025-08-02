def p(A):
 B=A[5][0];G=[(C%6,E%6)for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A and A!=B]
 for C in(0,6,12):
  for D in(0,6,12):
   for(E,F)in G:
    if A[C+E][D+F]==0:A[C+E][D+F]=B
 return A
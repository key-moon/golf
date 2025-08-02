def p(A):
 B,C=next((A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D);E=A[B][C]
 for F in range(B+1):
  for D in range(len(A[0])):
   if D&1==C&1:A[F][D]=4
 A[B+1][C]=E;return A
def p(H):
 A=H
 for G in set(sum(A,[])):
  B=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==G];C,D=min(B);E,F=max(B)
  if E-C>1<F-D and all(A in(C,E)or B in(D,F)for(A,B)in B):return[A[D+1:F]for A in A[C+1:E]]
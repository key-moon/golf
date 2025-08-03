def p(A):
 G={}
 for(B,I)in enumerate(A):
  for(C,D)in enumerate(I):
   if D:G.setdefault(D,[]).append((B,C))
 for(D,H)in G.items():
  B,C=H[0];E,F=H[1];J=(E>B)-(E<B);K=(F>C)-(F<C)
  while 1:
   A[B][C]=D
   if B==E and C==F:break
   B+=J;C+=K
 return A
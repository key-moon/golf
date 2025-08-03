def p(A):
 C=A[0].index(5);B=0
 while any(A[B][:C]):B+=1
 F=[A[:C]for A in A[:B]]
 for(G,H)in enumerate(A):
  for(I,J)in enumerate(H):
   if J==1:
    for D in range(B):
     for E in range(C):A[G-B//2+D][I-C//2+E]=F[D][E]
 return A
B=enumerate
def p(val_g):
 C=val_g;A=len(C);E=max(max(A)for A in C);D=[[0]*A*A for _ in range(A*A)]
 for(F,G)in B(C):
  for(H,I)in B(G):
   if I==E==2:
    for(J,K)in B(C):
     for(L,M)in B(K):D[F*A+J][H*A+L]=M
 return D
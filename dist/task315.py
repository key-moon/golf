B=enumerate
def p(g):
 A=len(g);D=max(max(A)for A in g);C=[[0]*A*A for _ in range(A*A)]
 for(E,F)in B(g):
  for(G,H)in B(F):
   if H==D==2:
    for(I,J)in B(g):
     for(K,L)in B(J):C[E*A+I][G*A+K]=L
 return C
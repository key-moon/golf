def p(g):
 B=g[0].index(5);A=0
 while any(g[A][:B]):A+=1
 E=[A[:B]for A in g[:A]]
 for(F,G)in enumerate(g):
  for(H,I)in enumerate(G):
   if I==1:
    for C in range(A):
     for D in range(B):g[F-A//2+C][H-B//2+D]=E[C][D]
 return g
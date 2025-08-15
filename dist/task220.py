A=enumerate
def p(g):
 B={3:6,8:4,2:1}
 for(F,G)in A(g):
  for(H,C)in A(G):
   if C in B:
    for D in-1,0,1:
     for E in-1,0,1:
      if D or E:g[F+D][H+E]=B[C]
 return g
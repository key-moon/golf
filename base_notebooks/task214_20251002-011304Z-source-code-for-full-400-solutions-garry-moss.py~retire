def p(g,R=range):
 C=[[A for A in A[:3]]for A in g];D=[A[::-1]for A in C[::-1]]
 for A in R(3):
  for B in R(3):g[A][B+4]=C[-(B+1)][A];g[A][B+8]=D[A][B]
 return g
def p(g):
 C=[[0]*3 for A in[0]*3]
 for A in range(5):
  for B in range(7):
   if g[A][B]:C[A-(A>1)*2][B-(B>2)*4]=g[A][B]
 return C
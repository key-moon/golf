def p(A):
 D=[[0]*3 for A in[0]*3]
 for B in range(5):
  for C in range(7):
   if A[B][C]:D[B-(B>1)*2][C-(C>2)*4]=A[B][C]
 return D
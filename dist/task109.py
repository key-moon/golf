def p(A):
 B=len(A)//2;D=2*B;I=A[B][B];C=[[0]*D for A in[0]*D]
 for E in range(B):
  for F in range(B):
   if A[E][F]:G=D-1-E;H=D-1-F;C[E][F]=C[E][H]=C[G][F]=C[G][H]=I
 return C
B=len
def p(j,A=range):
 c=B(j);D=B(j[0]);p=[A[:]for A in j]
 for k in A(D):
  C=[A for A in A(c)if j[A][k]];l=B(C)//2
  for E in A(l):p[C[-1-E]][k]=8
 return p
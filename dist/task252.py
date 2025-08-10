def p(j,A=range):
 c=len(j)
 for B in A(c):
  for(k,C)in zip(A(1,c,2),A(B+1,c,2)):
   if j[0][B]:j[k][C]=4
   if j[B][0]:j[C][k]=4
 return j
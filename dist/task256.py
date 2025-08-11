def p(j,A=range):
 c=len(j)
 for B in A(c):
  if j[B][0]==2:
   k=0
   while k<c and j[B][k]==2:k+=1
   for C in A(c):
    for l in A((k+B-C)*(C!=B)):j[C][l]=3-2*(C>B)
 return j
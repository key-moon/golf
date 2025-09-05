def p(j,A=enumerate):
 c=[k[:]for k in j]
 for E,k in A(j):
  for W,l in A(k):
   for J in(-1,0,1):
    for a in(-1,0,1):
     if l and J|a and(l==2and J*a or l==1and not J*a):
      C=E+J;e=W+a
      if 0<=C<len(j)and 0<=e<len(j[0])and c[C][e]<1:c[C][e]=4+3*(l&1)
 return c
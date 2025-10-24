def p(c):
 j,d=len(c),len(c[0])
 for o in range(j-1):
  for n in range(d-1):
   if c[o][n]==c[o][n+1]==c[o+1][n]==c[o+1][n+1]==5:
    if o>0and n>0:c[o-1][n-1]=1
    if o>0and n+2<d:c[o-1][n+2]=2
    if o+2<j and n>0:c[o+2][n-1]=3
    if o+2<j and n+2<d:c[o+2][n+2]=4
 return c
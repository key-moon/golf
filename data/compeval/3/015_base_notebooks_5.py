j=len
A=range
def p(c):
 E,k=j(c),j(c[0])
 for W in A(E):
  for l in A(k):
   if c[W][l]==2:
    for J,a in[[1,1],[-1,-1],[-1,1],[1,-1]]:c[J+W][a+l]=4
   if c[W][l]==1:
    for J,a in[[0,1],[0,-1],[-1,0],[1,0]]:c[J+W][a+l]=7
 return c
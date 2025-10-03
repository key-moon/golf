B=len
A=range
def p(g):
 u=[[v for*t,v in zip(*g,s)if 1in t]for s in g if 1in s]
 for d in[-1,-1,-1,1]*2:
  for i in A(-1,25-B(u)):
   for j in A(-1,25-B(u[0])):
    if all(u[k][l]&4==g[i+k][j+l]for k in A(B(u))for l in A(B(u[0]))if-1<i+k<23>j+l>-1):
     for k in A(B(u)):
      for l in A(B(u[0])):
       if-1<i+k<23>j+l>-1:g[i+k][j+l]=u[k][l]
  u[:]=zip(*u[::d])
 return g
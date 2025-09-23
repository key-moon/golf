def p(e,p=len,u=range):
 f,f=p(e),p(e[0])
 for a in u(25):
  for a in u(f):
   for l in u(f):
    if e[a][l]==0:
     if l+1<f:
      if e[a][l+1]==1:e[a][l]=1
     if a+1<f:
      if e[a+1][l]==1:e[a][l]=1
     if l-1>=0:
      if e[a][l-1]==1:e[a][l]=1
     if a-1>=0:
      if e[a-1][l]==1:e[a][l]=1
 return e
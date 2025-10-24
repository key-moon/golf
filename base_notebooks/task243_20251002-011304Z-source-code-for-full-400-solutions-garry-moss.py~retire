def p(e,p=len,i=range):
 f,f=p(e),p(e[0])
 for n in i(25):
  for n in i(f):
   for l in i(f):
    if e[n][l]==0:
     if l+1<f:
      if e[n][l+1]==1:e[n][l]=1
     if n+1<f:
      if e[n+1][l]==1:e[n][l]=1
     if l-1>=0:
      if e[n][l-1]==1:e[n][l]=1
     if n-1>=0:
      if e[n-1][l]==1:e[n][l]=1
 return e
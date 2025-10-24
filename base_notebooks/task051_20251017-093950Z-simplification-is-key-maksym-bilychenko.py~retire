def p(c):
 C=[*map(list,c)];l,f=len(C),len(c[0]);i=sum(C,[]);a=min({*i}-{0},key=i.count);m,n=divmod(i.index(a),f)
 for t,z in[(0,1),(1,0),(0,-1),(-1,0)]:
  d,e=m+t,n+z
  if not(0<=d<l and 0<=e<f and C[d][e]):
   k=1
   while 0<=m-k*t<l and 0<=n-k*z<f:
    if C[m-k*t][n-k*z]==0:C[m-k*t][n-k*z]=a
    k+=1
 return C
def p(g):
 A=sum(g,[]);u=[c for c in enumerate(A)if c[1]%8]
 while 8in A:
  i=A.index(8)
  for(j,v)in u:A[j]=0;A[i+j-u[0][0]]=v
 return[A[i*10:][:10]for i in range(10)]
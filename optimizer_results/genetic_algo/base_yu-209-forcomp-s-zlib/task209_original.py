B=len
A=range
def p(g):
 (u,l),*_,(d,r)=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==4];C=[g[i][l:r+1]for i in A(u,d+1)]
 for i in A(u,d+1):g[i][l:r+1]=[0]*(r+1-l)
 for s in A(2,6):
  for y in A(6,68):
   for x in A(-6,68):
    if all(i+y in A(B(g)*s)and j+x in A(B(g[0])*s)and g[(i+y)//s][(j+x)//s]==C[i][j]for i in A(B(C))for j in A(B(C[0]))if C[i][j]|4!=4):
     for i in A(B(C)):
      for j in A(B(C[0])):
       if i+y in A(B(g)*s)and j+x in A(B(g[0])*s):C[i][j]|=g[(i+y)//s][(j+x)//s]
     return C
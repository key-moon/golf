B=len
A=range
def p(g):
 n=B(g)
 for _ in A(4):
  for i in A(n):
   u=[j for j in A(n)if g[i][j]]
   if B(u)==4and u[0]+3<u[3]and l:
    for(j,s)in enumerate(g[1:]):
     if j>=i:
      for k in A(u[1]+1,u[2]):s[k]=4
      if-1<(l:=u[1]-j+i):s[l]=4
      if(l:=u[2]+j-i)<n:s[l]=4
     elif any(g[j]):
      for k in A(u[1],u[3]):
       if s[k]<1:s[k]=4
    n=0
   l=B(u)
  *g,=map(list,zip(*g[::-1]))
 return g
R=range
def p(g):
 n=len(g)
 for _ in R(4):
  for i in R(n):
   u=[j for j in R(n)if g[i][j]]
   if len(u)==4 and u[0]+3<u[3]and l:
    for j,s in enumerate(g[1:]):
     if j>=i:
      for k in R(u[1]+1,u[2]):s[k]=4
      if-1<(l:=u[1]-j+i):s[l]=4
      if(l:=u[2]+j-i)<n:s[l]=4
     elif any(g[j]):
      for k in R(u[1],u[3]):
       if s[k]<1:s[k]=4
    n=0
   l=len(u)
  *g,=map(list,zip(*g[::-1]))
 return g
A=range
def p(g):
 for c in A(1,10):
  a=[(i,j)for i in A(21)for j in A(21)if g[i][j]==c]
  if 0<len(a)<25:
   u,l=min(a);d,r=max(a)
   for y in A(21-d+u):
    for x in A(21-r+l):
     for(i,j)in a*(1-any(g[y+i][x+j]for i in A(1,d-u)for j in A(1,r-l))):g[y+i-u][x+j-l]=c
 return g
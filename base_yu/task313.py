def p(g):
 n,x,y=len(g),3-(g[0][0]==g[0][2]),3-(g[0][0]==g[2][0])
 R=range(n)
 for i in R:
  s=g[i]=g[i][1:]+[g[i][-1]]
  for j in R:
   if s[j]==g[-1][-1]:s[j]=g[i%y][j%x]
 return g

# def p(g):
#  n=len(g)
#  x=g[0][0]==g[0][2]
#  y=g[0][0]==g[2][0]
#  for i in range(n):
#   g[i]=g[i][1:]+[g[i][-1]]
#   for j in range(n):
#    if g[i][j]==g[-1][-1]:
#     g[i][j]=g[i%(3-y)][j%(3-x)]
#  return g
def p(g):
 P=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]==1:P.append([r,c])
 for N in P:
  m,F=N
  if m>0:g[m-1][F]=2
  if m<9:g[m+1][F]=8
  if F>0:g[m][F-1]=7
  if F<9:g[m][F+1]=6
 return g
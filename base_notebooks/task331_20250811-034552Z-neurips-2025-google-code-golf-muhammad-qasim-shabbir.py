def p(g):
 P=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]==1:P.append([r,c])
 for v in P:
  D,L=v
  if D>0:g[D-1][L]=2
  if D<9:g[D+1][L]=8
  if L>0:g[D][L-1]=7
  if L<9:g[D][L+1]=6
 return g
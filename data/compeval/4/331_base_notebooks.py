def p(g):
 P=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]==1:
    P.append([r,c])
 for p_ in P:
  p1,p2=p_
  if p1>0:g[p1-1][p2]=2
  if p1<9:g[p1+1][p2]=8
  if p2>0:g[p1][p2-1]=7
  if p2<9:g[p1][p2+1]=6
 return g

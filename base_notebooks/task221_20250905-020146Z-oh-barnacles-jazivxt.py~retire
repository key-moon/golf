R=range
def p(g):
 f=sum(g,[])
 S=f.count(0)
 Z=9-S
 X=[[0]*(S*3)for i in R(S*3)]
 for i in R(Z):
  for r in R(3):
   for c in R(3):
    if g[r][c]:X[r+(i//S)*3][c+(i%S)*3]=max(f)
 return X
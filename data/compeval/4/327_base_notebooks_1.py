def p(g):
 P=[]
 E=enumerate
 X=[[0,0,0,0,0,0] for _ in range(6)]
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]>0:
    P.append([r,c])
  for p_ in P:
   for i in range(10):
    try:X[p_[0]+i][p_[1]+i]=g[p_[0]][p_[1]]
    except:pass
 return X

def p(g):
 P=[]
 E=enumerate
 X=[[0,0,0,0,0,0]for _ in range(6)]
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]>0:P.append([r,c])
  for F in P:
   for i in range(10):
    try:X[F[0]+i][F[1]+i]=g[F[0]][F[1]]
    except:pass
 return X
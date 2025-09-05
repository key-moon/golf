def p(g):
 P=[]
 E=enumerate
 X=[[0,0,0,0,0,0]for _ in range(6)]
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]>0:P.append([r,c])
  for j in P:
   for i in range(10):
    try:X[j[0]+i][j[1]+i]=g[j[0]][j[1]]
    except:pass
 return X
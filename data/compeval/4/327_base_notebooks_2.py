def p(g):
 P=[]
 E=enumerate
 X=[[0,0,0,0,0,0]for _ in range(6)]
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]>0:P.append([r,c])
  for v in P:
   for i in range(10):
    try:X[v[0]+i][v[1]+i]=g[v[0]][v[1]]
    except:pass
 return X
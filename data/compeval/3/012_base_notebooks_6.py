def p(g):
 z=0
 E=enumerate
 X=[[C for i,C in E(R)]for R in g]
 for r,R in E(g):
  for c,C in E(R):
   try:
    if C!=0 and g[r][c+1]!=0 and g[r][c-1]!=0:
     for i in range(-2,3):
      for j in range(-2,3):
        if abs(i)==abs(j):X[r+i][c+j]=C
        elif 0 in[i,j]:X[r+i][c+j]=g[r][c-1]
   except:pass
 return X
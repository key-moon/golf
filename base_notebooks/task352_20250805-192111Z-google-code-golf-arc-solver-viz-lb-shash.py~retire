def p(g,E=enumerate):
 X=[[C for i,C in E(R)]for R in g]
 for r,R in E(g):
  for c,C in E(R):
   if C==2:
    for i in range(-1,2):
     for j in range(-1,2):
      try:
       if[i,j]!=[0,0]and r+i>-1and c+j>-1:X[r+i][c+j]=1
      except:0
 return X
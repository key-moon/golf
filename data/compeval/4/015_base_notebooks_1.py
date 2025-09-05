def p(g,k=range):
 z=0
 E=enumerate
 X=[[C for i,C in E(R)]for R in g]
 for r,R in E(g):
  for c,C in E(R):
   if C==2:
    for i in k(-1,2):
     for j in k(-1,2):
      try:
       if abs(i)==abs(j)and X[r+i][c+j]==0:X[r+i][c+j]=4
      except:pass
   if C==1:
    for i in k(-1,2):
     for j in k(-1,2):
      try:
       if 0 in[i,j]and X[r+i][c+j]==0:X[r+i][c+j]=7
      except:pass
 return X
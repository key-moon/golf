def p(g,u=range):
 X=[[0 for i in u(len(R))]for R in g]
 E=enumerate
 P=[]
 for r,R in E(g):
  for c,C in E(R):
   if C>0:
    for i in u(-9,10):
     for j in u(-9,10):
      try:
       if 0 in[i,j]:
        if[r+i,c+j]in P:X[r+i][c+j]=2
        else: X[r+i][c+j]=int(C)
        P.append([r+i,c+j])
      except:pass
 return X
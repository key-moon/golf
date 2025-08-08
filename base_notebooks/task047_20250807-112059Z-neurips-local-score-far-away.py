def p(g,N=range,E=enumerate):
 X=[[0 for i in N(len(b))]for b in g];P=[]
 for r,R in E(g):
  for c,C in E(R):
   if C>0:
    for i in N(-9,10):
     for j in N(-9,10):
      try:
       if 0 in[i,j]:
        if[r+i,c+j]in P:X[r+i][c+j]=2
        else:X[r+i][c+j]=C
        P+=[[r+i,c+j]]
      except:0
 return X
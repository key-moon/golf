def p(g):
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if C==5:
    for i in range(r-1,r+2):
     for j in range(c-1,c+2):
      if [i,j]!=[r,c]:
       g[i][j]=1
 return g

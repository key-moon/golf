A=range
def p(g,E=enumerate):
 for(r,B)in E(g):
  for(c,C)in E(B):
   if C==5:
    for i in A(r-1,r+2):
     for j in A(c-1,c+2):
      if[i,j]!=[r,c]:g[i][j]=1
 return g
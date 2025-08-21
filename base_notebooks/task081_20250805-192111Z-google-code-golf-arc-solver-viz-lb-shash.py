from collections import*
def p(g,E=range):
 X=[[8 if C==8 else 0 for C in R]for R in g]
 for r in E(len(g)-1):
  for c in E(len(g[0])-1):
   a=[g[r][c:c+2],g[r+1][c:c+2]]
   b=[x for R in a for x in R]
   C=Counter(b).most_common(1)
   if C[0][1]==3and C[0][0]!=0:
    for i in E(r,r+2):
     for j in E(c,c+2):
      if X[i][j]==0:X[i][j]=1
 return X
L=len
R=range
def p(g):
 h,w=L(g),L(g[0])
 C=[x for r in g for x in r]
 C=sorted(C)[-1]
 g=[[0]+R+[0]for R in g]
 Z=[[0]*(w+2)]
 g=Z+g+Z
 P=[[1,1],[-1,-1],[-1,1],[1,-1],[0,1],[0,-1],[-1,0],[1,0],[0,0]]
 for r in R(1,h+1):
  for c in R(1,w+1):
   if g[r][c]==C:
    X=[g[i[0]+r][i[1]+c]for i in P]
    if sum(X)==C:g[r][c]=0
 g=g[1:-1]
 g=[R[1:-1]for R in g]
 return g

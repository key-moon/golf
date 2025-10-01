A=range
def p(g):
 for l in A(10):
  for u in A(10):
   for r in A(l,10):
    if g[u][r]!=5:break
   for d in A(u,10):
    if g[d][l]!=5:break
   for c in A(10):
    B=[i*10+j for i in A(10)for j in A(10)if g[i][j]==c];C=[i*10+j for i in A(u,d)for j in A(l,r)if g[i][j]==0]
    if[x-min(B)for x in B]==[x-min(C)for x in C]:
     for x in B:g[x//10][x%10]=0
     for x in C:g[x//10][x%10]=c
 return g
A=range
def p(g):
 for m in A(1,8):
  for u in A(12-m):
   for l in A(12-m):
    if[k:=(5,)*(m+2),*[(5,*[0]*m,5)]*m,k]==[*zip(*g[u-1:u+m+1])][l-1:l+m+1]:
     for s in g[u:u+m]:s[l:l+m]=[2]*m
 return g
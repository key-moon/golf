A=range
def p(g):
 for l in A(14):
  for u in A(14):
   if g[u][l+6]==g[u+6][l]==5:
    for i in A(16):
     for j in A(16):
      if all(0**g[u+y+1][l+x+1]==0**g[i+y][j+x]for y in A(5)for x in A(5)):
       for y in A(5):
        for x in A(5):g[i+y][j+x]=g[i+y][j+x]and g[u+y+1][l+x+1]
 return g
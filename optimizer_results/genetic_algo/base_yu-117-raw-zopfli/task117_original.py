B=len
A=range
def p(g):
 for i in A(B(g)-2,0,-1):
  for j in A(B(g)):
   if[1]<[g[i][j]]*4==g[i-1][j-1:j+2:2]+g[i+1][j-1:j+2:2]:
    for x in A(B(g)):
     for y in A(B(g)):
      if g[y][x]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
    for x in A(B(g)):
     for y in A(B(g)):
      if g[y][x]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
    return g
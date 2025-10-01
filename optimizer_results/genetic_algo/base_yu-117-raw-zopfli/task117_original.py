A=range
def p(g):
 n=len(g)
 for i in A(n-2,0,-1):
  for j in A(n):
   if[1]<[g[i][j]]*4==g[i-1][j-1:j+2:2]+g[i+1][j-1:j+2:2]:
    for z in A(n*n*2):
     if g[y:=z//n%n][x:=z%n]:g[i*2-y][x]=g[y][j*2-x]=g[y][x]
    return g
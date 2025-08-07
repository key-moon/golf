R=range
def p(g):
 c=[next(filter(int,s))for s in g if any(s)][-1]
 for A in R(400):
  for k in R(i:=A%20,0,-1):
   if c==g[i][j:=A//20]!=g[k][j]>0:
    for s in g[k+1:20]:s[j]=g[i][j]
    break
 return g
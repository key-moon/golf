R=range
def p(g):
 c=[next(filter(int,s))for s in g if any(s)][-1]
 for I in R(400):
  for k in R(i:=I%20,0,-1):
   if c==g[i][j:=I//20]!=g[k][j]>0:
    for s in g[k+1:20]:s[j]=g[i][j]
    break
 return g

# def p(g):
#  c=[next(filter(int,s))for s in g if any(s)][-1]
#  for i in range(20):
#   for j in range(20):
#    for k in range(i)[::-1]:
#     if c==g[i][j]!=g[k][j]>0:
#      for l in range(k+1,20):g[l][j]=g[i][j]
#      break
#  return g
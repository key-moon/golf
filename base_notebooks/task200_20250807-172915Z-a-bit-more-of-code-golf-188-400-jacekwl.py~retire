def p(g):
 n,E,R,t=10,enumerate,range,0
 for i,a in E(g):
  for j,v in E(a):
   if v%5:
    for c in R(j,n,2):
     for r in R(i+1):g[r][c]=v
    for c in R(j+1,n,2):g[t*(n-1)][c]=5;t^=1
    return g
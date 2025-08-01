def p(g):
 n=len(g)//3;c=g[n][0]
 for a in range(3):
  for b in range(3):
   if a^b&1:
    o=a*(n+1);p=b*(n+1)
    for i in range(n):
     for j in range(n):
      if g[i][j]&(g[i][j]-c)and not g[o+i][p+j]:g[o+i][p+j]=c
 return g

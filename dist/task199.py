def p(g,E=enumerate):
 for(i,r)in E(g):
  for(j,v)in E(r):
   if v and v^4:
    g[i+1][j]=v
    for k in range(i+1):g[k][j&1::2]=[4]*len(g[k][j&1::2])
    return g
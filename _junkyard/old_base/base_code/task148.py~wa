def p(g):
 u,v=[j for j,c in enumerate(zip(*g)) if 2 in c]
 a=[i for i,r in enumerate(g) if r[u]==2][0]
 b=[i for i,r in enumerate(g) if r[v]==2][0]
 for i,r in enumerate(g):
  for j,z in enumerate(r):
   if z==8:
    for k in range(u+1,j):r[k]=8
    r[j]=4
    t=b+i-a
    for k in range(j+1,v):g[t][k]=8
 return g
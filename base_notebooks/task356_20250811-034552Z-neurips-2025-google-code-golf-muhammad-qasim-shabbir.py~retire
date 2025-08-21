def p(g,v=range):
 D=[r[:]for r in g]
 for c in v(1,10):
  E=[(i,j)for i in v(len(g))for j in v(len(g[0]))if g[i][j]==c]
  for i in v(len(E)):
   for j in v(i+1,len(E)):
    o,U=E[i]
    L,b=E[j]
    if o==L:
     for x in v(min(U,b),max(U,b)+1):D[o][x]=c
    elif U==b:
     for y in v(min(o,L),max(o,L)+1):D[y][U]=c
 return D
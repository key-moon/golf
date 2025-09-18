def p(g):
 for r in g:
  if (a:=[i for i,v in enumerate(r) if v==8])[1:]:
   for i in range(a[0]+1,a[-1]): r[i]=3
 for j,c in enumerate(zip(*g)):
  if (a:=[i for i,v in enumerate(c) if v==8])[1:]:
   for i in range(a[0]+1,a[-1]): g[i][j]=3
 return g

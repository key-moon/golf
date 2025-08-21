def p(g):
 E=enumerate
 m=len({v for F in g for v in F if v})
 s=[0]*m
 for i,F in E(g):
  for j,v in E(F):
   if v:s[(i+j)%m]=v
 return[[s[(i+j)%m]for j in range(len(g[0]))]for i in range(len(g))]
def p(g):
 E=enumerate
 m=len({v for k in g for v in k if v})
 s=[0]*m
 for i,k in E(g):
  for j,v in E(k):
   if v:s[(i+j)%m]=v
 return[[s[(i+j)%m]for j in range(len(g[0]))]for i in range(len(g))]
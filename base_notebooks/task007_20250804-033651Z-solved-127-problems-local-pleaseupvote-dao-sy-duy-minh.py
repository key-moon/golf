def p(g):
 E=enumerate
 m=len({v for row in g for v in row if v})
 s=[0]*m
 for i,row in E(g):
  for j,v in E(row):
   if v:s[(i+j)%m]=v
 return[[s[(i+j)%m]for j in range(len(g[0]))]for i in range(len(g))]

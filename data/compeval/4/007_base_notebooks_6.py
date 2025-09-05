def p(g):
 m=len({v for row in g for v in row if v})
 s=[0]*m
 for i,row in enumerate(g):
  for j,v in enumerate(row):
   if v:s[(i+j)%m]=v
 return[[s[(i+j)%m]for j in range(len(g[0]))]for i in range(len(g))]

def p(g):
 c=[r[:]for r in g]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if g[i][j:j+3]==[1,1,1]and g[i+1][j:j+3]==[1,0,1]and g[i+2][j:j+3]==[1,1,1]:
    for u,v in((0,1),(1,0),(1,1),(1,2),(2,1)):c[i+u][j+v]=2
    for u,v in((0,0),(0,2),(2,0),(2,2)):c[i+u][j+v]=0
 return c
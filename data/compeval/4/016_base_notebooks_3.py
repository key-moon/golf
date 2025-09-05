def p(g):
 d={0:7,1:5,2:6,3:4,4:3,5:1,6:2,7:0,8:9,9:8}
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   g[r][c]=d[C]
 return g

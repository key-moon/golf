def p(g):
 z=0
 S=False
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if C!=0:
    if S==False:
     S=True
     z=int(C)
    else:
     S=False
     z=0
   else:g[r][c]=z
 return g

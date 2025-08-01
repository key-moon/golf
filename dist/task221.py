def p(g):
 AA=len(g);AE=len(g[0]);AF=sum(v==0 for r in g for v in r);AD=[[0]*AE*AF for _ in range(AA*AF)]
 for AC in range(AA*AE-AF):
  for AB,row in enumerate(g):
   AD[AA*(AC//AF)+AB][AE*(AC%AF):AE*(AC%AF)+AE]=row
 return AD
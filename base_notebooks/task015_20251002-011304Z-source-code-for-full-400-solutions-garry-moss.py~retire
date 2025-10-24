def p(g,b=range(9)):
 b=[(e,f,c)for e in b for f in b if 0<(c:=g[e][f])<3]
 for e,f,c in b:
  for u in-1,0,1:
   for b in-1,0,1:
    if u|b and(u*b!=0)==(c>1):g[e+u][f+b]=7-3*(c>1)
 return g
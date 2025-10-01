def p(g):
 u=[*filter(max,g)];r=u[0][0]<1
 for j,s in enumerate(u):
  if r:s.reverse()
  if 8in s:
   a=s.index(8)
   s[1:a+1]=[8]*~-a+[4]
  if 8in u[j-len(u)//2]:
   s[:-1]=[8]*~-len(g[0])
  if r:s.reverse()
 return g
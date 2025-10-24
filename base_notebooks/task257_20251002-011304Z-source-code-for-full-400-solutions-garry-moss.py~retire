def p(n,r=len,g=range):
 r,r=r(n),r(n[0])
 for r in g(4):
  for o in g(4):
   if n[r][o]==0:
    if n[r][o+5]>0:n[r][o]=n[r][o+5]
   if n[r][o]==0:
    if n[r+5][o]>0:n[r][o]=n[r+5][o]
   if n[r][o]==0:
    if n[r+5][o+5]>0:n[r][o]=n[r+5][o+5]
 return[r[:4]for r in n[:4]]
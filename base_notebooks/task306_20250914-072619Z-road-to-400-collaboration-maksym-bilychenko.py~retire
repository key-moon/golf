def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 for r in R(h//2):
  if len(set(g[r]))>2:g[r+(h//2)+1]=g[r][:]
 x=g[0].count(4)+1
 for r in R(h//2,h):
  if len(set(g[r]))>2:g[r-(h//2)-1]=g[r][:]
 x=g[0].count(4)+1
 if x==1:
  for r in R(h//2):
   for c in R(w):
    m=max([g[r][c],g[r+(h//2)+1][c]])
    g[r][c]=m
    g[r+(h//2)+1][c]=m
 for r in R(h):
  for c in R(w//x):
   for z in R(x):
    g[r][c]=max([g[r][c],g[r][c+(w//x+1)*z]])
    g[r][c+(w//x+1)*z]=max([g[r][c],g[r][c+(w//x+1)*z]])
 for r in R(h):
  for c in R(w//x):
   for z in R(x):
    g[r][c]=max([g[r][c],g[r][c+(w//x+1)*z]])
    g[r][c+(w//x+1)*z]=max([g[r][c],g[r][c+(w//x+1)*z]])
 return g
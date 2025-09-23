L=len
R=range
def p(g):
 for i in range(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(h):
   if 3 in g[r]:
    x=g[r].index(3)
    C=max(g[r][:x])
    if C>0:
     for c in R(g[r].index(C),x):g[r][c]=C
 return g
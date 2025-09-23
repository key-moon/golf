L=len
R=range
def p(g):
 D=[0]
 for i in range(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(1,h-1):
   C=g[r][0]
   D+=[C]
   P=g[r][1:].count(C)
   if P>0:
    for i in R(P):
     x=g[r][i+1:].index(C)
     g[r][x+i+1]=0
     g[r][i+1]=C
 g=[[c if c in D else 0 for c in r] for r in g]
 return g
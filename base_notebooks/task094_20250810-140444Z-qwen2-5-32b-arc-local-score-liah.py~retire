L=len
R=range
def p(g):
 d,V=[],[]
 h,w=L(g),L(g[0])
 for r in R(h-4):
  for c in R(w-4):
   X=[[g[i+r][j+c]for i in R(5)]for j in R(5)]
   X=[x for R in X for x in R]
   X=sum([x for x in X if x==1])
   if X==16:d.append(r+2);V.append(c+2)
 for r in R(h):
  for c in R(w):
   if r in d or c in V:
    if g[r][c]!=1:g[r][c]=6
 return g
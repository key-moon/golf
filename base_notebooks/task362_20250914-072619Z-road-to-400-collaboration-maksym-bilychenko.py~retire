R=range
L=len
def p(g):
 P=sum(g,[]).count(5)
 I=[i for i in R(L(g)) if g[i].count(0)==0][0]
 C=g[I][0]
 J=g[0].index(C)
 for r in R(L(g)):
  for c in R(L(g[0])):
   if r==I+P or c==J-P:g[r][c]=C
   else:g[r][c]=0
 return g
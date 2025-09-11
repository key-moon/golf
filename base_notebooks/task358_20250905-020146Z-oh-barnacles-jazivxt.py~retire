R=range
L=len
def p(g):
 for i in R(4):
  g=list(map(list,zip(*g[::-1])))
  for r in R(L(g)):
   if len(set(g[r]))>2:S=[c for c in g[r]if c>0];O=g[r].index(S[0])%L(S);g[r]=S[-O:]+S*20;g[r]=g[r][:L(g[0])]
 return g
E=range
def p(g):
 C=len(g);B=len(g[0]);A=sum(v==0for r in g for v in r);F=[[0]*B*A for _ in E(C*A)]
 for D in E(C*B-A):
  for(G,H)in enumerate(g):F[C*(D//A)+G][B*(D%A):B*(D%A)+B]=H
 return F
def p(g):
 C=len(g);B=len(g[0]);A=sum(v==0for r in g for v in r);E=[[0]*B*A for _ in range(C*A)]
 for D in range(C*B-A):
  for(F,G)in enumerate(g):E[C*(D//A)+F][B*(D%A):B*(D%A)+B]=G
 return E
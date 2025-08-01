def p(g):
 C=len(g[0]);F=g[-1].index(1);A=1;B=[[0]*C for _ in g]
 for D in B[::-1]:
  D[F]=1;E=F+A
  (E<0 or E>=C)and(A:=-A)
  F+=A
 return B
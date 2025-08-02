def p(g):
 C=len(g[0]);B=g[-1].index(1);A=1;D=[[0]*C for A in g]
 for F in D[::-1]:F[B]=1;E=B+A;(E<0 or E>=C)and(A:=-A);B+=A
 return D
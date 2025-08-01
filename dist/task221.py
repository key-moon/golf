def p(g):
 A=len(g);E=len(g[0]);F=sum(v==0 for r in g for v in r);D=[[0]*E*F for _ in range(A*F)]
 for C in range(A*E-F):
  for B,row in enumerate(g):
   D[A*(C//F)+B][E*(C%F):E*(C%F)+E]=row
 return D
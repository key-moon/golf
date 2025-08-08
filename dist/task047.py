D=range
def p(g):
 C=D;A=[[0]*9for A in C(9)];B=[(A,B,g[A][B])for A in C(9)for B in C(9)if g[A][B]]
 for(F,G,H)in B:
  for E in D(9):A[F][E]=A[E][G]=H
 A[B[0][0]][B[1][1]]=A[B[1][0]][B[0][1]]=2;return A
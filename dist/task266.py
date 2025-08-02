def p(g):
 A,B=next((A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]==2);g[A][B]=0
 for(E,F,G)in((-1,-1,3),(-1,1,6),(1,1,7),(1,-1,8)):
  C,D=A+E,B+F
  if 0<=C<len(g)and 0<=D<len(g[0]):g[C][D]=G
 return g
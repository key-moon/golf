G=range
F=enumerate
def p(g):
 for(y,r)in F(g):
  for(x,v)in F(r):
   if v==8:A,C=x,y
   if v==2:D,B=x,y
 E=(B>C)-(B<C)
 for y in G(C+E,B+E,E):g[y][A]=4
 H=(D>A)-(D<A)
 for x in G(A+H,D,H):g[B][x]=4
 return g
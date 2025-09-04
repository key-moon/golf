def p(g):
 x=g[0].index(sum(g[0]));C,*_=zip(*g);y=C.index(sum(C))
 for k in range(9):
  if k-4:g[y+k//3-1][x+k%3-1]=4
 return g
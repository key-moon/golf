def p(g):
 w,h=len(g[0]),len(g)
 for c in range(1,w):g[h-1][c]=4;g[h-c-1][c]=2
 return g
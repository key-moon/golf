def p(g):
 C=next(i for i,r in enumerate(g)if 0 in r);A=g[C].index(0);B=len(g);return[[g[C+i][B-A-j-1]for j in range(3)]for i in range(3)]
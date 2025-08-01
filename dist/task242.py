def p(g):
 AC=next(i for i,r in enumerate(g)if 0 in r);AA=g[AC].index(0);AB=len(g);return[[g[AC+i][AB-AA-j-1]for j in range(3)]for i in range(3)]
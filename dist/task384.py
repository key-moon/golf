def p(g):
 a=[i for i,x in enumerate(g)if any(x)];b=[j for j,x in enumerate(zip(*g))if any(x)]
 return[[g[i][j]for j in b for _ in(0,1)]for i in a for _ in(0,1)]
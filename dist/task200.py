def p(g):
 A=next(filter(None,g[-1]));E=g[-1].index(A)
 for C in range(E,10,2):
  for B in range(10):g[B][C]=A
 for D,C in enumerate(range(E+1,10,2)):g[(D&1)*9][C]=5
 return g
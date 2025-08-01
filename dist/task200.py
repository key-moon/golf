def p(g):
 AA=next(filter(None,g[-1]));AE=g[-1].index(AA)
 for AC in range(AE,10,2):
  for AB in range(10):g[AB][AC]=AA
 for AD,AC in enumerate(range(AE+1,10,2)):g[(AD&1)*9][AC]=5
 return g
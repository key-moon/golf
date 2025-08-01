def p(g):
 E={3:6,8:4,2:1}
 for C,F in enumerate(g):
  for D,G in enumerate(F):
   if G in E:
    for A in(-1,0,1):
     for B in(-1,0,1):
      if A or B:
       g[C+A][D+B]=E[G]
 return g
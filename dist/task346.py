def p(g):
 for A in range(len(g)-2):
  for B in range(len(g[0])-2):
   C=g[A][B];D=g[A+1][B+1]
   if C and D!=C and all(g[A+D][B+E]==C for(D,E)in((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2))):return[[D]]
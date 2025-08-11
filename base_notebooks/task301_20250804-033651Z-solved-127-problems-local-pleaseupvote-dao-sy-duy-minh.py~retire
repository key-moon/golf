from collections import *
def p(g):
 h,w=len(g),len(g[0])
 f=[i for s in g for i in s]
 C=Counter(f).most_common(10)
 C=[c for c in C if c[0]>0]
 g=[[0 for _ in R] for R in g]
 for i in range(len(C)):
  g[-(i+1)]=g[-(i+1)][:w-C[i][1]] + [C[i][0] for _ in range(C[i][1])]
 return g

from collections import *
def p(g):
 X=[x for R in g for x in R]
 C=Counter(X).most_common(2)
 if C[0][0]==0:c=C[1][0]
 else:c=C[0][0]
 return [[c]*2 for i in range(2)]

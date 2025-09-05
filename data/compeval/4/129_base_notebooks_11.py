from collections import *
def p(g):
 f=[x for r in g for x in r]
 m=Counter(f).most_common(1)[0][0]
 return[[m]*len(g[0]) for _ in g]

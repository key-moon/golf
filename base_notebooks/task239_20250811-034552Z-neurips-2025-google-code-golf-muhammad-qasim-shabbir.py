from collections import*
def p(g,v=range):
 C=Counter([x for r in g for x in r]).most_common(9)
 h,w=C[0][1],len(C)
 g=[[0 for _ in v(w)]for _ in v(h)]
 for i in v(w):
  for j in v(C[i][1]):g[j][i]=C[i][0]
 return g
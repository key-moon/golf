from collections import*
def p(g,R=range):
 C=Counter([x for r in g for x in r]).most_common(9);h,w=C[0][1],len(C);g=[[0 for _ in R(w)]for _ in R(h)]
 for i in R(w):
  for j in R(C[i][1]):g[j][i]=C[i][0]
 return g
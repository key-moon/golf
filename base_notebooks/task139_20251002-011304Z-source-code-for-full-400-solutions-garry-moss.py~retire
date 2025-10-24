from itertools import product
def p(n,q=range):
 for(r,o)in product(q(len(n)-2),q(len(n[0])-2)):
  u=q(r,r+3)
  if not all(4in q for q in[n[r][o:o+3],n[r+2][o:o+3],[n[q][o]for q in u],[n[q][o+2]for q in u]]):continue
  for(u,o)in product(u,q(o,o+3)):n[u][o]+=7*(n[u][o]==0)
 return n
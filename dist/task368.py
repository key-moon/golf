def p(g):
 u=[t for s in g if(t:=[v for v in s if v%5])]
 while(t:=[*sum(g,[]),5].index(5))<100:
  for s in u:g[t//10][t%10:t%10+len(s)]=s;t+=10
 return g
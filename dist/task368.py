def p(g):
 u=[t for s in g if(t:=[v for v in s if v%5])]
 while(t:=str(g).find('5'))>0:
  for s in u:x=t%32//3;g[t//32][x:x+len(s)]=s;t+=32
 return g
# best: 138(jailctf merger, ox jam) / others: 142(Code Golf International), 142(4atj sisyphus luke Seek mukundan), 143(JRKKX), 149(HIMAGINE THE FUTURE.), 161(THUNDER THUNDER)
# ================================================================= 138 ==================================================================

def p(g):
 u=[t for s in g if(t:=[v for v in s if v%5])]
 while (t:=str(g).find("5"))>0:
  for s in u:
   x=t%32//3
   g[t//32][x:x+len(s)]=s
   t+=32
 return g

# def p(g):
#  u=[t for s in g if(t:=[v for v in s if v%5])]
#  while (t:=[*sum(g,[]),5].index(5))<100:
#   for s in u:
#    g[t//10][t%10:t%10+len(s)]=s
#    t+=10
#  return g

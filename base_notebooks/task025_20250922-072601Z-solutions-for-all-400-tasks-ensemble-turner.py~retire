d=len
r=range
def p(g):
 f=[0]
 for i in range(8):
  g=list(map(list,zip(*g[::-1])))
  q,o=d(g),d(g[0])
  for i in r(q):
   if len(set(g[i]))<2 and g[i][0]>0:
    p=g[i][0];f+=[p]
    for e in r(0,i-1):
     n=0
     for t in r(o):
      if g[e][t]==p:g[e][t]=0;n-=1;g[i+n][t]=p
    for e in r(i+1,q):
     n=0
     for t in r(o):
      if g[e][t]==p:g[e][t]=0;n+=1;g[i+n][t]=p
 g=[[t if t in f else 0 for t in i] for i in g]
 return g
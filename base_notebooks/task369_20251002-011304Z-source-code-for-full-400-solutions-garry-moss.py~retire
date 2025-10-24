def p(n):
 e=range;t=set();n=[t[:]for t in n]
 def u(e,d):
  if(e,d)in t or not(0<=e<10and 0<=d<10)or n[e][d]:return[]
  t.add((e,d));return[(e,d)]+sum([u(e+t,d+s)for(t,s)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
 for s in e(10):
  for d in e(10):
   if n[s][d]==0and(s,d)not in t:
    m=u(s,d)
    for(o,d)in m:n[o][d]=abs(len(m)-4)
 return n
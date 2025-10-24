d=len
a=range
def p(r):
 f=[0]
 for s in range(8):
  r=list(map(list,zip(*r[::-1])))
  l,o=d(r),d(r[0])
  for s in a(l):
   if len(set(r[s]))<2and r[s][0]>0:
    p=r[s][0];f+=[p]
    for e in a(0,s-1):
     l=0
     for t in a(o):
      if r[e][t]==p:r[e][t]=0;l-=1;r[s+l][t]=p
    for e in a(s+1,l):
     l=0
     for t in a(o):
      if r[e][t]==p:r[e][t]=0;l+=1;r[s+l][t]=p
 r=[[t if t in f else 0for t in s] for s in r]
 return r
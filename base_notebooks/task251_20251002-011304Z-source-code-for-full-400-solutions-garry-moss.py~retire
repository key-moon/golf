def p(a,r=range):
 o,g=len(a),len(a[0]);h=[[0]*g for o in r(o)];n=[]
 for i in r(o):
  for p in r(g):
   if i*p==0 or i==o-1or p==g-1:
    if a[i][p]==0:h[i][p]=1;n.append((i,p))
 while n:
  m,l=n.pop(0)
  for(t,e)in[(-1,0),(1,0),(0,-1),(0,1)]:
   i,p=m+t,l+e
   if 0<=i<o and 0<=p<g and a[i][p]==0and not h[i][p]:h[i][p]=1;n.append((i,p))
 r=[[a[o][g]if a[o][g]!=0 or h[o][g]else 1for g in r(g)]for o in r(o)];return r
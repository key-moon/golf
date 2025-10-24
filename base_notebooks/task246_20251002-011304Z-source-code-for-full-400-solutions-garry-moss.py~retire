def p(q):
 p=range;l=[e[:]for e in q]
 for e in p(len(q)):
  for n in p(len(q[0])):
   if q[e][n]==2:s,d=e,n
   if q[e][n]==3:t,o=e,n
 r=1if o>d else-1
 for n in p(d+r,o+r,r):l[s][n]=8
 r=1if t>s else-1
 for e in p(s+r,t,r):l[e][o]=8
 return l
def p(S,g=range):
 p,p=len(S),len(S[0]);i=[o[:]for o in S]
 def n():
  u=set();d=[]
  for o in g(p):
   for s in g(p):
    if i[o][s]==2and(o,s)not in u:
     e=[(o,s)];u.add((o,s));x=[]
     while e:
      t,f=e.pop();x.append((t,f))
      for(b,k)in[(1,0),(-1,0),(0,1),(0,-1)]:
       o,s=t+b,f+k
       if 0<=o<p and 0<=s<p and i[o][s]==2and(o,s)not in u:u.add((o,s));e.append((o,s))
     d.append(x)
  return d
 b=n()
 if len(b)!=2:return[o[:]for o in S]
 m=lambda j:(min(o for(o,s)in j),min(o for(s,o)in j),max(o for(o,s)in j),max(o for(s,o)in j));u,o=m(b[0]),m(b[1]);s,l=((u[0]+u[2])/2,(u[1]+u[3])/2),((o[0]+o[2])/2,(o[1]+o[3])/2)
 if abs(s[0]-l[0])>abs(s[1]-l[1]):
  t,k=(u,o)if u[0]<o[0]else(o,u);d,x=t[2]+1,k[0]-1;S,t,f=[],[],[]
  for o in g(p):
   s=[s for s in g(p)if i[o][s]==5]
   if s:
    if o<d:S.append((o,s))
    elif o>x:f.append((o,s))
    else:t.append((o,s))
  for o in g(p):
   for s in g(p):
    if i[o][s]==5:i[o][s]=0
  o=d
  for(k,s)in sorted(S,reverse=1):
   if o>x:break
   for s in s:i[o][s]=5
   o+=1
  for(s,s)in t:
   if d<=s<=x:
    for s in s:i[s][s]=5
  o=x
  for(k,s)in sorted(f):
   if o<d:break
   for s in s:i[o][s]=5
   o-=1
 else:
  s,d=(u,o)if u[1]<o[1]else(o,u);d,x=s[3]+1,d[1]-1;f,t,r=[],[],[]
  for s in g(p):
   e=[o for o in g(p)if i[o][s]==5]
   if e:
    if s<d:f.append((s,e))
    elif s>x:r.append((s,e))
    else:t.append((s,e))
  for o in g(p):
   for s in g(p):
    if i[o][s]==5:i[o][s]=0
  s=d
  for(k,e)in sorted(f,reverse=1):
   if s>x:break
   for o in e:i[o][s]=5
   s+=1
  for(s,e)in t:
   if d<=s<=x:
    for o in e:i[o][s]=5
  s=x
  for(k,e)in sorted(r):
   if s<d:break
   for o in e:i[o][s]=5
   s-=1
 return[o[:]for o in i]

def p(r):
 a=range;b=len;r=[c[:]for c in r];g=set()
 for c in a(b(r)):
  for f in a(b(r[0])):
   if r[c][f]and(c,f)not in g:
    x,u=[(c,f)],[(c,f)];g.add((c,f));c=r[c][f]
    while u:
     e,f=u.pop()
     for(h,k)in[(0,1),(1,0),(0,-1),(-1,0)]:
      h,o=e+h,f+k
      if 0<=h<b(r)and 0<=o<b(r[0])and r[h][o]==c and(h,o)not in g:g.add((h,o));x.append((h,o));u.append((h,o))
    p=min(c[0]for c in x);i=max(c[0]for c in x);u=min(c[1]for c in x);s=max(c[1]for c in x)
    for e in a(p+1,i):
     for f in a(u+1,s):r[e][f]=8
 return r
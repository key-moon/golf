def p(f):
 l=[o[:]for o in f];d,p=len(l),len(l[0]);e=None;f=-1
 for o in range(2,min(9,d)+1):
  for n in range(2,min(9,p)+1):
   for b in range(0,d-o+1):
    for u in range(0,p-n+1):
     a=True
     for a in range(b,b+o):
      i=l[a]
      if any(i[o]!=0for o in range(u,u+n)):a=False;break
     if a and o*n>f:f=o*n;e=b,u,o,n
 if e:
  b,u,o,n=e
  for a in range(b,b+o):
   for o in range(u,u+n):l[a][o]=6
 return l
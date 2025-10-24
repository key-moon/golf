def p(e,t=range):
 a,a=len(e),len(e[0]);u,e={},[t[:]for t in e]
 for n in t(a):
  for r in t(a):
   i=e[n][r]
   if i:u.setdefault(i,[]).append((n,r))
 for i in u:
  (n,p),(r,d)=u[i];a=1if r>n else-1;d=1if d>p else-1
  for r in t(abs(r-n)+1):e[n+r*a][p+r*d]=i
 return e
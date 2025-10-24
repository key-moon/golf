def p(g,i=range):
 a=[s[:]for s in g];s,e=len(a),len(a[0]);f=[]
 for g in a:
  e=[]
  for s in g:e+=[s]*2
  f.extend([e[:],e[:]])
 h,e=len(f),len(f[0]);a=[[False]*e for s in i(h)];p=[]
 for r in i(h):
  for s in i(e):
   if f[r][s]!=2or a[r][s]:continue
   d=[(r,s)];a[r][s]=True;k=[]
   while d:
    o,b=d.pop();k.append((o,b))
    for j in(-1,0,1):
     for g in(-1,0,1):
      if j==g==0:continue
      c,z=o+j,b+g
      if 0<=c<h and 0<=z<e and not a[c][z]and f[c][z]==2:a[c][z]=True;d.append((c,z))
   p.append(k)
 n={(s,r)for s in i(h)for r in i(e)if f[s][r]==2}
 def g(p,m,n,h):
  for s in i(p,n+1):
   for r in i(m,h+1):f[s][r]=4
 for o in p:k=[s for(s,f)in o];o=[s for(f,s)in o];g(min(k),min(o),max(k),max(o))
 def a(s,f):
  r=10**9
  for(o,c)in s:
   for(z,k)in f:
    p=abs(o-z)+abs(c-k)
    if p<r:r=p
    if r==0:return 0
  return r
 e=len(p)
 for r in i(e):
  for s in i(e):
   if a(p[r],p[s])<5:y=p[r]+p[s];k=[s for(s,f)in y];o=[s for(f,s)in y];g(min(k),min(o),max(k),max(o))
 for(r,s)in n:f[r][s]=2
 return[s[::2]for s in f[::2]]
def p(p,f=range):
 l,o=len(p),len(p[0]);s=[h[:]for h in p];k=[[0]*o for h in f(l)];d=[]
 for i in f(l):
  for q in f(o):
   if k[i][q]or p[i][q]==0:continue
   r=[(i,q)];a=[]
   while r:
    h,n=r.pop()
    if h<0 or h>=l or n<0 or n>=o or k[h][n]or p[h][n]==0:continue
    k[h][n]=1;a.append((h,n,p[h][n]));r.extend([(h+a,n+i)for(a,i)in[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]if 0<=h+a<l and 0<=n+i<o and not k[h+a][n+i]and p[h+a][n+i]!=0])
   a and d.append(a)
 g,e,c,p=[],[],[],[]
 for a in d:
  d={n for(h,h,n)in a}
  if len(a)==1:
   r,h,n=a[0]
   if n==2:c.append((r,h))
   elif n==3:p.append((r,h))
  else:
   if 2in d:g.append(a)
   if 3in d:e.append(a)
 def a(u,z,a,t=0):
  n=next(((h,n)for(h,n,a)in u if a==z),None)
  if not n:return
  i,q=n
  for(r,n)in a:
   for(d,g,e)in u:
    c,h=d-i,g-q
    if t:h=-h
    a,k=r+c,n+h
    if 0<=a<l and 0<=k<o:s[a][k]=e
 for n in g:a(n,2,c,1)
 for n in e:a(n,3,p)
 return s
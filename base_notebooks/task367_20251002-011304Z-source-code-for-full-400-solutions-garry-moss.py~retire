def p(l,x=range):
 t,o=len(l),len(l[0])
 def e(u,g):
  a=[[0]*o for q in x(t)];e=[]
  for q in x(t):
   for n in x(o):
    if a[q][n]or u[q][n]!=g:a[q][n]=1;continue
    a[q][n]=1;h=[(q,n)];l=0;f=[(q,n)]
    while l<len(h):j,p=h[l];l+=1;[h.append((j+q,p+n))or f.append((j+q,p+n))or a[j+q].__setitem__(p+n,1)for(q,n)in[(1,0),(-1,0),(0,1),(0,-1)]if 0<=j+q<t and 0<=p+n<o and not a[j+q][p+n]and u[j+q][p+n]==g]
    e.append(f)
  return e
 q=lambda h:(min(q for(q,n)in h),min(q for(n,q)in h),max(q for(q,n)in h),max(q for(n,q)in h));f=lambda h:(lambda i,n,s,r:len(h)==(s-i+1)*(r-n+1))(*q(h));h=lambda h:(lambda i,n,s,r:{(q,n-1)for q in x(i-1,s+2)}|{(q,r+1)for q in x(i-1,s+2)}|{(i-1,q)for q in x(n-1,r+2)}|{(s+1,q)for q in x(n-1,r+2)})(*q(h));r={(q,n)for q in x(t)for n in x(o)if l[q][n]==5};j=set()
 for n in e(l,0):
  if f(n):p=h(n);a=set();[a.add((q+j,n+p))for(q,n)in(lambda i,n,s,r:{(i,n),(i,r),(s,n),(s,r)})(*q(list(p)))for(j,p)in[(1,0),(-1,0),(0,1),(0,-1)]];r.isdisjoint(a-p)and j.update(n)
 h=[list(q)for q in l];[h[q].__setitem__(n,4)for(q,n)in j if 0<=q<t and 0<=n<o];return[list(q)for q in h]
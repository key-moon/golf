def k(p):
 c={}
 for h in p:
  for l in h:c[l]=c.get(l,0)+1
 return max(c,key=c.get)
def p(f):
 h,h=len(f),len(f[0]);a=k(f);i=[list(c)for c in f];p=[]
 for e in range(h):
  for l in range(h):
   u=f[e][l]
   if u==a:continue
   b=False
   for(r,c)in((1,0),(-1,0),(0,1),(0,-1)):
    s,n=e+r,l+c
    if 0<=s<h and 0<=n<h and f[s][n]==u:b=True;break
   if not b:p.append((e,l,u))
 for(c,l,u)in p:
  for(n,a,u)in p:
   if c==n:n=(min(l,a)+max(l,a)+1)//2;s=c
   elif l==a:s=(min(c,n)+max(c,n)+1)//2;n=l
   else:continue
   if 0<=s<h and 0<=n<h:i[s][n]=u
 return i
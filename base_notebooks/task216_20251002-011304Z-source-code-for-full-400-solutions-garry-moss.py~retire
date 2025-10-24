t=range
a=len
def p(n):
 f,p=a(n),a(n[0]);b=y=k=d=m=u=0
 for l in t(f):
  r=[0]*p;e=[0]*p
  for z in t(l,f):
   r=[c+(i==2)for(c,i)in zip(r,n[z])];e=[c+(i==0)for(c,i)in zip(e,n[z])];i=q=0
   for c in t(p+1):
    if c<p and e[c]==0:i+=r[c]
    else:
     o=c-q;o=(z-l+1)*o
     if o and(i>b or i==b and o>y):b,y,k,d,m,u=i,o,l,q,z,c-1
     q=c+1;i=0
 return[c[d:u+1]for c in n[k:m+1]]if y else[]
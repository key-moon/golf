def p(n,h=len,r=enumerate,p=min,l=max,u=range):
 t,o=h(n),h(n[0]);s=[(h,e)for(h,z)in r(n)for(e,i)in r(z)if i==5];a=p(h for(h,z)in s);m=l(h for(h,z)in s);f=p(h for(z,h)in s);e=l(h for(z,h)in s)
 for z in range(a+1,m):n[z][f+1:e]=[8]*(e-f-1)
 i=None;h=0,0
 for e in u(f,e+1):
  if n[a][e]==0:i=a,e;h=-1,0;break
 if not i:
  for e in range(f,e+1):
   if n[m][e]==0:i=m,e;h=1,0;break
 if not i:
  for z in range(a,m+1):
   if n[z][f]==0:i=z,f;h=0,-1;break
 if not i:
  for z in range(a,m+1):
   if n[z][e]==0:i=z,e;h=0,1;break
 z,e=i;f,s=h
 while 0<=z<t and 0<=e<o and n[z][e]==0:n[z][e]=8;z+=f;e+=s
 return n
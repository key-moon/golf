def p(n):
 i={};t=range
 for z in t(10):
  for a in t(10):
   if n[z][a]:i[n[z][a]]=i.get(n[z][a],0)+1
 h=next(i for(i,t)in i.items()if t==1);z,i=next((i,z)for i in t(10)for z in t(10)if n[i][z]==h);n=[[0]*10for i in t(10)];n[z][i]=h
 for a in[-1,0,1]:
  for t in[-1,0,1]:
   if a or t:
    t,r=z+a,i+t
    if 0<=t<10and 0<=r<10:n[t][r]=2
 return n
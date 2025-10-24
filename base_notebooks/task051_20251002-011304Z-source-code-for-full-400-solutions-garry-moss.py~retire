def p(p):
 t=range;p=[m[:]for m in p];l,f=len(p),len(p[0]);n={}
 for m in t(l):
  for i in t(f):
   if p[m][i]:n[p[m][i]]=n.get(p[m][i],0)+1
 m,i,a=next((m,i,p[m][i])for m in t(l)for i in t(f)if p[m][i]and n[p[m][i]]==1)
 for(t,z)in[(0,1),(1,0),(0,-1),(-1,0)]:
  d,e=m+t,i+z
  if(d<0)|(d>=l)|(e<0)|(e>=f)|(p[d][e]==0):
   e=1
   while(0<=m-e*t<l)&(0<=i-e*z<f):
    if p[m-e*t][i-e*z]==0:p[m-e*t][i-e*z]=a
    e+=1
 return p
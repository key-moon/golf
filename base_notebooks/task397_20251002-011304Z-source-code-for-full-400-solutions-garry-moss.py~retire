def p(i,f=range):
 d,r=len(i),len(i[0]);n=[]
 for m in f(d-1):
  for l in f(r-1):
   e=i[m][l],i[m][l+1],i[m+1][l],i[m+1][l+1]
   if all(e):n+=[(m,l,len(set(e)))]
 for(m,l,a)in n:
  for n in f(a):
   e=m+2+n
   if e<d:i[e][l]=i[e][l+1]=3
 return i
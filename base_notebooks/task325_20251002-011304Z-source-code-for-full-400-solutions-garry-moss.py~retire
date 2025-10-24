def p(e,r=range):
 t,o=len(e),len(e[0]);a=0
 def p(l,i):
  e[l][i]=0
  for(d,f)in((1,0),(-1,0),(0,1),(0,-1)):
   r,a=l+d,i+f
   if 0<=r<t and 0<=a<o and e[r][a]:p(r,a)
 for d in r(t):
  for f in r(o):
   if e[d][f]:a+=1;p(d,f)
 return[[8*(t==r)for r in r(a)]for t in r(a)]
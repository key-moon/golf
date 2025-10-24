d=range
t=len
def p(y):
 r=False;n=None;f,f=t(y),t(y[0]);n=[[1if y[e][m]else 0for m in d(3)]for e in d(3)]
 for e in d(f-2):
  for m in d(f-2):
   if e<1and m<1:continue
   o=n;u=True
   for q in d(3):
    for s in d(3):
     i=y[e+q][m+s]
     if n[q][s]:
      if not i or o is not n and i!=o:u=r;break
      if o is n:o=i
     elif i:u=r;break
    if not u:break
   if not u:continue
   if any(0<=e+q+u<f and 0<=m+s+i<f and not(e<=e+q+u<e+3and m<=m+s+i<m+3)and y[e+q+u][m+s+i]==o for q in d(3)for s in d(3)if n[q][s]for(u,i)in((1,0),(-1,0),(0,1),(0,-1))):continue
   for q in d(3):
    for s in d(3):
     if n[q][s]:y[e+q][m+s]=5
   return y
 return y
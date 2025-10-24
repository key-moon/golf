t=enumerate
d=range
f=len
def p(y):
 i=[[c,r]for(r,e)in t(y)for(c,e)in t(e)if e==3];e=sum(i,[]);c=e[::2];e=e[1::2];r=[min(e)+1,max(e)-1,min(c)+1,max(c)-1];i=[[c,r]for(r,e)in t(y)for(c,e)in t(e)if e==2];e=sum(i,[]);c=e[::2];e=e[1::2];r[0]-=min(e);r[1]-=max(e);r[2]-=min(c);r[3]-=max(c);i=[r[:]for r in y];y=[[0if r!=3else 3for r in r]for r in y]
 for c in d(f(y)):
  for e in d(f(y[0])):
   if i[c][e]==2:y[c-min([r[0],0])+max([r[1],0])][e-min([r[2],0])+max([r[3],0])]=2
 return y
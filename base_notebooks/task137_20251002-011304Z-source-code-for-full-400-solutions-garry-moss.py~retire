def p(s):
 b,b=len(s),len(s[0]);m=[[0]*b for n in range(b)];f={};[[f.setdefault(s[n][l],[]).append((n,l))for l in range(b)if s[n][l]]for n in range(b)]
 for(s,n)in f.items():
  n.sort();i,r=n[len(n)//2];l=abs(n[1][0]-n[0][0])or abs(n[1][1]-n[0][1])if len(n)>1else 0
  if l<=0:
   for l in range(len(n)):
    for r in range(l+1,len(n)):
     if(u:=max(abs(n[l][0]-n[r][0]),abs(n[l][1]-n[r][1]))):l=u;break
    if l:break
  l=l or 1
  for n in range(1,max(i,b-1-i,r,b-1-r)//l+1):f,p,t,u=i-n*l,i+n*l,r-n*l,r+n*l;0<=f<b and[m[f].__setitem__(n,s)for n in range(max(0,t),min(b,u+1))];0<=p<b and[m[p].__setitem__(n,s)for n in range(max(0,t),min(b,u+1))];0<=t<b and[m[n].__setitem__(t,s)for n in range(max(0,f),min(b,p+1))];0<=u<b and[m[n].__setitem__(u,s)for n in range(max(0,f),min(b,p+1))]
  m[i][r]=s
 return m
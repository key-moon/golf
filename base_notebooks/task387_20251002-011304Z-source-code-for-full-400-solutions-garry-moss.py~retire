def p(t,l=range):
 s,i=len(t),len(t[0]);e=[list(u)for u in t];n,o=[],set()
 for u in l(s):
  for d in l(i):
   a=t[u][d]
   if a!=0:n.append((u,d,a));o.add(a)
 if not n:return t
 g=sorted(o)
 def x(a):return g[0]if len(g)==1or a==g[1]else g[1]
 for(u,d,a)in n:
  r=x(a)
  for y in(-1,0,1):
   for a in(-1,0,1):
    if y==0and a==0:continue
    t,a=u+y,d+a
    if 0<=t<s and 0<=a<i:e[t][a]=r
 s=min(u for(u,d,d)in n);i=max(u for(u,d,d)in n);x=min(d for(u,d,u)in n);n=max(d for(u,d,u)in n)
 if n>x:
  for d in l(x+1,n):
   if min(d-x,n-d)%2==0:e[s][d]=5;e[i][d]=5
 if i>s:
  for u in l(s+1,i):
   if min(u-s,i-u)%2==0:e[u][x]=5;e[u][n]=5
 return e
def p(z,r=range):
 n=[n[:]for n in z];s,s=len(n),len(n[0]);from collections import Counter as t,deque;c=t(sum(n,[])).most_common()[0][0];m=[[0]*s for n in r(s)];e=[]
 for u in r(s):
  for l in r(s):
   if m[u][l]:continue
   m[u][l]=1;g=n[u][l]
   if g==c:continue
   q=deque([(u,l)]);o=[(u,l)]
   while q:
    y,d=q.popleft()
    for u in(-1,0,1):
     for k in(-1,0,1):
      if u==0and k==0:continue
      p,k=y+u,d+k
      if 0<=p<s and 0<=k<s and not m[p][k]and n[p][k]==g:m[p][k]=1;q.append((p,k));o.append((p,k))
   e.append((g,o))
 for u in r(s):
  for l in r(s):
   if n[u][l]==9:
    for i in r(u,s):
     if n[i][l]==c:n[i][l]=1
 for(g,o)in e:
  if g!=9or not o:continue
  j=min(n for(n,s)in o);h=max(n for(n,s)in o);l=min(n for(s,n)in o);u=max(n for(s,n)in o);a=(u-l+1)//2
  for d in r(1,a+1):
   m,f,a,t=j-d,h+d,l-d,u+d
   if 0<=m<s:
    for d in r(max(0,a),min(s,t+1)):n[m][d]=3
   if 0<=f<s:
    for d in r(max(0,a),min(s,t+1)):n[f][d]=3
   if 0<=a<s:
    for y in r(max(0,m),min(s,f+1)):n[y][a]=3
   if 0<=t<s:
    for y in r(max(0,m),min(s,f+1)):n[y][t]=3
 return n
def p(e):
 o=[s[:]for s in e];i,f=len(e),len(e[0]);n=set();g=[]
 for u in range(i):
  for s in range(f):
   if e[u][s]!=2and(u,s)not in n:
    x,l=[],[(u,s)];n.add((u,s));a=0
    while l:
     s,h=l.pop();x.append((s,h))
     if e[s][h]==0:a+=1
     for(m,d)in[(0,1),(1,0),(0,-1),(-1,0)]:
      if 0<=s+m<i and 0<=h+d<f and e[s+m][h+d]!=2and(s+m,h+d)not in n:n.add((s+m,h+d));l.append((s+m,h+d))
    g.append((a,x))
 y=max(s[0]for s in g);t=min(s[0]for s in g)
 for(a,x)in g:
  n=1if a==y else 8if a==t else 0
  if n:
   for(s,h)in x:
    if e[s][h]==0:o[s][h]=n
 return o
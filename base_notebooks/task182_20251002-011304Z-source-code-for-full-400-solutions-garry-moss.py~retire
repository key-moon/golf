def p(g):
 y=False;from collections import Counter as b,deque;n,t=len(g),len(g[0]);e=b(q for s in g for q in s).most_common(1)[0][0]
 def h(u,e):
  m=g[u][e];l=deque([(u,e)]);f={(u,e)};x=[(u,e)]
  while l:
   j,e=l.popleft()
   for(i,y)in((1,0),(-1,0),(0,1),(0,-1)):
    s,q=j+i,e+y
    if 0<=s<n and 0<=q<t and(s,q)not in f and g[s][q]==m:f.add((s,q));l.append((s,q));x.append((s,q))
  return m,x
 d=[[y]*t for s in range(n)];x=[]
 for q in range(n):
  for l in range(t):
   if g[q][l]!=e and not d[q][l]:
    f,s=h(q,l)
    for(u,j)in s:d[u][j]=True
    x.append((f,s))
 def j(e):s=e;q=[s for(s,q)in s];l=[s for(q,s)in s];return min(q),min(l),max(q),max(l)
 def a(e):
  l=e;m,f,n,t=j(l);x=set(l)
  for s in range(m,n+1):
   for q in range(f,t+1):
    e=s in(m,n)or q in(f,t)
    if e and(s,q)not in x:return y
    if not e and(s,q)in x:return y
  return True
 e=None
 for(f,s)in x:
  if f==5and a(s):e=s;break
 if e is None:return[list(s)for s in g]
 i,y,p,n=j(e);a,t,e,n=i+1,y+1,p-1,n-1;o=[(s,q)for s in range(a,e+1)for q in range(t,n+1)];m=[(s,q)for(s,q)in o if g[s][q]!=0]
 if not m:return[list(s)for s in g]
 y=min(s for(s,q)in m);e=min(s for(q,s)in m);e={(s-y,q-e)for(s,q)in m};u=b(g[s][q]for(s,q)in m).most_common(1)[0][0];g=[s[:]for s in g]
 for(f,s)in x:
  i,y,p,n=j(s);n={(s-i,q-y)for(s,q)in s}
  if n==e:
   for(q,l)in s:g[q][l]=u
 return g
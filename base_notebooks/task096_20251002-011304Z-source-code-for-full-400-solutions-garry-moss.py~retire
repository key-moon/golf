d=max
z=min
m=range
def p(g):
 from collections import Counter as r,deque;e=r(n for a in g for n in a).most_common(1)[0][0];i,o=len(g),len(g[0]);n={}
 for f in m(i):
  for r in m(o):
   a=g[f][r]
   if a!=e:n.setdefault(a,set()).add((f,r))
 def q(g):
  n=set();p=[]
  for f in g:
   if f in n:continue
   y=deque([f]);n.add(f);h={f}
   while y:
    e,f=y.popleft()
    for(r,i)in((1,0),(-1,0),(0,1),(0,-1)):
     a=e+r,f+i
     if a in g and a not in n:n.add(a);y.append(a);h.add(a)
   p.append(h)
  return p
 def y(g):a=[a for(a,n)in g];n=[a for(n,a)in g];return z(a),z(n),d(a),d(n)
 def i(g):a,n,f,f=y(g);return{(f-a,y-n)for(f,y)in g}
 def j(g):a,n,f,n=y(g);p=a+f;return{(p-a,n)for(a,n)in g}
 def a(g):a,n,a,f=y(g);p=n+f;return{(a,p-n)for(a,n)in g}
 def f(g):a,n,f,f=y(g);return{(y-n+a,f-a+n)for(f,y)in g}
 def u(g):return a(f(a(g)))
 def g(g):n=[a(g),f(g),u(g),j(g)];return z(n,key=lambda j:sorted(i(j)))
 def r(y,p):return z(abs(a-f)+abs(n-y)for(a,n)in y for(f,y)in p)
 def b(a):a=q(n[a]);y=d((d(a for(n,a)in a)-z(a for(n,a)in a)+1for a in a),default=0);f=[r(a[n],a[f])for n in m(len(a))for f in m(n+1,len(a))];p=z(f)-1if f else-2;return-(2*y+p)
 p=sorted(n,key=b);i={a:i(g(n[a]))for a in p};x=len(p);r=x if any(len(n[a])==1for a in p)else x+1;h=2*r-1;f=[[e]*h for a in m(h)];p=[(n,(f+a,y+a))for(a,n)in enumerate(p)for(f,y)in i[n]]
 def y(y):return[list(a)for a in zip(*y[::-1])]
 def e(y):
  for(f,(a,n))in p:
   if 0<=a<h and 0<=n<h:y[a][n]=f
  return y
 for t in m(3):f=e(f);f=y(f)
 return e(f)
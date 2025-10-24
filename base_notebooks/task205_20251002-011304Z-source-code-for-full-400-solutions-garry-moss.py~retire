def p(n):
 if not n or not n[0]:return[]
 p,s=len(n),len(n[0]);f=set();k=[]
 for u in range(p):
  for z in range(s):
   if(u,z)in f:continue
   d=n[u][z];i=[(u,z)];q=[];f.add((u,z))
   while i:
    c,g=i.pop();q.append((c,g))
    for(x,o)in((1,0),(-1,0),(0,1),(0,-1)):
     m,t=c+x,g+o
     if 0<=m<p and 0<=t<s and(m,t)not in f and n[m][t]==d:f.add((m,t));i.append((m,t))
   if len(q)>len(k):k=q
 o=min(z for(z,k)in k);l=max(z for(z,k)in k);g=min(z for(k,z)in k);p=max(z for(k,z)in k);n=[z[g:p+1]for z in n[o:l+1]]
 if not n:return[]
 g=[z[:]for z in n];b=[k for z in g for k in z];o=max(set(b),key=b.count);z=[z[:]for z in g];y,l=len(z),len(z[0])
 while z and sum(1for z in z[0]if z==o)*2<=l:z.pop(0);y-=1
 while z and sum(1for z in z[-1]if z==o)*2<=l:z.pop();y-=1
 if not z:return[]
 k=list(zip(*z))
 while k and sum(1for z in k[0]if z==o)*2<=len(z):k.pop(0)
 while k and sum(1for z in k[-1]if z==o)*2<=len(z):k.pop()
 if not k:return[]
 g=[list(z)for z in zip(*k)];b=[k for z in g for k in z];o=max(set(b),key=b.count);n=min(set(b),key=b.count);y,l=len(g),len(g[0]);d=[[o]*l for z in range(y)];k=[(z,u)for(z,k)in enumerate(g)for(u,g)in enumerate(k)if g==n]
 if not k:return d
 z={z for(z,k)in k};k={z for(k,z)in k}
 for u in z:d[u]=[n]*l
 for z in k:
  for u in range(y):d[u][z]=n
 return d
def p(f,x=range):
 k='h';g,g=len(f),len(f[0]);h=[[not f[i][z]and all(not(0<=i+l<g and 0<=z+a<g)or not f[i+l][z+a]for l in(-1,0,1)for a in(-1,0,1)if l or a)for z in x(g)]for i in x(g)];p=[0]*g;a=[]
 for y in x(g):
  for b in x(g):p[b]=h[y][b]and p[b]+1
  for M in x(g):
   l=p[M]
   if l:
    for z in x(M,g):
     if not p[z]:break
     l=min(l,p[z]);[a.append((y-i+1,M,y,z,(z-M+1)*i))for i in x(1,l+1)]
 if not a:return[[*i]for i in f]
 t,e=lambda g:g[3]-g[1]+1,lambda g:g[2]-g[0]+1;a.sort(key=lambda t:(-t[4],t[0],t[1]));j=next((i for i in a if t(i)>e(i)),0);p=next((i for i in a if e(i)>t(i)),0);i=j and p and(j if t(j)>e(p)else p if t(j)<e(p)else j if j[4]>=p[4]else p)or j or p or a[0];s=[[*i]for i in f]
 def u(e):
  for i in x(e[0],e[2]+1):s[i][e[1]:e[3]+1]=[3]*t(e)
 h=lambda e,i:e[1]<=i[3]and i[1]<=e[3]and e[0]<=i[2]and i[0]<=e[2];l='vh'[t(i)<=e(i)];n=lambda e:e[1]==0 or e[3]==g-1if l==k else e[0]==0 or e[2]==g-1;b=lambda e:(e[3]+1==i[1]or e[1]-1==i[3])and e[0]<=i[2]and e[2]>=i[0]if l==k else(e[2]+1==i[0]or e[0]-1==i[2])and e[1]<=i[3]and e[3]>=i[1];c=lambda e:all(not(0<=i<g and 3in s[i][e[1]:e[3]+1])for i in(e[0]-1,e[2]+1))if l==k else all(not(0<=i<g and 3in[*zip(*s[e[0]:e[2]+1])][i])for i in(e[1]-1,e[3]+1));u(i);r=[i]
 while 1:
  for z in sorted(a,key=lambda t:(not n(t),-t[4],t[0],t[1])):
   if(t,e)[l>k](z)<5or not c(z)or not b(z)or any(h(z,i)for i in r):continue
   u(z);r+=[z];break
  else:break
 return s
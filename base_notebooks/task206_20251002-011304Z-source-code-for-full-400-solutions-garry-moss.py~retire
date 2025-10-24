def p(n,z=range):
 t=None;x,p=len(n),len(n[0]);from collections import Counter as t,deque;M=t(t for l in n for t in l).most_common(1)[0][0];s=[[False]*p for l in z(x)];k=[]
 for l in z(x):
  for t in z(p):
   if n[l][t]==M or s[l][t]:continue
   a=deque([(l,t)]);s[l][t]=True;C=[]
   while a:
    o,e=a.popleft();C.append((o,e))
    for(t,g)in((1,0),(-1,0),(0,1),(0,-1)):
     i,q=o+t,e+g
     if 0<=i<x and 0<=q<p and not s[i][q]and n[i][q]!=M:s[i][q]=True;a.append((i,q))
   k.append(C)
 r=t;m=t
 for C in k:
  if any(n[l][t]==5for(l,t)in C):r=C
  else:m=C
 if r is t or m is t:return[l[:]for l in n]
 a=min(l for(l,t)in r);u=min(l for(t,l)in r);c=max(l for(l,t)in r);u=max(l for(t,l)in r);a=a+(c-a)//2;r=u+(u-u)//2;c=min(l for(l,t)in m);z=min(l for(t,l)in m);b=[l[:]for l in n]
 for(l,t)in m:
  y=l-c+a-1;o=t-z+r-1
  if 0<=y<x and 0<=o<p:b[y][o]=n[l][t]
 return b
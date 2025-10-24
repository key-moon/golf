def p(I):
 f=True;y,e=len(I),len(I[0])
 def z(G):return tuple(map(tuple,zip(*G)))
 def G(G):from collections import Counter as A;return A([B for A in G for B in A]).most_common(1)[0][0]
 def r(f):A=f;B=[A for(A,B)in A];p=[A for(B,A)in A];return min(B),min(p),max(B),max(p)
 def a(G,E):
  H,I=len(G),len(G[0]);y=[[False]*I for A in range(H)];q=[]
  for A in range(H):
   for B in range(I):
    if y[A][B]or G[A][B]==E:continue
    z=G[A][B];m=[(A,B)];b=[]
    while m:
     e,r=m.pop()
     if G[e][r]!=z:continue
     b.append((e,r))
     for(s,o)in((1,0),(-1,0),(0,1),(0,-1)):
      p,D=e+s,r+o
    q.append((b,z))
  return q
 def p(e,r):
  A,p=e;B,D=r
  if A==B:y,H=sorted((p,D));return{(A,B)for B in range(y,H+1)}
  if p==D:f,I=sorted((A,B));return{(A,p)for A in range(f,I+1)}
 def A(G,c,p):
  D,y=len(G),len(G[0]);A=[list(A)for A in G]
  for(B,p)in p:A[B][p]=c
  return tuple(tuple(A)for A in A)
 def g(G,t):
  D,y=len(G),len(G[0]);A=[list(A)for A in G]
  for(f,(B,p))in t:A[B][p]=f
  return tuple(tuple(A)for A in A)
 def E(p):A=p;B=[A for(A,B)in A];p=[A for(B,A)in A];D,y,f,G=min(B),min(p),max(B),max(p);return(D,y),(D,G),(f,y),(f,G)
 f=G(I);m=[(A,B)for A in range(y)for B in range(e)if I[A][B]!=f]
 if m:o,m,b,s=r(m);H=b-o+1>s-m+1
 else:H=f
 q=tuple(tuple(A)for A in(I if H else z(I)));c=G(q);e=a(q,c);(n,r),(m,b)=e[0],e[-1];s=min(n);c=min(m);D=p(s,c);o=max(1,len(D));t=sum(A for(A,B)in D)//o;e=sum(A for(B,A)in D)//o;B=t,e;s=p(s,B);o=A(q,b,D);y=A(o,r,s);R={(B[0],B[1]),(B[0]+1,B[1])};s,t=len(y),len(y[0]);S={(y[A][B],(A,B))for(A,B)in R if 0<=A<s and 0<=B<t};i={(A,(B,p+2))for(A,(B,p))in S}|{(A,(B,p-2))for(A,(B,p))in S};t={(A,B)for(p,(A,B))in i}
 if t:E,t,s,e=E(t);a={(A-1,B)for(A,B)in p(E,t)};W={(A+1,B)for(A,B)in p(s,e)}
 y=g(y,i);n=A(y,r,a);X=A(n,b,W);t=G(X);n=A(X,t,R);return n if H else z(n)

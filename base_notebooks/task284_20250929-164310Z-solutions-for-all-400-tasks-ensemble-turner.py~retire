def p(I):
 F=True;E,a=len(I),len(I[0])
 def K(G):return tuple(map(tuple,zip(*G)))
 def G(G):from collections import Counter as A;return A([B for A in G for B in A]).most_common(1)[0][0]
 def N(cells):A=cells;B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
 def c(G,bg):
  H,I=len(G),len(G[0]);E=[[False]*I for A in range(H)];J=[]
  for A in range(H):
   for B in range(I):
    if E[A][B]or G[A][B]==bg:continue
    K=G[A][B];h=[(A,B)];E[A][B]=F;i=[]
    while h:
     M,N=h.pop()
     if G[M][N]!=K:continue
     i.append((M,N))
     for(P,r)in((1,0),(-1,0),(0,1),(0,-1)):
      C,D=M+P,N+r
      if 0<=C<H and 0<=D<I and not E[C][D]and G[C][D]==K:E[C][D]=F;h.append((C,D))
    J.append((i,K))
  J.sort(key=lambda t:min(A for(A,B)in t[0]));return J
 def C(a,N):
  A,C=a;B,D=N
  if A==B:E,H=sorted((C,D));return{(A,B)for B in range(E,H+1)}
  if C==D:F,I=sorted((A,B));return{(A,C)for A in range(F,I+1)}
  if B-A==D-C:F,E=(A,C)if A<=B else(B,D);G=abs(B-A);return{(F+A,E+A)for A in range(G+1)}
  if B-A==C-D:F,E=(A,C)if A<=B else(B,D);G=abs(B-A);return{(F+A,E-A)for A in range(G+1)}
  return set()
 def A(G,value,indices):
  D,E=len(G),len(G[0]);A=[list(A)for A in G]
  for(B,C)in indices:
   if 0<=B<D and 0<=C<E:A[B][C]=value
  return tuple(tuple(A)for A in A)
 def d(G,t):
  D,E=len(G),len(G[0]);A=[list(A)for A in G]
  for(F,(B,C))in t:
   if 0<=B<D and 0<=C<E:A[B][C]=F
  return tuple(tuple(A)for A in A)
 def e(indices):A=indices;B=[A for(A,B)in A];C=[A for(B,A)in A];D,E,F,G=min(B),min(C),max(B),max(C);return(D,E),(D,G),(F,E),(F,G)
 f=G(I);h=[(A,B)for A in range(E)for B in range(a)if I[A][B]!=f]
 if h:g,h,i,s=N(h);H=i-g+1>s-h+1
 else:H=F
 J=tuple(tuple(A)for A in(I if H else K(I)));k=G(J);M=c(J,k);(l,N),(m,i)=M[0],M[-1];P=min(l);n=min(m);D=C(P,n);r=max(1,len(D));o=sum(A for(A,B)in D)//r;p=sum(A for(B,A)in D)//r;B=o,p;q=C(P,B);r=A(J,i,D);E=A(r,N,q);R={(B[0],B[1]),(B[0]+1,B[1])};s,t=len(E),len(E[0]);S={(E[A][B],(A,B))for(A,B)in R if 0<=A<s and 0<=B<t};T={(A,(B,C+2))for(A,(B,C))in S}|{(A,(B,C-2))for(A,(B,C))in S};o={(A,B)for(C,(A,B))in T}
 if o:e,o,s,x=e(o);V={(A-1,B)for(A,B)in C(e,o)};W={(A+1,B)for(A,B)in C(s,x)}
 else:V=set();W=set()
 y=d(E,T);z=A(y,N,V);X=A(z,i,W);A0=G(X);Y=A(X,A0,R);return Y if H else K(Y)
from collections import deque,Counter
def p(i):
 T=lambda a:Counter([B for A in a for B in A]if isinstance(a,list)and a and isinstance(a[0],list)else[A for(A,B)in a]).most_common(1)[0][0]if a else 0
 def a(G,o=1,b=1):
  E,F=len(G),len(G[0]);K=T(G)if b else a;D=[[0]*F for A in range(E)];j=[];I=(lambda i,y:[(i+A,y+B)for A in(-1,0,1)for B in(-1,0,1)if A or B])if o else lambda i,y:[(i-1,y),(i+1,y),(i,y-1),(i,y+1)]
  for c in range(E):
   for d in range(F):
    L=deque([(c,d)]);M=[]
    while L:
     A,B=L.popleft()
     if not(0<=A<E and 0<=B<F)or D[A][B]:continue
     C=G[A][B]
     if b and C==K:continue
     D[A][B]=1;M.append((C,(A,B)))
     for(J,C)in I(A,B):L.append((J,C))
    j.append(M)
  return j
 d=lambda a:[A for(B,A)in a];A=lambda d:(min(A for(A,B)in d),min(A for(B,A)in d),max(A for(A,B)in d),max(A for(B,A)in d));f=lambda d:(A(d)[2]-A(d)[0]+1,A(d)[3]-A(d)[1]+1);U=lambda d:(A(d)[0]+(A(d)[2]-A(d)[0])//2,A(d)[1]+(A(d)[3]-A(d)[1])//2)
 def h(a,b):
  A,B=U(a);C,D=U(b)
  if A==C:return 0,1if B<D else-1
  if A<C:return 1,1if B<D else-1
  if A>C:return-1,1if B<D else-1
 l=lambda a:[(B,(A(d(a))[0]+A(d(a))[2]-C,D))for(B,(C,D))in a]if a else[];W=lambda a:[(B,(C,A(d(a))[1]+A(d(a))[3]-D))for(B,(C,D))in a]if a else[];D=lambda a,o:[(A,(B+o[0],C+o[1]))for(A,(B,C))in a]
 def L(G,C):
  F,c=len(G),len(G[0]);A=[A[:]for A in G]
  for(B,(D,E))in C:
   if B and 0<=D<F and 0<=E<c:A[D][E]=B
  return A
 def M(G,d):
  for(A,B)in d:
   C=G[A][B]
   if C:return C
 y=a(i);C=[A[:]for A in i];j,I,I=[],[],[]
 for B in y:
  if not B:continue
  E=T(B);y=[A for A in B if A[0]==E];m=[A for A in B if A[0]!=E];e=[A for(B,A)in y];G=[A for(B,A)in m];c=y[0]
  n=G+[c[1]]if G else[c[1]];m,n,o,a=A(n);r={(A,B)for A in range(m,o+1)for B in range(n,a+1)};J,K=h(e,G if G else e);H,a=f([A for(B,A)in B]);s,y,o=(H*J,0),(0,a*K),(H*J,a*K)
  def F(p):p=-p;return 0if p==0else p+1if p>0else p-1
  t,u,p=(F(J),F(0)),(F(0),F(K)),(F(J),F(K));m=[A for A in D(l(B),s)if A[0]==E];e=[A for A in D(W(B),y)if A[0]==E];y=[A for A in D(l(W(B)),o)if A[0]==E];b,c,o=D(m,t),D(e,u),D(y,p);j+=[(M(i,{A for(B,A)in b if A in r}),A)for(B,A)in b];I+=[(M(i,{A for(B,A)in c if A in r}),A)for(B,A)in c];I+=[(M(i,{A for(B,A)in o if A in r}),A)for(B,A)in o]
 C=L(C,j);C=L(C,I);C=L(C,I);return C

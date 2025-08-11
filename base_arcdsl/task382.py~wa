def E(A):return max(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def V(A):return tuple(map(max,zip(*Z(A))))
def X(A):return tuple(map(min,zip(*Z(A))))
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PP(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def ZS(A,B):return PP(A,(A[0]+42*B[0],A[1]+42*B[1]))
def ZL(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PU(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=X(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def G(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=X(A)[1]+V(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def H(A):
	if isinstance(A,tuple):return A[::-1]
	B=X(A)[0]+V(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def L(A):return min(A for(B,A)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def PR(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PZ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def M(A):return PL(A)>PW(A)
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-S(A)+1
def PX(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PY(A,B):return PQ(ZU(A,B))
def ZU(A,B):return type(B)(A(B)for B in B)
def ZX(A,a,b):return lambda x:A(a(x),b(x))
def ZZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PG(h,g,f):return lambda x:h(g(f(x)))
def PS(A,B):return lambda x:A(B(x))
def PE(A,a,b):return a if A else b
def ZY(a,b):return tuple(zip(a,b))
def PJ(a,b):return a,b
def Y(A,B,C):return tuple(range(A,B,C))
def PM(A,B):return B.union(frozenset({A}))
def ZV(A):return max(enumerate(A))[1]
def PK(A):return next(iter(A))
def K(A,B):return type(A)(A for A in A if B(A))
def PV(j):return 0,j
def J(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def P(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def ZM(a,b):return a and b
def PQ(A):return type(A)(B for A in A for B in A)
def ZE(A):return len(A)
def R(a,b):return a>b
def PH(A,B):return tuple(sorted(A,key=B))
def Q(a,b):return a==b
def W(x):return x
def p(I):I=tuple(map(tuple,I));B=PZ(I,2);U=M(B);C=PE(U,W,PU);V=C(I);X=L(B);Z=Q(X,0);D=PE(Z,W,G);E=D(V);a=PZ(E,8);b=S(a);c=Q(b,0);F=PE(c,W,H);A=F(E);d=PZ(A,8);N=PZ(A,2);e=ZJ(ZS,(1,0));f=PY(e,d);g=PL(A);O=ZU(PK,N);h=PM(0,O);i=PM(g,O);j=ZU(J,i);k=PH(h,W);l=PH(j,W);m=ZE(N);n=P(m);o=Y(0,n,1);p=ZU(PV,o);q=ZY(k,l);r=ZZ(K,f);T=PS(PK,ZV);s=PG(J,PK,PK);t=ZX(R,T,s);u=PG(P,ZV,PK);v=ZX(R,u,T);w=ZX(ZM,t,v);x=ZZ(ZZ,PJ);y=ZZ(PS,w);z=PG(r,y,x);A0=ZU(z,q);A1=PX(PR,A0,p);A2=PQ(A1);A3=ZL(A,8,A2);A4=PG(C,D,F);A5=A4(A3);return[*map(list,A5)]
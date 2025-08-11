def PX(A):return type(A)(B for A in A for B in A)
def X(A):return max(A for(A,B)in Z(A))
def U(A):return min(A for(A,B)in Z(A))
def PM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A,B,C):
	G,H=len(A),len(A[0]);I=S(A);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def V(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PL(A):return next(iter(A))[0]
def G(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def J(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in G(A))
def PV(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PK(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-U(A)+1
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PS(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PE(A,B):return PX(PQ(A,B))
def PQ(A,B):return type(B)(A(B)for B in B)
def PW(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def R(A,B):return lambda x:A(x)==B
def H(A,B):return lambda x:A(B(x))
def Q(a,b):return frozenset((B,A)for A in b for B in a)
def PP(a,b):return a,b
def Y(A,B,C):return tuple(range(A,B,C))
def PR(A):return max(enumerate(A))[1]
def PY(A):return next(iter(A))
def PZ(A):return tuple(A)
def K(A,B):return next(A for A in A if B(A))
def W(A):return frozenset({A})
def P(a,b):return type(a)(A for A in a if A not in b)
def PG(b):return not b
def PJ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a//b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]//b[0],a[1]//b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a//b[0],a//b[1]
	return a[0]//b,a[1]//b
def L(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def PH(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));T=PU(I);U=S(I);X=V(I);Z=M(T,2);A=PJ(Z,3);a=PP(A,A);b=PK(I,(0,0),a);c=J(b);d=R(PL,0);e=H(PG,d);B=K(c,e);f=W(U);g=G(X);h=G(B);i=P(g,h);j=P(i,f);k=PY(j);C=Y(0,3,1);l=Q(C,C);D=PZ(l);F=PQ(PY,D);N=PQ(PR,D);O=PW(L,A);m=PQ(O,F);n=PQ(O,N);o=PS(PH,m,F);p=PS(PH,n,N);q=PS(PP,o,p);r=PW(PV,B);s=PE(r,q);t=E(I,k,s);return[*map(list,t)]
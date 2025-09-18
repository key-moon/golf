def PG(A):return type(A)(B for A in A for B in A)
def Y(A):return min(A for(B,A)in Z(A))
def X(A):return min(A for(A,B)in Z(A))
def PS(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def ZS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ZY(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return PY(PP(ZP(A)))
def PP(A):return A[:len(A)//2]
def PH(A,B):return ZY(A,U(A),Z(B))
def PZ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def ZU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def R(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=L(A)[1]+V(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PY(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PQ(A):return tuple(tuple(A[::-1])for A in A[::-1])
def ZP(A):return tuple(A for A in zip(*A[::-1]))
def PK(A):return next(iter(A))[0]
def J(A):return len(PS(A))
def E(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PS(A))
def S(A):
	if len(A)==0:return A
	return ZZ(A,(-X(A),-Y(A)))
def ZZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def K(A,B):return frozenset((A,B)for B in Z(B))
def V(A):return tuple(map(max,zip(*Z(A))))
def Q(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*Z(A)))))
def M(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*Z(A)))))
def L(A):return tuple(map(min,zip(*Z(A))))
def P(A,n):return frozenset(A for A in A if len(A)==n)
def PL(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PV(A,B):return PG(ZX(A,B))
def ZX(A,B):return type(B)(A(B)for B in B)
def ZL(A,a,b):return lambda x:A(a(x),b(x))
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PR(h,g,f):return lambda x:h(g(f(x)))
def PJ(A,B):return lambda x:A(B(x))
def ZM(a,b):return tuple(zip(a,b))
def PW(A,B):return B.union(frozenset({A}))
def ZW(A):return max(enumerate(A))[1]
def H(A,B):return type(A)(A for A in A if B(A))
def PM(j):return 0,j
def G(A):return frozenset({A})
def PX(A,B):return max(A,key=B)
def PE(A):return max(A,default=0)
def PU(a,b):return type(a)((*a,*b))
def ZV(n):return n%2==0
def ZQ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));O=ZP(I);T=PQ(I);U=PY(I);X=G(I);Y=PR(J,W,PP);Z=PW(O,X);a=PW(T,Z);b=PW(U,a);D=PX(b,Y);c=R(D);d=PL(ZM,D,c);A=ZJ(ZX,PE);F=ZX(A,d);e=E(F);C=P(e,4);f=ZX(Q,C);g=ZX(V,C);h=PU(f,g);i=PH(F,h);j=PM(-2);k=ZE(ZQ,(0,2));l=ZE(ZQ,j);N=PJ(k,L);m=PJ(l,M);n=ZL(PZ,N,m);o=PJ(ZV,ZW);p=ZE(H,o);q=PR(S,p,n);r=ZL(ZZ,q,N);s=ZL(K,PK,r);t=PV(s,C);B=ZU(i,t);u=ZP(B);v=PQ(B);w=PY(B);x=PL(ZM,B,u);y=ZX(A,x);z=PL(ZM,y,v);A0=ZX(A,z);A1=PL(ZM,A0,w);A2=ZX(A,A1);return[*map(list,A2)]
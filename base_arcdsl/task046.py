def PG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PE(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PH(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Y(A):return max(A for(B,A)in J(A))
def V(A):return min(A for(B,A)in J(A))
def K(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=U(A);S=X if C else Z
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in S(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def PW(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A,B):return frozenset((A,B)for B in J(B))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-V(A)+1
def ZZ(A,B):return type(B)(A(B)for B in B)
def ZJ(A,a,b):return lambda x:A(a(x),b(x))
def PY(A,n):
	if n==1:return A
	return PZ(A,PY(A,n-1))
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZP(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return lambda x:A(x)==B
def PV(h,g,f):return lambda x:h(g(f(x)))
def PZ(A,B):return lambda x:A(B(x))
def PS(a,b):return a,b
def PK(A,B):return PM(PX(B,A))
def PX(A,B):return type(B)(B for B in B if B!=A)
def ZU(A):return max(enumerate(A))[1]
def PM(A):return next(iter(A))
def R(A,B):return type(A)(A for A in A if B(A))
def L(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def Q(A):return frozenset({A})
def PU(A,B):return min(A,key=B)
def ZS(A):return len(A)
def PQ(A,B):return tuple(sorted(A,key=B))
def P(a,b):return a&b
def PJ(a,b):return type(a)((*a,*b))
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZE(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def W(x):return x
def p(I):F=False;I=tuple(map(tuple,I));A=K(I,F,F,True);N=ZP(PK,5);O=PZ(N,H);S=ZJ(G,O,W);T=ZZ(S,A);U=PQ(T,V);X=PZ(ZU,ZU);B=PR(PP,X);a=PZ(B,V);b=PZ(B,Y);c=ZJ(R,W,a);d=ZJ(R,W,b);e=PZ(Z,ZU);f=ZP(PV,e);g=PR(f,ZS);h=PR(ZP,P);C=PV(g,h,J);i=ZJ(PU,c,C);j=ZJ(PU,d,C);k=PZ(ZU,i);l=PZ(ZU,j);m=PS(0,(1,-1));n=Q(m);o=PR(ZE,(0,1));p=PV(k,PM,ZU);q=PZ(l,PM);r=ZJ(M,q,p);D=PZ(PM,ZU);s=PZ(o,r);t=ZJ(PW,D,s);u=ZJ(PJ,PM,t);v=ZJ(PX,D,ZU);w=ZJ(PS,u,v);x=ZS(A);y=PY(w,x);z=PS(n,U);A0=y(z);E=PM(A0);A1=PL(E);A2=L(A1);A3=PS(3,A2);A4=PE(0,A3);A5=PH(A4,E);return[*map(list,A5)]
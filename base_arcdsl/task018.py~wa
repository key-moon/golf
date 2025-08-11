_A=False
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def H(A):return tuple(map(max,zip(*U(A))))
def ZR(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A):return max(A for(A,B)in U(A))
def W(A):return min(A for(A,B)in U(A))
def ZV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return max(A for(B,A)in U(A))
def R(A):return min(A for(B,A)in U(A))
def ZJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Q(A)-R(A)+1
def PH(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-W(A)+1
def ZX(A):return PH(A),ZJ(A)
def P(A,B):
	C=set();L=E(B);D,F=len(A),len(A[0]);M,N=ZX(B);O,P=D-M+1,F-N+1
	for G in range(O):
		for H in range(P):
			I=True
			for(Q,(J,K))in ZY(L,(G,H)):
				if not(0<=J<D and 0<=K<F and A[J][K]==Q):I=_A;break
			if I:C.add((G,H))
	return frozenset(C)
def ZE(A,B):return ZR(A,Y(A),U(B))
def ZW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PY(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return PS(PG(PS(A)))
def PG(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=K(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PS(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=K(A)[1]+H(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PX(A):
	if isinstance(A,tuple):return A[::-1]
	B=K(A)[0]+H(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def L(A):return len(PL(A))
def PL(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PZ(A,B,C,D):
	K=Y(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=X(A);R=V if C else S
	for E in Q:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		M={(H,E)};I={E}
		while len(I)>0:
			N=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:M.add((J,F));G.add(F);N|={(A,B)for(A,B)in R(F)if 0<=A<O and 0<=B<P}
			I=N-G
		L.add(frozenset(M))
	return frozenset(L)
def E(A):
	if len(A)==0:return A
	return ZY(A,(-W(A),-R(A)))
def ZY(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def K(A):return tuple(map(min,zip(*U(A))))
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def ZP(A,B):return ZS(ZG(A,B))
def PK(A,B):return type(A)(A(B)for A in A)
def ZG(A,B):return type(B)(A(B)for B in B)
def ZK(A,a,b):return lambda x:A(a(x),b(x))
def ZM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def ZU(h,g,f):return lambda x:h(g(f(x)))
def PV(A,B):return lambda x:A(B(x))
def PU(a,b):return frozenset((B,A)for A in b for B in a)
def PM(a,b):return a,b
def ZZ(A,B):return type(B)(B for B in B if B!=A)
def ZH(A):return max(enumerate(A))[1]
def ZL(A):return next(iter(A))
def PQ(A):return tuple(A)
def PJ(A,B):return type(A)(A for A in A if B(A))
def PR(A,B):return max(A,key=B)
def ZS(A):return type(A)(B for A in A for B in A)
def PE(a,b):return a>b
def PW(a,b):return type(a)((*a,*b))
def M(A,B):return A in B
def PP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));F=PL(I);G=PZ(I,_A,_A,True);H=ZQ(PE,1);J=PV(H,L);B=PJ(G,J);C=ZZ(0,F);N=ZM(Z,I);O=PR(C,N);Q=ZZ(O,C);R=ZQ(M,Q);S=PV(R,ZL);D=ZQ(PJ,S);T=ZM(ZQ,PP);U=ZM(P,I);V=ZM(ZM,ZY);W=PV(T,K);X=ZU(W,D,E);Y=ZU(U,D,E);a=ZK(ZG,X,Y);b=PV(V,E);c=ZK(ZP,b,a);d=PM(PY,PG);e=PM(PX,PS);A=PW(d,e);f=PU(A,A);g=ZK(PV,ZL,ZH);h=ZG(g,f);i=PQ(h);j=PW(A,i);k=ZM(PK,j);l=ZP(k,B);m=ZP(c,l);n=ZW(I,m);o=ZS(B);p=ZE(n,o);return[*map(list,p)]
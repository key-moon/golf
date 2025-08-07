def ZS(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PL(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def H(A):return tuple(map(max,zip(*U(A))))
def G(A):return tuple(map(min,zip(*U(A))))
def Q(A):return max(A for(A,B)in U(A))
def M(A):return min(A for(A,B)in U(A))
def ZX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return max(A for(B,A)in U(A))
def K(A):return min(A for(B,A)in U(A))
def ZZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-M(A)+1
def ZJ(A):return PR(A),ZZ(A)
def P(A,B):
	C=set();L=E(B);D,F=len(A),len(A[0]);M,N=ZJ(B);O,P=D-M+1,F-N+1
	for G in range(O):
		for H in range(P):
			I=True
			for(Q,(J,K))in ZE(L,(G,H)):
				if not(0<=J<D and 0<=K<F and A[J][K]==Q):I=False;break
			if I:C.add((G,H))
	return frozenset(C)
def PW(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for J in A:
			D=tuple()
			for E in J:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,H=G(A);K,L=-F,-H;M=ZE(A,(K,L));I=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):I.add((E,(N*B+P,O*B+Q)))
		return ZE(frozenset(I),(F,H))
def ZY(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PY(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return PJ(PQ(PJ(A)))
def PQ(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=G(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PJ(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=G(A)[1]+H(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PX(A):
	if isinstance(A,tuple):return A[::-1]
	B=G(A)[0]+H(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def L(A):return len(PL(A))
def PS(A,B,C,D):
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
	return ZE(A,(-M(A),-K(A)))
def ZE(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PH(A,B):return ZS(ZM(A,B))
def PG(A,B):return type(A)(A(B)for A in A)
def ZM(A,B):return type(B)(A(B)for B in B)
def ZW(A,a,b):return lambda x:A(a(x),b(x))
def ZL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PV(A,B):return lambda x:A(x)==B
def PM(A,B):return lambda x:A(B(x))
def PE(a,b):return frozenset((B,A)for A in b for B in a)
def R(A,B,C):return tuple(range(A,B,C))
def ZP(A,B):return B.union(frozenset({A}))
def ZQ(A):return max(enumerate(A))[1]
def ZU(A):return next(iter(A))
def PU(A,B):return type(A)(A for A in A if B(A))
def PZ(A):return frozenset({A})
def PK(A,B):return max(A,key=B)
def Z(a,b):return type(a)(A for A in a if A not in b)
def PP(x):return x
def p(I):I=tuple(map(tuple,I));A=PS(I,False,True,True);B=PK(A,L);C=E(B);D=ZL(PV,ZU);F=PM(D,Y);G=ZW(PU,PP,F);H=ZW(Z,PP,G);J=ZL(ZV,PW);K=R(1,4,1);M=ZM(J,K);N=PZ(PP);O=ZP(PJ,N);Q=ZP(PX,O);S=ZP(PY,Q);T=ZP(PQ,S);U=ZW(PM,ZU,ZQ);V=ZL(P,I);W=ZL(ZL,ZE);X=PM(V,H);a=PE(T,M);b=ZM(U,a);c=PG(b,C);d=ZW(PH,W,X);e=PH(d,c);f=ZY(I,e);return[*map(list,f)]
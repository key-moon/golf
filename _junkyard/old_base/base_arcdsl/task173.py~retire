def PY(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PU(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Q(A):return max(A for(A,B)in U(A))
def M(A):return min(A for(A,B)in U(A))
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return max(A for(B,A)in U(A))
def K(A):return min(A for(B,A)in U(A))
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-M(A)+1
def PV(A):return PE(A),PL(A)
def P(A,B):
	C=set();L=E(B);D,F=len(A),len(A[0]);M,N=PV(B);O,P=D-M+1,F-N+1
	for G in range(O):
		for H in range(P):
			I=True
			for(Q,(J,K))in PW(L,(G,H)):
				if not(0<=J<D and 0<=K<F and A[J][K]==Q):I=False;break
			if I:C.add((G,H))
	return frozenset(C)
def PK(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def L(A):return len(PU(A))
def PP(A,B,C,D):
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
	return PW(A,(-M(A),-K(A)))
def PW(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A):return tuple(map(min,zip(*U(A))))
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PX(A,B):return PY(PH(A,B))
def PH(A,B):return type(B)(A(B)for B in B)
def ZP(A,a,b):return lambda x:A(a(x),b(x))
def PG(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PS(A,B):return lambda x:A(x)==B
def PJ(A,B):return lambda x:A(B(x))
def PM(A):return next(iter(A))
def PZ(A,B):return type(A)(A for A in A if B(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZZ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def H(x):return x
def p(I):I=tuple(map(tuple,I));A=PP(I,False,True,True);K=PS(L,1);M=PZ(A,K);B=Z(A,M);N=PG(PS,PM);O=PJ(N,Y);C=ZP(PZ,H,O);D=ZP(Z,H,C);F=PG(P,I);Q=PJ(F,C);S=PJ(F,D);T=PJ(G,D);U=ZP(R,G,T);V=PG(PR,ZZ);W=PJ(V,U);X=ZP(PH,W,S);a=PG(PG,PW);J=PJ(a,E);b=ZP(PX,J,Q);c=ZP(PX,J,X);d=PX(b,B);e=PX(c,B);f=PK(I,d);g=PK(f,e);return[*map(list,g)]
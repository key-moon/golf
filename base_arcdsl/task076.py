_A=False
def ZP(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PE(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def R(A):return tuple(map(max,zip(*J(A))))
def Q(A):return max(A for(A,B)in J(A))
def M(A):return min(A for(A,B)in J(A))
def ZE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return max(A for(B,A)in J(A))
def K(A):return min(A for(B,A)in J(A))
def PH(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PK(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-M(A)+1
def ZS(A):return PK(A),PH(A)
def P(A,B):
	C=set();K=U(B);D,E=len(A),len(A[0]);L,M=ZS(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in ZU(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=_A;break
			if H:C.add((F,G))
	return frozenset(C)
def ZL(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PX(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return PZ(PW(PZ(A)))
def PW(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=G(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PZ(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=G(A)[1]+R(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PU(A):
	if isinstance(A,tuple):return A[::-1]
	B=G(A)[0]+R(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def X(A):return len(PE(A))
def PP(A,B,C,D):
	M=L(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=Y if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def U(A):
	if len(A)==0:return A
	return ZU(A,(-M(A),-K(A)))
def ZU(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A):return tuple(map(min,zip(*J(A))))
def PR(A,B):return ZP(ZV(A,B))
def PQ(A,B):return type(A)(A(B)for A in A)
def ZV(A,B):return type(B)(A(B)for B in B)
def ZM(A,a,b):return lambda x:A(a(x),b(x))
def ZX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def ZZ(h,g,f):return lambda x:h(g(f(x)))
def PL(A,B):return lambda x:A(B(x))
def PJ(a,b):return frozenset((B,A)for A in b for B in a)
def PY(a,b):return a,b
def ZW(A):return max(enumerate(A))[1]
def ZJ(A):return next(iter(A))
def PM(A):return tuple(A)
def PS(A,B):return type(A)(A for A in A if B(A))
def PG(A,B):return max(A,key=B)
def PV(a,b):return type(a)((*a,*b))
def V(A,B):return A in B
def H(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));C=PP(I,_A,_A,True);D=PG(C,X);E=PY(2,4);F=ZY(V,E);J=PL(F,ZJ);B=ZY(PS,J);K=ZX(ZY,H);L=ZX(P,I);M=ZX(ZX,ZU);N=PL(K,G);O=ZZ(N,B,U);Q=ZZ(L,B,U);R=ZM(ZV,O,Q);S=PL(M,U);T=ZM(PR,S,R);W=PY(PX,PW);Y=PY(PU,PZ);A=PV(W,Y);Z=PJ(A,A);a=ZM(PL,ZJ,ZW);b=ZV(a,Z);c=PM(b);d=PV(A,c);e=PQ(d,D);f=PR(T,e);g=ZL(I,f);return[*map(list,g)]
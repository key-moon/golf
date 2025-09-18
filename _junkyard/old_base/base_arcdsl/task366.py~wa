_A=False
def W(A):return max(A for(B,A)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PU(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def ZM(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Q(A):return max(A for(A,B)in J(A))
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def ZS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A):return min(A for(B,A)in J(A))
def V(A):return min(A for(A,B)in J(A))
def U(A):
	if len(A)==0:return A
	return ZP(A,(-V(A),-K(A)))
def PR(A):return PM(A),PQ(A)
def P(A,B):
	C=set();K=U(B);D,E=len(A),len(A[0]);L,M=PR(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in ZP(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=_A;break
			if H:C.add((F,G))
	return frozenset(C)
def PV(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(ZM(A,(B*C+C*E,0),(B,D))for C in range(n))
def PW(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(ZM(A,(0,B*C+C*E),(D,B))for C in range(n))
def ZU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def X(A):return len(PU(A))
def PS(A,B,C,D):
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
def ZP(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A):return tuple(map(min,zip(*J(A))))
def H(A):return PM(A)>PQ(A)
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def ZX(A,B):return type(B)(A(B)for B in B)
def ZY(A,a,b):return lambda x:A(a(x),b(x))
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
def PE(A,B):return lambda x:A(x)==B
def PK(h,g,f):return lambda x:h(g(f(x)))
def PL(A,B):return lambda x:A(B(x))
def PY(A,a,b):return a if A else b
def ZW(A):return max(enumerate(A))[1]
def PH(A):return next(iter(A))
def PX(A,B):return PG(PJ(A,B))
def PJ(A,B):return type(A)(A for A in A if B(A))
def R(x):return x>0
def M(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PG(A):return type(A)(B for A in A for B in A)
def ZL(A):return len(A)
def ZZ(A,B):return tuple(sorted(A,key=B))
def ZV(b):return not b
def PP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def PZ(x):return x
def p(I):I=tuple(map(tuple,I));F=H(I);J=PY(F,PV,PW);K=J(I,2);B=ZZ(K,X);C=PH(B);N=ZW(B);D=PS(N,_A,_A,True);O=PG(D);Q=L(O);S=PE(PH,Q);T=PL(ZV,S);A=ZE(PJ,T);E=ZJ(P,C);U=PL(E,A);V=PK(R,ZL,U);W=PJ(D,V);Y=PK(PH,E,A);Z=PL(G,A);a=ZY(PP,Y,Z);b=ZY(ZP,PZ,a);c=ZX(b,W);d=PL(M,PQ);e=PK(R,M,d);f=PX(c,e);g=ZU(C,f);return[*map(list,g)]
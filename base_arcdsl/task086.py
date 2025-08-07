def PG(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|J(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PZ(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def H(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def R(A):return tuple(map(max,zip(*U(A))))
def Q(A):return tuple(map(min,zip(*U(A))))
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def W(A):return max(A for(A,B)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def PY(A):F,H=Y(A)-1,G(A)-1;I,J=W(A)+1,V(A)+1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def ZJ(A):F,H=Y(A)+1,G(A)+1;I,J=W(A)-1,V(A)-1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def K(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=Q(B);E,F=R(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PS(A):return frozenset({Q(A),H(A),PZ(A),R(A)})
def PV(A,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in A)
def M(A,B,C):
	G,H=len(A),len(A[0]);I=X(A);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def ZX(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PU(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
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
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-G(A)+1
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PM(A,B):return PG(ZU(A,B))
def PL(A,B):return type(A)(A(B)for A in A)
def ZU(A,B):return type(B)(A(B)for B in B)
def ZE(A,a,b):return lambda x:A(a(x),b(x))
def PK(A,n):
	if n==1:return A
	return PE(A,PK(A,n-1))
def ZS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PR(h,g,f):return lambda x:h(g(f(x)))
def PE(A,B):return lambda x:A(B(x))
def ZZ(A,B):return PH(PW(B,A))
def PW(A,B):return type(B)(B for B in B if B!=A)
def PH(A):return next(iter(A))
def PJ(A):return frozenset({A})
def P(a,b):return a&b
def PP(x):return x
def p(I):F=False;I=tuple(map(tuple,I));B=PU(I,F,F,True);C=S(I);G=PX(I);H=PW(0,G);D=ZZ(H,C);J=PV(I,C,D);L=PE(PQ,ZJ);N=ZS(PK,PY);E=PE(N,L);O=PJ(E);Q=ZS(PL,O);R=PR(PJ,PH,Q);T=ZE(PL,R,PP);U=PE(PH,T);A=PE(K,U);V=ZS(PR,K);W=ZS(V,ZJ);X=PE(W,E);Y=ZS(ZU,PJ);Z=PR(Y,PS,A);a=ZE(PM,X,Z);b=ZE(P,A,a);c=PM(A,B);d=PM(b,B);e=M(J,D,c);f=ZX(e,0,d);return[*map(list,f)]
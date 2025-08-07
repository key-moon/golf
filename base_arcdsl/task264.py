def ZZ(A):return type(A)(B for A in A for B in A)
def ZU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def ZP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PG(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def PZ(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def R(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def M(A):return max(A for(B,A)in J(A))
def G(A):return min(A for(B,A)in J(A))
def W(A):return max(A for(A,B)in J(A))
def V(A):return min(A for(A,B)in J(A))
def K(A):return tuple(map(max,zip(*J(A))))
def ZQ(A):
	if len(A)==0:return A
	F,G=Q(A);H,I=K(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|L)
def PQ(A):F,H=V(A)-1,G(A)-1;I,J=W(A)+1,M(A)+1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def ZX(A):F,H=V(A)+1,G(A)+1;I,J=W(A)-1,M(A)-1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PS(A):return frozenset({Q(A),R(A),PZ(A),K(A)})
def PR(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PH(A):return V(A)+PG(A)//2,G(A)+ZP(A)//2
def PM(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def ZL(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def ZW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
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
def U(A):
	if len(A)==0:return A
	return ZJ(A,(-V(A),-G(A)))
def ZJ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return tuple(map(min,zip(*J(A))))
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PK(A,B):return ZZ(ZV(A,B))
def ZV(A,B):return type(B)(A(B)for B in B)
def ZM(A,a,b):return lambda x:A(a(x),b(x))
def ZE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PL(A,B):return lambda x:A(x)==B
def ZS(h,g,f):return lambda x:h(g(f(x)))
def PY(A,B):return lambda x:A(B(x))
def PV(a,b):return a,b
def PX(A,B):return next(A for A in A if B(A))
def PE(A,B):return type(A)(A for A in A if B(A))
def PJ(A):return frozenset({A})
def P(a,b):return type(a)(A for A in a if A not in b)
def PW(a,b):return type(a)((*a,*b))
def Y(A,B):return A in B
def H(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def PP(x):return x
def p(I):F=False;A=True;I=tuple(map(tuple,I));G=PM(I,5,0);K=PU(G,A,F,A);L=ZV(U,K);M=PV(9,9);B=PR(5,M);C=E(B);D=ZQ(C);N=PH(C);O=ZE(Y,0);R=ZY(H,N);S=PY(O,R);T=ZS(PQ,PQ,PJ);V=PS(C);W=PK(T,V);X=P(D,W);Z=ZX(D);a=PE(Z,S);b=PW(X,a);c=ZW(B,1,b);d=PU(c,A,F,A);e=ZV(J,d);f=ZE(PL,U);g=ZE(PX,e);h=ZS(Q,g,f);i=PY(h,J);j=ZM(ZJ,PP,i);k=PK(j,L);l=ZL(B,k);return[*map(list,l)]
def PY(A):return type(A)(B for A in A for B in A)
def PG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def PQ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-Q(A)+1
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def ZZ(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PM(A):return PX(A),PL(A)
def V(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def M(A):return max(A for(A,B)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def G(A):return tuple(map(max,zip(*J(A))))
def W(A):return tuple(map(min,zip(*J(A))))
def ZS(A):
	if len(A)==0:return A
	F,H=W(A);I,J=G(A);B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PK(A):F,G=Y(A)+1,Q(A)+1;H,I=M(A)-1,V(A)-1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def PZ(A,B):return ZZ(B,W(A),PM(A))
def PH(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def K(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PV(A):return next(iter(A))[0]
def H(A,B,C,D):
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
	return PQ(A,(-Y(A),-Q(A)))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PR(A,a,b):return lambda x:A(a(x),b(x))
def PJ(A,B):return lambda x:A(x)==B
def PE(A,B):return lambda x:A(B(x))
def PW(A):return next(iter(A))
def PS(A,B):return next(A for A in A if B(A))
def PU(A,B):return PY(PP(A,B))
def PP(A,B):return type(A)(A for A in A if B(A))
def R(a,b):return a==b
def ZP(b):return not b
def p(I):I=tuple(map(tuple,I));A=H(I,True,False,True);C=P(A,5);D=PR(R,J,ZS);E=PS(C,D);F=PK(E);G=PZ(F,I);L=K(G);M=PJ(PW,0);N=PE(ZP,M);O=PP(L,N);B=U(O);Q=J(B);S=PE(J,U);T=PJ(S,Q);V=PU(A,T);W=PV(B);X=PH(I,W,V);return[*map(list,X)]
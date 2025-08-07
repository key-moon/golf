def PJ(A,B):return type(B)(A(B)for B in B)
def R(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):return next(iter(A))[0]
def X(a,b):return len(set(A for(B,A)in U(a))&set(A for(B,A)in U(b)))>0
def M(A,B,C,D):
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
def V(A,B):return frozenset((A,B)for B in U(B))
def J(A,n):return frozenset(A for A in A if len(A)==n)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def K(A,B):return R(PJ(A,B))
def PU(A,a,b):return lambda x:A(a(x),b(x))
def G(A,B):return lambda x:A(B(x))
def Q(a,b):return frozenset((B,A)for A in b for B in a)
def PE(A):return max(enumerate(A))[1]
def PP(A):return next(iter(A))
def W(A,B):return type(A)(A for A in A if B(A))
def p(I):I=tuple(map(tuple,I));A=M(I,True,False,True);B=J(A,1);C=P(A,5);D=Q(B,C);E=PU(X,PP,PE);F=W(D,E);L=G(H,PP);N=PU(V,L,PE);O=K(N,F);R=PS(I,O);return[*map(list,R)]
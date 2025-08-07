def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(max,zip(*U(A))))
def L(A):return tuple(map(min,zip(*U(A))))
def V(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=L(B);E,F=Y(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def H(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def G(A):return next(iter(A))[0]
def M(A,B,C,D):
	M=J(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=X if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			P=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			K=P-H
		N.add(frozenset(O))
	return frozenset(N)
def Q(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def K(A,B):return type(B)(A(B)for B in B)
def W(A):return tuple(A)
def P(A):return max(set(A),key=A.count)
def p(I):I=tuple(map(tuple,I));B=M(I,True,False,True);C=W(B);D=K(G,C);A=P(D);E=Q(I,A);F=V(E);J=H(I,A,F);return[*map(list,J)]
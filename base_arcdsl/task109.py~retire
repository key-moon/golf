def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|S(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def V(A):return tuple(map(max,zip(*U(A))))
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(min,zip(*U(A))))
def G(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Y(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def M(A):B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);C=tuple(A for(A,B)in enumerate(G(A))if len(set(B))==1);return tuple(tuple(B for(A,B)in enumerate(D)if A not in C)for(A,D)in enumerate(A)if A not in B)
def R(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def L(a,b,A):
	G,H=len(a),len(a[0]);B=tuple()
	for D in range(G):
		C=tuple()
		for E in range(H):F=a[D][E];I=F if F==b[D][E]else A;C=C+(I,)
		B=B+(C,)
	return B
def K(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Y(A)[1]+V(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def W(A):
	if isinstance(A,tuple):return A[::-1]
	B=Y(A)[0]+V(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def Q(A,B,C,D):
	M=J(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=E(A);U=X if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in U(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def H(A):return type(A)(B for A in A for B in A)
def p(I):B=True;I=tuple(map(tuple,I));A=Z(I);D=K(I);E=Q(I,B,B,B);F=H(E);G=J(F);C=L(I,D,A);N=W(C);O=L(C,N,A);P=M(O);S=R(P,A,G);return[*map(list,S)]
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PU(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Y(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def M(A):return min(A for(B,A)in S(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-M(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PX(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def V(A):return tuple(map(min,zip(*S(A))))
def PJ(A):return PP(A),PZ(A)
def W(a,b,A):
	G,H=len(a),len(a[0]);B=tuple()
	for D in range(G):
		C=tuple()
		for E in range(H):F=a[D][E];I=F if F==b[D][E]else A;C=C+(I,)
		B=B+(C,)
	return B
def G(A,B):return PX(B,V(A),PJ(A))
def R(a,b):return a+b
def K(a,b):return tuple(A+B for(A,B)in zip(a,b))
def H(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=V(A);J,K=-F,-G;L=PU(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return PU(frozenset(H),(F,G))
def Q(A,B,C,D):
	M=U(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);V=E if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in V(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def PS(A):return type(A)(B for A in A for B in A)
def p(I):I=tuple(map(tuple,I));C=Q(I,True,False,True);D=PS(C);A=G(D,I);E=H(A,3);F=K(A,A);B=K(F,A);J=R(B,B);L=R(J,B);M=W(E,L,0);return[*map(list,M)]
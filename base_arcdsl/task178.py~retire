def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(map(min,zip(*S(A))))
def W(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=X(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def R(A):return next(iter(A))[0]
def L(A):return min(A for(B,A)in S(A))
def M(A,B,C,D):
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
def PJ(A,B):return type(B)(A(B)for B in B)
def H(h,g,f):return lambda x:h(g(f(x)))
def G(A,a,b):return a if A else b
def PP(A):return next(iter(A))
def PU(A):return len(A)
def K(A,B):return tuple(A for B in range(B))
def PZ(A,B):return tuple(sorted(A,key=B))
def Q(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def V(a,b):return a==b
def Y(x):return x
def p(I):B=False;I=tuple(map(tuple,I));C=H(PU,Q,PP);D=C(I);E=V(D,1);A=G(E,W,Y);F=A(I);J=M(F,True,B,B);N=PZ(J,L);O=PJ(R,N);P=K(O,1);S=A(P);return[*map(list,S)]
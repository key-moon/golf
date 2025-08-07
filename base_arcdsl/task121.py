def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PP(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def V(A):return max(A for(A,B)in S(A))
def L(A):return min(A for(A,B)in S(A))
def Y(A):return max(A for(B,A)in S(A))
def W(A):return min(A for(B,A)in S(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PE(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def M(A):return tuple(map(min,zip(*S(A))))
def PJ(A):return PZ(A),PS(A)
def H(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def G(A,B):return PE(B,M(A),PJ(A))
def U(A):return len(PP(A))
def Q(A,B,C,D):
	M=E(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);U=X if C else P
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
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(A,B):return lambda x:A(x)==B
def K(A,B):return next(A for A in A if B(A))
def p(I):I=tuple(map(tuple,I));B=Q(I,False,True,True);C=R(U,2);A=K(B,C);D=G(A,I);F=E(A);J=H(D,8,F);return[*map(list,J)]
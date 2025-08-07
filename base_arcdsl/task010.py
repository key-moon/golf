def G(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def R(A):return type(A)(B for A in A for B in A)
def L(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PZ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
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
def V(A,B):return frozenset((A,B)for B in S(B))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-X(A)+1
def W(A,a,b):return R(G(A,a,b))
def Y(A,B,C):return tuple(range(A,B,C))
def Q(A):return tuple(A)
def PS(A):return len(A)
def H(A,B):return tuple(sorted(A,key=B))
def p(I):I=tuple(map(tuple,I));A=M(I,True,False,True);B=Q(A);C=H(A,K);D=PS(B);E=Y(D,0,-1);F=W(V,E,C);G=PZ(I,F);return[*map(list,G)]
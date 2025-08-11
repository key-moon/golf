def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def P(A):return A[len(A)//2+len(A)%2:]
def X(A):return A[:len(A)//2]
def V(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def L(A,B,C,D):
	M=J(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=E if C else Z
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
def Y(A):return type(A)(B for A in A for B in A)
def p(I):I=tuple(map(tuple,I));A=X(I);B=P(I);C=L(A,True,False,True);D=Y(C);E=V(B,D);return[*map(list,E)]
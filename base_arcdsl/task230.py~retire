def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def H(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return max(A for(B,A)in S(A))
def M(A):return min(A for(B,A)in S(A))
def Y(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def R(A):F,G=X(A)-1,M(A)-1;H,I=Y(A)+1,L(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def PZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def K(A,B,C,D):
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
def W(A):return tuple(map(max,zip(*S(A))))
def G(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def Q(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def V(A):return tuple(map(min,zip(*S(A))))
def PP(A,B):return type(B)(A(B)for B in B)
def p(I):I=tuple(map(tuple,I));B=K(I,True,False,True);A=PP(R,B);C=PP(V,A);D=PP(Q,A);E=PP(G,A);F=PP(W,A);H=PZ(I,1,C);J=PZ(H,2,D);L=PZ(J,3,E);M=PZ(L,4,F);return[*map(list,M)]
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PZ(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def M(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def Q(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PZ(A,(0,B*C+C*E),(D,B))for C in range(n))
def PP(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def L(A,B,C,D):
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
def R(A,B):return type(B)(A(B)for B in B)
def Y(a,b):return a,b
def X(A,B,C):return tuple(range(A,B,C))
def W(j):return 0,j
def G(A):return type(A)(B for A in A for B in A)
def H(A):return len(A)
def V(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def p(I):I=tuple(map(tuple,I));A=L(I,True,False,True);B=H(A);C=V(B);D=X(0,C,2);E=R(W,D);F=Y(1,9);J=M(0,F);K=PP(J,1,E);N=Q(K,3);O=G(N);return[*map(list,O)]
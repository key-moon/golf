def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return J(A)|U(A)
def J(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def L(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def X(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in X(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def V(A,B,C,D):
	N=E(A)if D else None;O=set();H=set();R,S=len(A),len(A[0]);T=L(A);U=Y if C else J
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==N:continue
		P={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				M=A[G[0]][G[1]]
				if I==M if B else M!=N:P.add((M,G));H.add(G);Q|={(A,B)for(A,B)in U(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		O.add(frozenset(P))
	return frozenset(O)
def S(A,n):return frozenset(A for A in A if len(A)==n)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def M(A):return type(A)(B for A in A for B in A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):B=False;I=tuple(map(tuple,I));C=V(I,True,B,B);A=P(C,3);D=S(A,1);E=Z(A,D);F=M(E);G=Q(I,8,F);return[*map(list,G)]
def G(A,B):return type(A)(A for A in A if B(A))
def PP(A):return type(A)(B for A in A for B in A)
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return max(A for(A,B)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def V(A):return max(A for(B,A)in U(A))
def W(A):return min(A for(B,A)in U(A))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-W(A)+1
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def PJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PZ(A):return H(A)==len(A)and R(A)==1
def Q(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def J(A,n):return frozenset(A for A in A if len(A)==n)
def K(A,B):return PP(G(A,B))
def P(a,b):return type(a)(A for A in a if A not in b)
def p(I):B=False;I=tuple(map(tuple,I));C=E(I);D=Q(I,True,B,B);F=J(D,3);G=K(F,PZ);A=U(G);H=P(C,A);L=PJ(I,5,A);M=PJ(L,0,H);return[*map(list,M)]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|S(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(max,zip(*U(A))))
def L(A):return tuple(map(min,zip(*U(A))))
def R(A):
	if len(A)==0:return A
	F,G=L(A);H,I=Y(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def V(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=L(B);E,F=Y(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def W(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def K(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A,B,C,D):
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
def Q(A):return type(A)(B for A in A for B in A)
def p(I):I=tuple(map(tuple,I));D=M(I,True,False,True);A=W(I,8,0);B=Z(A);E=W(A,B,0);F=Z(E);C=Q(D);G=V(C);H=R(C);J=K(I,B,G);L=K(J,F,H);return[*map(list,L)]
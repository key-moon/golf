def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def L(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def V(A):return tuple(map(max,zip(*E(A))))
def Y(A):return tuple(map(min,zip(*E(A))))
def M(A):
	if len(A)==0:return frozenset({})
	B=E(A);C,D=Y(B);F,G=V(A);return frozenset((A,B)for A in range(C,F+1)for B in range(D,G+1))
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(B):
	if len(B)==0:return frozenset({})
	return M(B)-E(B)
def H(A,B,C):
	H,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:D[F][G]=B
	return tuple(tuple(A)for A in D)
def W(A,B,C,D):
	K=U(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=L(A);T=X if C else S
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def X(A):return S(A)|J(A)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def K(A):return next(iter(A))
def G(A):return type(A)(B for A in A for B in A)
def p(I):I=tuple(map(tuple,I));A=Z(I);B=W(I,True,False,True);C=P(B,A);D=G(C);E=Q(D);F=K(E);J=X(F);L=H(I,4,J);return[*map(list,L)]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def W(A):return min(A for(B,A)in J(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PL(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PJ(A):return PZ(A),PS(A)
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def G(A):return tuple(map(max,zip(*J(A))))
def M(A):return tuple(map(min,zip(*J(A))))
def Q(A):
	if len(A)==0:return frozenset({})
	B=J(A);C,D=M(B);E,F=G(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PE(B):
	if len(B)==0:return frozenset({})
	return Q(B)-J(B)
def R(A,B):return PL(B,M(A),PJ(A))
def K(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=U(A);S=X if C else Z
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in S(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def H(A,B):return lambda x:A(B(x))
def PP(A,B):return max(A,key=B)
def PX(A):return len(A)
def p(I):A=False;I=tuple(map(tuple,I));B=K(I,True,A,A);C=P(B,1);D=H(PX,PE);E=PP(C,D);F=R(E,I);return[*map(list,F)]
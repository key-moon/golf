def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|U(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in E(A))
def V(A):return min(A for(A,B)in E(A))
def M(A):return max(A for(B,A)in E(A))
def G(A):return min(A for(B,A)in E(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PL(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Q(A):return tuple(map(min,zip(*E(A))))
def PU(A):return PZ(A),PS(A)
def H(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def R(A,B):return PL(B,Q(A),PU(A))
def PJ(A):return next(iter(A))[0]
def K(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);T=Y if C else S
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
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PP(A,B):return max(A,key=B)
def PX(A):return len(A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));A=J(I);B=K(I,True,False,True);D=P(B,A);E=Z(B,D);C=PP(E,PX);F=PJ(C);G=R(C,I);L=H(G,F,A);return[*map(list,L)]
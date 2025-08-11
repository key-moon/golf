def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in U(A))
def M(A):return max(A for(B,A)in U(A))
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in U(A))
def V(A):return min(A for(A,B)in U(A))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def R(A):return V(A)+K(A)//2,Q(A)+H(A)//2
def PJ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def G(A,B,C,D):
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
def E(A):
	if len(A)==0:return A
	return PZ(A,(-V(A),-Q(A)))
def PZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PP(A):return next(iter(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):C=False;I=tuple(map(tuple,I));A=G(I,C,C,True);B=P(A,5);D=PP(B);F=R(D);H=Z(A,B);J=PP(H);K=E(J);L=PZ(K,F);M=PZ(L,(-1,-1));N=PJ(I,M);return[*map(list,N)]
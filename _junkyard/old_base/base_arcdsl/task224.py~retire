def M(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Z(A)-X(A)+1
def V(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-J(A)+1
def R(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def E(A):return tuple(map(min,zip(*S(A))))
def Q(A):return V(A),M(A)
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return max(A for(B,A)in S(A))
def X(A):return min(A for(B,A)in S(A))
def U(A):return max(A for(A,B)in S(A))
def J(A):return min(A for(A,B)in S(A))
def W(A):F,G=J(A)+1,X(A)+1;H,I=U(A)-1,Z(A)-1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def K(A):return tuple(A[1:-1]for A in A[1:-1])
def L(A,B):return R(B,E(A),Q(A))
def H(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def p(I):I=tuple(map(tuple,I));A=Y(I,5);B=L(A,I);C=K(B);D=P(C);E=W(A);F=H(I,D,E);return[*map(list,F)]
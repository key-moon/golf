def E(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def S(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(X(A,(0,B*C+C*E),(D,B))for C in range(n))
def L(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Z(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def J(A,B):return type(B)(B for B in B if B!=A)
def Y(A):return max(enumerate(A))[1]
def U(A):return next(iter(A))
def p(I):I=tuple(map(tuple,I));A=S(I,3);B=U(A);C=J(B,A);D=U(C);E=Y(C);F=Z(D,9);G=Z(B,4);H=L(E,9,F);K=L(H,4,G);return[*map(list,K)]
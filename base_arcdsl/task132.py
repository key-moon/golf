def Q(A,B):return type(B)(A(B)for B in B)
def V(A):return type(A)(B for A in A for B in A)
def L(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):return tuple(map(max,zip(*S(A))))
def J(A):return tuple(map(min,zip(*S(A))))
def E(A):
	if len(A)==0:return frozenset({})
	B=S(A);C,D=J(B);E,F=U(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def W(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def M(A):return next(iter(A))[0]
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in L(A)-{Z(A)})
def X(A,B):return frozenset((A,B)for B in S(B))
def Y(A,B):return V(Q(A,B))
def K(A,a,b):return lambda x:A(a(x),b(x))
def p(I):I=tuple(map(tuple,I));A=P(I);B=K(X,M,E);C=Y(B,A);D=W(I,C);return[*map(list,D)]
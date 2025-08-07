def X(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def V(A):return type(A)(B for A in A for B in A)
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def W(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def M(A):return next(iter(A))[0]
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in E(A))
def U(A,B):return frozenset((A,B)for B in Z(B))
def J(A,a,b):return V(X(A,a,b))
def Q(A,B):return type(B)(A(B)for B in B)
def Y(A,B):return type(B)(B for B in B if B!=A)
def H(A):return max(enumerate(A))[1]
def R(A):return len(A)
def L(A,B):return tuple(A for B in range(B))
def G(A,B):return tuple(sorted(A,key=B))
def S(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=P(I);A=G(C,R);D=Q(M,A);B=H(A);E=Y(B,A);F=L(B,1);K=S(F,E);N=J(U,D,K);O=W(I,N);return[*map(list,O)]
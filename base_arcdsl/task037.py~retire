def Q(A,B):return type(B)(A(B)for B in B)
def Y(A):return type(A)(B for A in A for B in A)
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def E(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def M(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def V(A):return next(iter(A))[0]
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in X(A)-{Z(A)})
def U(A,B):return frozenset((A,B)for B in S(B))
def L(A,B):return Y(Q(A,B))
def H(A,a,b):return lambda x:A(a(x),b(x))
def G(A,n):
	if n==1:return A
	return J(A,G(A,n-1))
def J(A,B):return lambda x:A(B(x))
def R(A):return max(enumerate(A))[1]
def W(A):return next(iter(A))
def p(I):I=tuple(map(tuple,I));A=P(I);B=J(R,W);C=G(R,2);D=H(E,B,C);F=H(U,V,D);K=L(F,A);N=M(I,K);return[*map(list,N)]
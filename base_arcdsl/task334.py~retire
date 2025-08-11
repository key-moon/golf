def Y(A,B):return type(B)(B for B in B if B!=A)
def M(A):return next(iter(A))
def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return frozenset((A[0],B)for B in range(30))
def Z(A):return frozenset((B,A[1])for B in range(30))
def X(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def Q(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def G(A,a,b):return lambda x:A(a(x),b(x))
def L(A,a,b):return a if A else b
def V(A,B):return M(Y(B,A))
def U(a,b):return type(a)((*a,*b))
def J(a,b):return a==b
def p(I):I=tuple(map(tuple,I));B=E(I);A=V(B,0);C=J(A,1);D=J(A,2);F=L(C,(1,1),(2,2));H=L(D,(0,1),F);K=G(U,Z,S);M=K(H);N=X(0,(3,3));O=Q(N,5,M);return[*map(list,O)]
def J(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def K(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A,B):return K(A,P(A),Z(B))
def V(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def M(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A,B,C):return V(W(A,B),M(B,C))
def E(A,B):return frozenset((A,B)for B in Z(B))
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Y(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-S(A)+1
def L(A,a,b):return a if A else b
def U(a,b):return a==b
def p(I):I=tuple(map(tuple,I));A=X(I,3);B=Y(A);C=U(B,1);D=L(C,(0,2),(2,0));F=X(I,2);H=E(2,F);J=G(I,H,D);return[*map(list,J)]
def Y(A,B):return type(B)(A(B)for B in B)
def X(A):return type(A)(B for A in A for B in A)
def L(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def V(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def E(A,B):return X(Y(A,B))
def p(I):I=tuple(map(tuple,I));A=J(I,5);B=U(I,5,0);C=E(P,A);D=E(Z,A);F=V(B,1,C);G=V(F,5,D);return[*map(list,G)]
def S(A):return tuple(map(max,zip(*P(A))))
def Z(A):return tuple(map(min,zip(*P(A))))
def L(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Z(A)[1]+S(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def U(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def J(A,B):return lambda x:A(B(x))
def M(A):return max(enumerate(A))[1]
def X(A,B):return type(A)(A for A in A if B(A))
def Y(n):return n%2==0
def p(I):I=tuple(map(tuple,I));A=E(I);B=U(A,5);C=J(Y,M);D=X(B,C);F=V(A,3,D);G=E(F);return[*map(list,G)]
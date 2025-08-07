def V(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):return A[:len(A)//2]
def P(A):return A[len(A)//2+len(A)%2:]
def L(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def Y(A):return tuple(A for A in zip(*A[::-1]))
def Z(A):return L(P(Y(A)))
def J(A):return L(E(Y(A)))
def M(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def U(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=J(I);B=Z(I);C=X(A,4);D=X(B,3);E=U(C,D);F=M(A,6,E);return[*map(list,F)]
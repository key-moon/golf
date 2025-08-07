def X(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return tuple(map(max,zip(*P(A))))
def Z(A):return tuple(map(min,zip(*P(A))))
def J(A):
	if len(A)==0:return frozenset({})
	B=P(A);C,D=Z(B);E,F=S(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(B):
	if len(B)==0:return frozenset({})
	return J(B)-P(B)
def L(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def p(I):I=tuple(map(tuple,I));A=U(I,8);B=E(A);C=L(I,3,B);return[*map(list,C)]